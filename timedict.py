#!/usr/bin/python3
"""JCOpinaldo | Tuesday Morning Brew
Given the data contained within isisnow, available from:

    http://api.open-notify.org/iss-now.json

write a program that displays the current:

At, <timestamp> this iss is:
    Longitude - <longitude>
    Latitude - <latitude>


"""
# make sure to define a function
def main():

    # source data:
    issnow = {"message": "success", "timestamp": 1617722667, "iss_position": {"longitude": "-179.5472", "latitude": "-51.6250"}}

    # my code:
    ts = issnow.get("timestamp")
    #print "At timestamp the iss is: "
    print(f"At, {issnow.get("timestamp")} the iss is: ")

    # print "longitude"
    longit = issnow.get("iss_position").get("longitude")
    print("Longitude - " + longit)
    print(f"Longitude - {issnow.get('iss_position').get('longitude')}
    


#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true

