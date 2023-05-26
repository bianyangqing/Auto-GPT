"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command

MOCK = """
The store id=223524545 is offline because you have been out of business for 8 days. 
If you want to go back online, please contact your account manager
"""

@command(
    "query_store_status",
    "1. Check the current status of the store; 2. Check the reason for going offline",
    '"store_id": "<store_id>"',
)
def query_store_status(args: str) -> str:
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        args (str): question
    Returns:
        A result string from related docs
    """
    return MOCK
