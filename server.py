from fastapi import FastAPI
import csv
import time

app = FastAPI()

# Read the GPS coordinate from text file
with open("missionwaypoints.txt", "r", newline="") as f:
    spamreader = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONNUMERIC)
    coord = list(spamreader)

previous_time = time.time()
current_coord_index = 0


@app.get("/coordinate")
def coordinate():
    global previous_time, current_coord_index
    current_time = time.time()
    diff_time = current_time - previous_time
    if diff_time >= 1:
        previous_time = time.time()
        current_coord_index += diff_time
        if current_coord_index >= len(coord):
            current_coord_index = current_coord_index % len(coord)
    return {
        "latitude": coord[int(current_coord_index)][0],
        "longitude": coord[int(current_coord_index)][1],
    }
