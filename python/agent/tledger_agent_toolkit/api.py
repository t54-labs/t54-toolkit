"""Util that calls Stripe."""

from __future__ import annotations

import json
from typing import Optional, List, Dict, Any

import requests
from pydantic import BaseModel, PrivateAttr


class TLedgerAPI:
    """ "Wrapper for TLedger API"""
    _api_key: str = PrivateAttr()
    _api_secret: str = PrivateAttr()
    base_url: str
    configuration: Dict[str, Any]

    def __init__(self, api_key: str, api_secret: str, base_url: str = "http://localhost:4000/api/v1",
                 configuration: Dict[str, Any] = None):
        """
        Initializes the TLedger Agent Toolkit.

        Args:
            api_key (str): The API key for TLedger authentication.
            api_secret (str): The API secret for TLedger authentication.
            base_url (str): The base URL for TLedger API requests.
            configuration (Dict[str, Any], optional): Configuration for enabling specific actions.
        """
        self._api_key = api_key
        self._api_secret = api_secret
        self.base_url = base_url
        self.configuration = configuration or {}

    def _request(self, method: str, endpoint: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Makes an HTTP request to the TLedger API.

        Args:
            method (str): HTTP method (GET, POST, etc.).
            endpoint (str): API endpoint to hit.
            data (Dict[str, Any], optional): Request payload.

        Returns:
            Dict[str, Any]: API response JSON.
        """
        headers = {
            "X-API-Key": self._api_key,
            "X-API-Secret": self._api_secret,
            "Content-Type": "application/json"
        }

        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, json=data, headers=headers)

        response.raise_for_status()  # Raise an error for non-2xx responses
        return response.json()


    def create_payment(self, receiving_agent_id: str, amount: float, currency: str) -> Dict[str, Any]:
        """
        Creates a payment request.

        Args:
            receiving_agent_id (str): The ID of the receiving agent.
            amount (float): The payment amount.
            currency (str): The currency (e.g., SOL, USDC).

        Returns:
            Dict[str, Any]: The created payment response.
        """
        # if not self.configuration.get("actions", {}).get("payment", {}).get("create", False):
        #     raise PermissionError("Payment creation is disabled in configuration.")
        print(f"Payment request for beneficiary agent: {receiving_agent_id}, amount: {amount}, currency: {currency}")
        payload = {
            "receiving_agent_id": receiving_agent_id,
            "payment_amount": amount,
            "currency": currency
        }
        return self._request("POST", "payment", payload)

    def get_payment_status(self, payment_id: str) -> Dict[str, Any]:
        """
        Retrieves the status of a payment.

        Args:
            payment_id (str): The ID of the payment.

        Returns:
            Dict[str, Any]: The payment details including status.
        """
        return self._request("GET", f"payment/{payment_id}")

    def wait_for_payment_success(self, payment_id: str, poll_interval: int = 5) -> Dict[str, Any]:
        """
        Polls until the payment status becomes "success".

        Args:
            payment_id (str): The ID of the payment.
            poll_interval (int): Time in seconds between each poll.

        Returns:
            Dict[str, Any]: The final payment response.
        """
        import time

        while True:
            response = self.get_payment_status(payment_id)
            status = response.get("status")

            print(f"Payment status: {status}")
            if status == "success":
                print("Payment has been successfully completed! ✅")
                return response

            time.sleep(poll_interval)

    def get_tools(self) -> List:
        """
        Returns a list of agent-compatible tools.

        Returns:
            List: List of functions for integration with AI frameworks.
        """
        return [
            self.create_payment,
            self.get_payment_status,
            self.wait_for_payment_success
        ]





