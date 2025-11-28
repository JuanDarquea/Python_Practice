# Example_URL_Translation.py

from googletrans import Translator
import requests

translator = Translator()

url = 'https://introcomputing.org/'

page = requests.get(url)

translated = translator.translate(page.text)

print(translated)