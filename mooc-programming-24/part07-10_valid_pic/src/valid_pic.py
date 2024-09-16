# Write your solution here
from datetime import datetime, timedelta

def is_it_valid(pic: str):
    
    # PIC must be equal to 11
    if len(pic) != 11:
        return False
    
    try:
        
        # the century marker must be correct. + for 1800s, - for 1900s, or A for 2000s.
        century = ""
        if pic[6] == "+":
            century = "18"
        elif pic[6] == "-":
            century = "19"
        elif pic[6] == "A":
            century = "20"
        else:
            return False
        
        # the first six characters must be a valid date in format ddmmyy
        birthdate = datetime(year=int(century + pic[4:6]), month=int(pic[2:4]), day=int(pic[0:2]))
        
        # the control character must be correct
        index = int(pic[0:6] + pic[7:10]) % 31
        if "0123456789ABCDEFHJKLMNPRSTUVWXY"[index] != pic[10]: return False
    
    except ValueError:
        return False
    
    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))