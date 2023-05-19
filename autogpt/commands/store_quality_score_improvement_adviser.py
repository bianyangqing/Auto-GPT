"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command

MOCK_DATA = """
1,Extended business hours
2,Lower the minimum delivery fee
"""

@command(
    "store_quality_score_improvement_adviser",
    "Provide suggestions for store quality improvement based on historical store quality score",
    '"historical_store_quality_score": "<historical_store_quality_score>"',
)
def query_store_data(historical_store_quality_score: str):
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        question (str): question
    Returns:
        A result string from related docs
    """
    return MOCK_DATA
