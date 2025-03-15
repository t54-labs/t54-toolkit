"""tLedger Agent Toolkit."""

from typing import List, Optional

from game_sdk.game.custom_types import Function
from pydantic import PrivateAttr
import json



from ..api import TLedgerAPI

from .tool import TledgerTool


class TledgerAgentToolkit:
    _tools: List[Function] = PrivateAttr(default=[])
    _tLedger_api: TLedgerAPI = PrivateAttr(default=None)

    def __init__(
        self, api_key: str, api_secret: str
    ):
        super().__init__()

        self.tLedger_api = TLedgerAPI(api_key=api_key, api_secret=api_secret)

        self._tools = [
            TledgerTool(self.tLedger_api)
        ]

    def get_tools(self) -> List[Function]:
        """Get the tools in the toolkit."""
        return self._tools

