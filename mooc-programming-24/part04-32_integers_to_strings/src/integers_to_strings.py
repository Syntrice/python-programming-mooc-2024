# Write your solution here
 
def formatted(floats: list[float]):
    result = []
    for value in floats:
        result.append(f"{value:.2f}")
    return result