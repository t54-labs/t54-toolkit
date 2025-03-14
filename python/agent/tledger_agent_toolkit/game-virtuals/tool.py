"""
This tool allows agents to interact with the Stripe API.
"""

from __future__ import annotations

from collections.abc import Awaitable
from typing import Any, Tuple
import json

from game_sdk.game.custom_types import Function, Argument, FunctionResultStatus

from python.agent.tledger_agent_toolkit.api import TLedgerAPI


def TledgerTool(tLedger_api: TLedgerAPI) -> Function:

    def pay_the_agent(object: str, **kwargs) -> Tuple[FunctionResultStatus, str, dict]:
        """
        Function to pay the agent

        Args:
            object: Name of the object to sit on
            **kwargs: Additional arguments that might be passed
        """
        ##Invoke TLedger api Wrapper
        tLedger_api.pay_the_agent(object)
        return FunctionResultStatus.DONE, f"Successfully paid the agent for the {object}", {}


    return Function(
        fn_name="pay",
        fn_description="Pay the agent",
        args=[Argument(name="object", type="string", description="Pay the agent for the object")],
        executable=pay_the_agent
)
