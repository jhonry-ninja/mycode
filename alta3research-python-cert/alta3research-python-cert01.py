#!/usr/bin/python3
"""JC | Alta3 Research Python Certification"""

import requests

# Define API URL
nasa_url = 'https://api.nasa.gov/planetary/apod?api_key=VaH8Za0R3yrCZt9E4dbWii3Xp3rQCijgv2Xebkdb'

def main():
        # Call the API
        nebula = requests.get(nasa_url)

        # translate the json into python lists and dictionaries
        got_nebula = nebula.json()

        # display the nebula
        # print(got_nebula)

        # print 'Explanation: ' and the value of the 'explanation' key 
        # print('\nExplanation: ', got_nebula['explanation'])

        # print 'Explanation: ' and the value of the 'copyright' key 
        print('\nCopyright: ', got_nebula['copyright'])




if __name__ == '__main__':
    main()