"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command

MOCK_DATE = {
    "20230518":''' 
Operating hours :40 
Peak hours :76 
Minimum delivery score :80 
Store richness score :32 
Service richness score :80 
Marketing activity richness score :77 
The manual response rate of the recent 7 days of poor evaluation :32 
IM online response rate :89 
Store score :70 
Quality commodity rate :80 
Menu richness score :68 
Business responsibility cancellation rate score :70 
Meal reporting rate :80 
'''
}

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
