"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command


@command(
    "chatgpt_export",
    "If you do not know what to do, you can ask this command for help. before ask this command,you should ask business_expert for some knowledge.The prompt for this command should using the format like 'knowledge:XXXX\ntask:XXXX'",
    '"prompt": "<prompt>"',
)
def ask(prompt: str) -> list[str]:
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        question (str): question
    Returns:
        A result string from related docs
    """
    return ["1","2"]
