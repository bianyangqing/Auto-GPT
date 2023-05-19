"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command


@command(
    "business_expert",
    "Explain any business terms or rules that you don't understand.Give you some additional information about a topic",
    '"question": "<question>"',
)
def query_knowledge(question: str) -> list[str]:
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        question (str): question
    Returns:
        A result string from related docs
    """
    return ["1","2"]
