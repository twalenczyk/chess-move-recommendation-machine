# Converts text file to a Board
import sys
from board import Board
from bs4 import BeautifulSoup
from selenium import webdriver
from piece import Piece

# returns a list of pieces
def parse_piece_tags(tags):
    ret = []
    for i in range(len(tags)):
        cur = tags[i]
        if cur['class'][0] != 'ghost':
            ret.append(Piece(cur['class'][0], cur['class'][1]))
    return ret

def main():
    # grab the webpage
    url = sys.argv[1]
    browser = webdriver.Chrome(executable_path=r"/Users/twalen/Desktop/WebDrivers/chromedriver")
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    # translate_index = 64
    # grab the pieces
    piece_tags = soup.find_all('piece')
    pieces = parse_piece_tags(piece_tags)

    # build chess board



if __name__ == '__main__':
    main()
