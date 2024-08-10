# Write your solution here:

def sort_by_seasons(items: list[dict]) -> list[dict]:
    def order_by_season(item: dict):
        return item['seasons']
    
    return sorted(items, key=order_by_season)