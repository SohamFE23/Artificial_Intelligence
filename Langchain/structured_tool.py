from typing import Dict,Union,List
from langchain_core.tools import tool
import re

def sum_nums_with_complex_output(inputs:str) -> Dict[str,Union[float,str]]:
    """
    Extracts and sums all integers and decimals frp, the input ..
    """
    matches= re.findall(r'-?\d+\.?\d*',inputs)
    if not matches:
        return {"result":"No numbers found in inputs."}
    try:
        numbers=[float(num) for num in matches]
        total=sum(numbers)
        return {"result":total}
    except Exception as e:
        return {"result": f"Error occured while processing. {str(e)}"}
