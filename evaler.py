"""
Name: Gabriel Engberg
Date: 31-10-2021
Info:
<Insert information about file>
"""


def before(src:str, i:int, invert=False)-> str | None:
    """Returns char at index before the give index, or after if invert.

    Args:
        src (str): [mutable str]
        i (int): [current index, standing on]
        invert (bool, optional): [gives char after index]. Defaults to False.

    Returns:
        [str | None]: [returns char before else None if out of range]
    """    
    match i:
        case 0:
            return None
        case len(src):
            return None
    if invert:
        return src[i+1]
    return src[i-1]


def count_ops(source: str, comparer: str | list) -> dict: 
    op_dict = dict(zip(comparer, [0] * len(comparer)))
    
    

def evaluate(source: str) -> int | float:
    operators = ["(", "**", "^", "/", "*", "+", "-"]
    operator_count = str()


if __name__ == "__main__":
    count_ops("2+2*3", ["(", "**", "^", "/", "*", "+", "-"])
    # evaluate(source="2+3+5**2")