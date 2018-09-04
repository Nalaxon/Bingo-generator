#!/usr/bin/env python
#-*-coding: utf-8 -*-

import random, sys

# Check arguments which contain all
if len(sys.argv) != 5:
    print("Command: " + sys.argv[0] + " [file of datas] [output file] [# of cards] [# of dimensions]")
    print("Sample: " + sys.argv[0] + " bingo.txt bingo.html 10 5")
    sys.exit(1)

# read in the bingo datas
file_input = open(sys.argv[1], 'r')
datas = [line.strip() for line in file_input.readlines()]
datas = list(filter(lambda x: x != "", datas))
file_input.close()

# Set sys.argv[4] to dimention's table
dim =  int(float(sys.argv[4]))

# read number of line for check the bingo datas
file_input = open(sys.argv[1], 'r')
num_lines = sum(1 for line in file_input)
file_input.close()

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
    mid_dim = (dim*dim)/2
    final_dim = (dim*dim)-1
    ts = datas[:mid_dim] + ["<p style=\"color:white;\">Bingo!!</p>"] + datas[mid_dim:final_dim]
    if pagebreak:
        tmp = "<center><img src=\"logo-bingo.png\" width=\"520\" height=\"130.4\" /></center>\n"
        tmp += "<table class=\"newtable\">\n"
    else:
        tmp = "<center><img src=\"logo-bingo.png\" width=\"520\" height=\"130.4\" /></center>\n"
        tmp += "<table>\n"
    for i, data in enumerate(ts):
        if i % dim == 0:
            tmp += "\t<tr>\n"
        if i == (mid_dim):
            tmp += "\t\t<td style=\"background-color:black;\">" + data + "</td>\n"
        else:
            tmp += "\t\t<td>" + data + "</td>\n"
        if i % dim == (dim-1):
            tmp += "\t</tr>\n"
    tmp += "</table>\n"
    return tmp


# Write an output as HTML file
file_output = open(sys.argv[2], 'w')
file_output.write(Header)
cards = int(sys.argv[3])
for i in range(cards):
    random.shuffle(datas)
    if i != cards - 1:
        file_output.write(getBingoTable(datas))
    else:
        file_output.write(getBingoTable(datas, False))
file_output.write("</body></html>")

file_output.close()
