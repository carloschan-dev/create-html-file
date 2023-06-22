#! /usr/bin/env python3

# create-html-file  A simple tool to create the basic stucture of html files 
# Copyright (C) 2023 carlos chan dev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser
from os.path import exists,isfile
from sys import exit

parser = ArgumentParser()
parser.prog = "create-html-file"
parser.description = "A simple tool to create the basic stucture of html files"
parser.add_argument("-f","--file",metavar="",default="index.html",help="set the name of the file")
parser.add_argument("-t","--title",metavar="",default="Document",help="set the title of the document")
parser.add_argument("-l","--lang",metavar="",default="en",help="set the language of the document")
parser.add_argument("-c","--color",metavar="",default="royalblue",help="set the color theme of the document")
parser.add_argument("-v","--version",action="version",version="%(prog)s 1.0")
parser.epilog = "Copyright (c) carlos chan dev 2023"
args = parser.parse_args()

template_config = {
    "$title":args.title,
    "$lang":args.lang,
    "$color":args.color
}

FILE_NAME = args.file

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="$lang">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="$color">
    <title>$title</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>"""

def export_template(new_template):
    with open(FILE_NAME,"w") as file:
        file.write(new_template)

def create_template():
    new_template = HTML_TEMPLATE
    for item in template_config.items():
        new_template = new_template.replace(item[0],item[1])
    return new_template

def main(args):
    new_template = create_template()
    export_template(new_template)

if __name__ == "__main__":
    if exists(FILE_NAME) and isfile(FILE_NAME):
        print(f"Error: The file {args.f} already exists")
        exit(1)
    main(args)