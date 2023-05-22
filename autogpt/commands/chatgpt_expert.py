"""Code evaluation module."""
from __future__ import annotations
from autogpt.llm.llm_utils import create_chat_completion
from autogpt.config.config import Config

from autogpt.commands.command import command

cfg = Config()

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
    massage=[{"role": "user", "content": args}]
    return create_chat_completion( massage, cfg.fast_llm_model)
