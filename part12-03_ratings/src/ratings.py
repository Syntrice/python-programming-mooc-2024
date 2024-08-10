# TEE RATKAISUSI TÄHÄN:

def sort_by_ratings(items: list[dict]) -> list[dict]:
    def order_by_season(item: dict):
        return item['rating']
    
    return sorted(items, key=order_by_season, reverse=True)