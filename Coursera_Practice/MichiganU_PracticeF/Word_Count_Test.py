# !/usr/bin/env python3
# encoding: utf-8
# Word_Count_Test
import os
from dotenv import load_dotenv # to load environment variables from .env file
load_dotenv()

filePath = os.getenv("docx_translator_dir"), "\\TestDocument.docx"

# Get the name of the file and open it
#name = input('Enter the words: ')
name = filePath
handle = open(name, 'r', encoding='utf-8')
all_words = dict()
all_words = handle.read().text()
handle.close()

# Count word frecuency
count = dict()
for line in all_words:
    words = line.split(sep=None, maxsplit=-1)
    for word in words:
        count[word] = count.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Print result
print(bigword, bigcount)