# Write your solution here
from typing import Callable

def search(products: list[tuple[str,float,int]], criterion: Callable[[tuple[str,float,int]], bool] = lambda x: True):
    
    result = []
    for product in products:
        if criterion(product):
            result.append(product)
            
    return result