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

    search = input('what would you like to search for? ')

    commentSearch = False
    commentBool = input('do you want to include comments in the search? (warning will be a huge loading time) (y/n)')
    if (commentBool == 'y'):
        commentSearch = True


    scrappy.scrape(search, commentSearch)
    scrappy.printResults()
    scrappy.turnToCSV()


if __name__ == "__main__": main()
