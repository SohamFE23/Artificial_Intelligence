from typing import List
from langchain_core.tools import tool

@tool
def add_numbers_with_option(numbers: List[float],absolute:bool=False)-> float:
    """
    Adds a list of Numbers provided by the user. If absolute is set to True, it will add the absolute values of the numbers.
    """
    if absolute:
        numbers=[abs(num) for num in numbers]
    return sum(numbers)

