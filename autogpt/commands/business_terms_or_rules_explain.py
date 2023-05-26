"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command

MOCK = """
If you want to go online again, please contact your sales manager and ask him to help you with the online operation
"""

@command(
    "business_expert",
    # "Before you call chatgpt_expert command, you should call this command to get some export knowledge."
    # "Explain any business terms or rules that you don't understand."
    # "Give you some additional information about a topic. "
    "args for this command can be the task",
    '"args": "<args>"',
)
def query_knowledge(args: str) -> str:
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        args (str): question
    Returns:
        A result string from related docs
    """
    return MOCK
