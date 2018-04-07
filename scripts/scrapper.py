# scrapper.py
# Written by Matthew Timms for HardHack2018
# Scraps weebly stuff from exported archive files

from bs4 import BeautifulSoup
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

for file in os.listdir(parent_dir):  # list files in directory
    if file.endswith(".html"):
        file_path = os.path.join(parent_dir, file)
        soup = BeautifulSoup(open(file_path, 'r', encoding='utf-8'), "html.parser")

        # Remove footer-wrap div
        try:
            soup.find('div', {'class': 'footer-wrap'}).decompose()
        except AttributeError:
            pass

        # Replace /uploads
        soup_string = str(soup).replace('/uploads', 'uploads')
        soup = BeautifulSoup(soup_string, "html.parser")

        # # dbg only: doesn't overwrite
        # path, ext = os.path.splitext(file_path)
        # file_path = path + '1' + ext

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
