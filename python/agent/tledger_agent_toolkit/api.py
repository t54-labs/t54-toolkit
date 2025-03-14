"""Util that calls Stripe."""

from __future__ import annotations

import json
from typing import Optional
from pydantic import BaseModel



class TLedgerAPI(BaseModel):
    """ "Wrapper for TLedger API"""


    def __init__(self, api_key: str, api_secret: str):
        super().__init__()

    def pay_the_agent(self, object: str, **kwargs) -> None:
        """
        Function to pay the agent

        Args:
            object: Name of the object to sit on
            **kwargs: Additional arguments that might be passed
        """
        ##Invoke TLedger api







