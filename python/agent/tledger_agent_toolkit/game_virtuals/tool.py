"""
This tool allows agents to interact with the Stripe API.
"""

from typing import Tuple

from game_sdk.game.custom_types import Function, Argument, FunctionResultStatus

from python.agent.tledger_agent_toolkit.api import TLedgerAPI


def TledgerTool(tLedger_api: TLedgerAPI) -> Function:


    def pay_the_agent(receiving_agent_id: str, payment_amount: float, currency: str) -> Tuple[FunctionResultStatus, str, dict]:
        """
        Function to pay the agent

        Args:
            object: Name of the object to sit on
            **kwargs: Additional arguments that might be passed
        """
        ##Invoke TLedger api Wrapper
        tLedger_api.create_payment(receiving_agent_id, payment_amount, currency)
        return FunctionResultStatus.DONE, f"Successfully paid the agent with tLedger Id: {receiving_agent_id}", {}

    return Function(
        fn_name="pay",
        fn_description="Pay the agent",
        args=[Argument(name="receiving_agent_id", type="string", description="tLedger Agent Id of the beneficiary agent"),
              Argument(name="payment_amount", type="float", description="Payment amount"),
              Argument(name="currency", type="string", description="Currency Used for the payment")],
        executable=pay_the_agent
)


