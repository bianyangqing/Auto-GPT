"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command


@command(
    "chatgpt_expert",
    "The args for this command should using the format like "
    "'prompt:'context or details about the task, provide as much information as you can \n"
    "'task:'the task you want to do'",
    '"args": "<args>"',
)
def ask(args: str) -> str:
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        question (str): question
    Returns:
        A result string from related docs
    """
    return ["1","2"]
