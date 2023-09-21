# UAS-Coding-Challenge-2023
UBC UAS Software Systems Coding Challenge - GPS Speed Challenge (B-GPS-0)

The software contains a server used to serve GPS coordinate using REST API and a speed calculation program.

`server.py` is a fastapi server used to serve GPS coordinate by calling `GET /coordinate`. 

To run the server `uvicorn server:app`

The server will update the GPS coordinate every one second. (if the request come in before the coordinate have been updated, the server will return old coordinate)

`speed.py` is a program to calculate speed in m/s and average speed since the program start.
