# !/usr/bin/env python3
# encoding: utf-8
# Word_Count_Test
import os
from dotenv import load_dotenv # to load environment variables from .env file

load_dotenv()

filedir = os.getenv("coursera_mich_dir", ".")
filename = "words.txt"

# Get the name of the file and open it
#name = input('Enter the words: ')
name = os.path.join(filedir, filename)
handle = open(name)

# Count word frecuency
count = dict()
for line in handle:
    words = line.split(sep=None, maxsplit=-1)
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)

# Find the most common word
bigcount = None
bigword = None
for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Print result
print("Word:", bigword, "Count:", bigcount)