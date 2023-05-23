"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command

MOCK_DATE = """
each factor score of the store with id=223524545 :
Operating hours score:40 \\n
Peak hours score:32 \\n
Minimum delivery score :80 \\n
Store richness score :32 \\n
Service richness score :80 \\n
Marketing activity richness score :77 \\n
The manual response rate of the recent 7 days of poor evaluation :32 \\n
IM online response rate :89 \\n
Store score :70 \\n
Quality commodity rate :80 \\n
Menu richness score :68 \\n
Business responsibility cancellation rate score :70 \\n
Meal reporting rate :41 
"""

@command(
    "query_historical_store_data",
    "Query historical store quality score data by store id",
    '"store_id": "<store_id>"',
)
def query_store_data(store_id: str):
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        question (str): question
    Returns:
        A result string from related docs
    """
    return MOCK_DATE
