#!/usr/bin/env python
#-*-coding: utf-8 -*-

import random, sys
import argparse

# set up argparser
aparser = argparse.ArgumentParser(description="Create bingo sheets")
aparser.add_argument("--wordlist", help="File includes words for bingo, one word per line.", required=True, type=argparse.FileType('r'))
aparser.add_argument("--output", help="Filename for the resulting html outputfile.", default="bingo-output.html", type=argparse.FileType('w'))
aparser.add_argument("--card_size", help="Size of card, should be an odd number.", type=int, default=3)
aparser.add_argument("--card_count", help="Amount of card that should be created.", type=int, default=1)
aparser.add_argument("--branding", help="Use branding, text can assigned here.", type=str)
aparser.add_argument("--image_directory", help="Directory which includes images, images have to have the same name as the words (jpg)", type=str)
aparser.add_argument("--moderator_cards", help="Also generate moderator cards", action='store_true')

args = aparser.parse_args(sys.argv[1:])

# read in the bingo datas
file_input = args.wordlist
datas = [line.strip() for line in file_input.readlines()]
datas = list(filter(lambda x: x != "", datas))
file_input.close()

# Set sys.argv[4] to dimention's table
dim =  int(float(args.card_size))

# Check if data less then pow(dimension,2) -> exit
if (pow(dim,2) > len(datas)):
    print("Your input is less than dimensions, please try again")
    sys.exit(1)

# HTML5 Code @ Header File
Header = ("<!DOCTYPE HTML>\n"
         "<html>\n"
         "<head>\n"
         "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n"
         "<title>Create your own Bingo</title>\n"
         "<style type=\"text/css\">\n"
         "\tbody { font-size: 14px; }\n"
         "\ttable { margin: 40px auto; border-spacing: 2px; border-style: solid; border-color: #000000;}\n"
         "\t.newtable { page-break-after:always; }\n"
         "\ttr { height: 60px; }\n"
         "\ttd { text-align: center; border: thin black solid; padding: 10px; width: 70px; height:70px; }\n"
         "</style>\n</head>\n<body>\n")

# Generate an HTML table implementation of the bingo card for datas
def getBingoTable(datas, pagebreak = True):
    mid_dim = int((dim*dim)/2)
    final_dim = (dim*dim)
    ts = datas[:mid_dim]
    if args.branding:
        ts = ts + ["<p style=\"color:white;\">" + args.branding + "</p>"] + datas[mid_dim:final_dim-1]
    else:
        ts = ts + datas[mid_dim:final_dim]

    if pagebreak:
        tmp = "<center><img src=\"logo-bingo.png\" width=\"520\" height=\"130.4\" /></center>\n"
        tmp += "<table class=\"newtable\">\n"
    else:
        tmp = "<center><img src=\"logo-bingo.png\" width=\"520\" height=\"130.4\" /></center>\n"
        tmp += "<table>\n"
    for i, data in enumerate(ts):
        if i % dim == 0:
            tmp += "\t<tr>\n"
        if (i == (mid_dim)) and args.branding:
            tmp += "\t\t<td style=\"background-color:black;\">" + data + "</td>\n"
        else:
            tmp += "\t\t<td>" + data + "</td>\n"
        if i % dim == (dim-1):
            tmp += "\t</tr>\n"
    tmp += "</table>\n"
    return tmp


# Write an output as HTML file
file_output = args.output
file_output.write(Header)
cards = int(args.card_count)
for i in range(cards):
    random.shuffle(datas)
    if i != cards - 1:
        file_output.write(getBingoTable(datas))
    else:
        file_output.write(getBingoTable(datas, False))
file_output.write("</body></html>")

file_output.close()
