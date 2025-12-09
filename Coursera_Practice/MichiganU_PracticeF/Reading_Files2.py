# Reading_Files2.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Set up the file directory and URL
url = "https://www.py4e.com/code3/mbox-short.txt?PHPSESSID=827130571fb5a8da475724010e6f3538"
filedir = os.getenv("coursera_mich_dir", ".")
data = requests.get(url).text

# Define the filename and path
filepath = os.path.join(filedir, "mbox-short.txt")

# Save the file if it does not exist
if not os.path.exists(filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(data)
    print(f"The file {filepath} has been created.")
else:
        print(f"The file {filepath} already exists.")

# Read the file
# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fname = "mbox-short.txt"
i = 0
s = 0
with open(fname) as fh:
    for line in fh:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        else:
            cont = line.find(":")
            ncont = line[cont+2:]
            fcont = float(ncont)
            s = s + fcont
        i = i + 1   
        
avg = s / i
print("Average spam confidence:", avg)