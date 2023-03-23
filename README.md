# Advanced-Python

# EX1
Module that converts coordinates from WGS84 to L-Est97 and vice versa, created install package and uploaded to test.pypi.org.

User interface which uses created and installed module for converting coordinates. The pip install command is something like this: pip install https://test.pypi.org/simple/transformations-username/
There are documentation and tests also.

Simple Flask webpage which uses installed module for converting coordinates. There are two input fields (X and Y) and two output fields and 'Convert' button.

# EX2
Databases and Python

Used plain SQL language to:

1) Created SQLite database DINERS, with two related tables CANTEEN and PROVIDER

Table CANTEEN fields: ID, ProviderID, Name, Location,  time_open, time_closed (weekday doesn't matter).

Table Provider fields: ID, ProviderName.

2) Inserted IT College canteen data by separate statement, other canteens as one list.

3) Created query for canteens which are open 16.15-18.00

4) Created query for canteens which are serviced by Rahva Toit. 

B) Used SqlAlchemy to do same steps again
# EX3
The task is to draw the direct flights departing from Tallinn Airport in the pre-corona period and now on the map of Europe. The OpenFlights Airports Database https://openflights.org/data.html has more than 14,000 airports all over the world, but regular flights from Tallinn take place to only a few dozen.

Airports data with geographic coordinates:
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat

Pre-corona direct flights from Tallinn:
https://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud20.csv

Direct flights from Tallinn in February 2023:
https://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud23.csv

The result is saved in EX3 directory as map.png file.
# EX4
