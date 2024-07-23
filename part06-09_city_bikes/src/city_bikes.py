# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    
    data = {}
    
    with open(filename) as file:
        
        header_column = True
        for line in file:
            if header_column == True:
                header_column = False
                continue
            
            line = line.strip()
            parts = line.split(";")
            
            data[parts[3]] = (float(parts[0]),float(parts[1]))
            
    return data

def distance(stations: dict, station1: str, station2: str):
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    return math.sqrt(x_km**2 + y_km**2)



def greatest_distance(stations: dict):
    greatest = (None, None, 0)
    
    for key1 in stations.keys():
        for key2 in stations.keys():
            d = distance(stations, key1, key2)
            if d > greatest[2]:
                greatest = (key1, key2, d)
    return greatest
            
            
    
    
    
            
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)