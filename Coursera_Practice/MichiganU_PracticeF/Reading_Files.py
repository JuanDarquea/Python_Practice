# Reading_Files.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Download the file from the URL
url = "https://www.py4e.com//code3//words.txt?PHPSESSID=2bbfdfb2d3fa8f41fa2f0e131a6d3402"
filedir = os.getenv("coursera_mich_dir", ".")
data = requests.get(url).text

# Define the filename and path
filepath = os.path.join(filedir, "words2.txt")

# Save the file if it does not exist
if not os.path.exists(filepath):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(data)
else:
        print(f"The file {filepath} already exists.")

# Read the file
def read_file(file_path):
    """Read a text file and return its content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lstrip()
            content = content.upper()
        return content
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    return content
    
# Use the function to read the file and print its content
content = read_file(filepath)
print("\nFile content read all at once:")
print(content)
print("-" * 40)
print("\nReading file line by line:")

# Alternativelly, read the file line by line
with open(filepath, 'r', encoding='utf-8') as fh:
    for line in fh:
        l2 = line.rstrip()
        print(l2.upper())