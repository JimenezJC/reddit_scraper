import datetime
import random
import re
import sys
import urllib.request

from bs4 import BeautifulSoup

from scraper import Scraper

def main():
    """
    This function is the main function for the entire
    program
    """    
    print('hello, this program will scrape reddit for your search terms')
    subBool = input('do you want to search a specific subreddit? (y/n) ')
    subReddit = None
    
    if(subBool == 'y'):
        subReddit = input('which subreddit would you like to search for? ')
    
    scrappy = Scraper(subReddit)

    search = input('what would you like to serach for? ')

    scrappy.scrape(search)
    


    


    




