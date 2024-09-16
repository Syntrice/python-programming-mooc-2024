# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date

def list_years(dates: list):
    years = []
    
    for d in dates:
        years.append(d.year)
        
    return sorted(years)