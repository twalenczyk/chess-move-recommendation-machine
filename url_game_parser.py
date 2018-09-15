# Converts text file to a Board
import sys
from board import Board
from bs4 import BeautifulSoup
from selenium import webdriver
from piece import Piece

# returns a list of pieces
def parse_piece_tags(tags):
    ret = []
    for tag in tags:
        print(tag['style'].split(' ')[1].split('(')[1])
        lead_tag = tag['class'][0]
        if lead_tag != 'ghost':
            ret.append(Piece(lead_tag, tag['class'][1]))
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
    b = Board(pieces)
    b.print_board()



if __name__ == '__main__':
    main()
