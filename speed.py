from geopy import distance
import requests
import time

URL = "http://localhost:8000/coordinate"
INTERVAL = 1

previous_coord = None
total_distance_traveled = 0
total_time = 0

previous_time = time.time()

while True:
    start_time = time.time()
    coord = requests.get(URL).json()
    if previous_coord == None:
        previous_coord = coord
        continue
    distance_traveled = distance.distance(
        (previous_coord["latitude"], previous_coord["longitude"]),
        (coord["latitude"], coord["longitude"]),
    ).meters
    total_distance_traveled += distance_traveled
    total_time += 1
    print(f"Current Speed: {distance_traveled:.3f}, Average Speed: {total_distance_traveled/total_time:.3f}")
    previous_coord = coord
    time.sleep(INTERVAL - (time.time() - start_time))