import urllib.request
from bs4 import BeautifulSoup
import datetime
import random
import re
import sys 



def main():
    if(len(sys.argv) < 1):
        sys.exit('ERROR: No arguements given.')
            
