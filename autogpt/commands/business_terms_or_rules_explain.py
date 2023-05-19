"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command


@command(
    "business_terms_or_rules_explain",
    "Explain any business terms or rules that you don't understand",
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
