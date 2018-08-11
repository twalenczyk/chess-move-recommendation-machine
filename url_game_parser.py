# Converts text file to a Board
import sys
from board import Board
from bs4 import BeautifulSoup
from selenium import webdriver

def parse_piece_tags(tags):
    print(pieces)

def main():
    # grab the webpage
    url = sys.argv[1]
    browser = webdriver.Chrome(executable_path=r"/Users/twalen/Desktop/WebDrivers/chromedriver")
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    # translate_index = 64
    # grab the pieces
    pieces = soup.find_all('piece')
    parse_piece_tags(pieces)

    # build chess board



if __name__ == '__main__':
    main()
