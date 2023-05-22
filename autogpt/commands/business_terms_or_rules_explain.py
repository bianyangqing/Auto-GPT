"""Code evaluation module."""
from __future__ import annotations

from autogpt.commands.command import command

MOCK = """
Store quality scoring rules:\\n
1,Operating hours score, weight:5%, caliber:Average operating hours of the last 7 days\\n
2,Peak operating hours score, weight:15%, caliber:Average peak operating hours of recent 7 days\\n
3,Minimum delivery price score, weight:2%, caliber:Lowest starting price yesterday\\n
4,Store richness score, weight:9%, caliber:Number of types of stores installed yesterday\\n
5,Service richness score, weight:5%, caliber:Yesterday's service richness\\n
6,Marketing activity richness score, weight:10%, caliber:Yesterday marketing richness\\n
7,Manual response rate of negative comments in recent 7 days score, weight:4%, caliber:Manual response rate of negative comments in recent 7 days\\n
8,IM online response rate score, weight:10%, caliber:Online response rate within 5 minutes in recent 7 days\\n
9,Store rating score, weight:4%, caliber:Yesterday's business rating\\n
10,Quality commodity rate score, weight:10%, caliber:Yesterday's rate of quality goods = number of quality goods/number of online goods\\n
11,Menu richness score, weight:10%, caliber:Richness of yesterday's menu\\n
12,Business responsibility cancellation rate score, weight:5%, caliber:Cancellation rate of business responsibility in recent 7 days\\n
13,Reporting rate of meals served score, weight:11%, caliber:Meal reporting rate of the last 7 days/overtime demand rate of the last 7 days\\n
"""

@command(
    "business_expert",
    # "Before you call chatgpt_expert command, you should call this command to get some export knowledge."
    # "Explain any business terms or rules that you don't understand."
    # "Give you some additional information about a topic. "
    "args for this command can be the task",
    '"args": "<args>"',
)
def query_knowledge(args: str) -> list[str]:
    """
    Invoke the vector retrieval service to query and question-related doc


    Parameters:
        args (str): question
    Returns:
        A result string from related docs
    """
    return ["1","2"]
