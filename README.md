# tLedger Agent Toolkit

The **tLedger Agent Toolkit** allows integration with TLedger APIs for handling Agent to Agent payments using popular agent frameworks like Virtual's GAME sdk, ai16z etc.

## Installation

To install the package, use:

```bash
pip install tledger-agent-toolkit
```
### Requirements
* Python 3.11+

## Usage

To use the **tLedger Agent Toolkit**, configure it with your API credentials and actions.

```python
from agents import Agent
from tledger_agent_toolkit import TLedgerAgentToolkit

# Initialize TLedger toolkit
tledger_agent_toolkit = TLedgerAgentToolkit(
    api_key="your_api_key",
    api_secret="your_api_secret",
    configuration={
        "actions": {
            "payment": {
                "create": True
            }
        }
    }
)

# Use it in an AI agent
tledger_agent = Agent(
    name="TLedger Agent",
    instructions="You are an expert at interacting with TLedger APIs for payments.",
    tools=tledger_agent_toolkit.get_tools()
)
```

## Features

- **Payment API Support:** Create and manage payments via TLedger.  
- **Easy Integration:** Works seamlessly with AI agent frameworks.  
- **Customizable Actions:** Configure available tLedger actions for agents via configuration.  
