import requests
import curses
import curses.textpad
import sys
import os
from helper import *
from dotenv import load_dotenv

# Read environment variables from .env file
load_dotenv()

base_url = os.environ['BASE_URL']
version = os.environ["VERSION"]

# Set up headers
headers = {
    "Authorization": f"Basic {os.environ['BEARER_TOKEN']}", 
    "CwtLicenseKey": f"{os.environ['CWT_LICENSE_KEY']}"
    }

## All the endpoints to be tested we can be more specific as we go ahead
class Endpoint:

    def __init__(self, text, url="", acceptsParams =False):
        self.text = text
        self.url = url
        self.acceptsParams = acceptsParams
    
    # We need to make multiple request types here eventualy
    def makeRequest(self,stdscr):
        url = ""
         #check if we are passing query params we could copy automatically
        if self.acceptsParams == True :
            queryParam = get_text_input(stdscr)
            url = f"{base_url}{version}{self.url}{queryParam.strip()}"
        else :
            url = f"{base_url}{version}{self.url}"

        try:
            # Make an HTTP GET request
            response = requests.get(url, headers=headers)
            display_json(stdscr,response.text)

        except Exception as e:
            display_json(stdscr, str(e) )
    

endPoints = [
    Endpoint("Check Status", "/Status"),
    Endpoint("Get Products", "/Products"),
    Endpoint("Get Product Details","/Products/", True),
    Endpoint("Exit")
]

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()

    selected_option = 0
    options = []
    #populate the options
    for e in endPoints:
        options.append(e.text)

    while True:
        stdscr.clear()
        
        # Display the options
        for count, option in enumerate(options):
            if count == selected_option:
                stdscr.addstr(count, 0, f"> {option}", curses.A_BOLD)
            else:
                stdscr.addstr(count, 0, f"  {option}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_option = max(0, selected_option - 1)
        elif key == curses.KEY_DOWN:
            selected_option = min(len(options) - 1, selected_option + 1)
        elif key == ord('\n'):
            if selected_option < (len(options)-1):
                # Make the request for the selected option 
                # we can work on differerent request types GET/POST/PUT/DELETE
                endPoints[selected_option].makeRequest(stdscr)
            else:
                sys.exit(0)    

            stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
