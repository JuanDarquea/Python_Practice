from bs4 import BeautifulSoup
import requests

# reading of sample URL containing job listings
try:
    url = 'https://realpython.github.io/fake-jobs/'
    response = requests.get(url)
except Exception as e:
    print(f'Error retrieving page: {e}')
    exit()

# printing status code and first 3000 characters of the response for debbugging purposes
print('Page response:', response.status_code)
#print(response.text[:1000]) # prints first X characters of the HTML content

# parsing the HTML content using BeautifulSoup
try:
    soup = BeautifulSoup(response.text, 'lxml')
    print(f'\nPage title:', soup.title.text) # prints the title of the webpage
    # .text or .string can be used to get the text content
except Exception as e:
    print(f'Page could not be parsed, error: {e}')
    exit()

# finding all job cards on the page
try:
    jobs = soup.find_all('div', class_='card-content')
    print(f'Found {len(jobs)} job cards')
except Exception as e:
    print(f'Error finding job cards: {e}')
    exit()

# extracting and printing job titles from each job card
print(f'\nJob Titles:')
try:
#    raise Exception("Simulated error for demonstration purposes")  # Remove or comment this line to proceed normally
    for i, job in enumerate(jobs, 1):
        title = job.find('h2', class_='title is-5').text
        company = job.find('h3', class_='subtitle is-6 company').text
        location = job.find('p', class_='location').text.strip()
        learn = job.find_all('a')[0]['href'] # method 1 of link result when multiple tags called the same on the same level
        #apply = job.find('a', string='Apply')['href'] # method 2 of link result, same situation
        footer = job.find('footer', class_='card-footer')
        apply = footer.find('a', string='Apply')['href'] # more robust alternative method 2 using footer context

        print(f'Job {i}: {title}', 
              f'\nCompany: {company}', 
              f'\nLocation: {location}', 
              f'\nLearn: {learn}', 
              f'\nApply: {apply}'
              )
        print()
except Exception as e:
    print(f'Error extracting job details: {e}')
    exit()

print()
i = 0 # counter for Python jobs
# filtering and printing only Python job listings
print('Python Jobs:')
for job in jobs:
    if 'Python' in job.find('h2', class_='title is-5').text: # check if 'Python' is in the job title
        i = i + 1 # increment counter
        print(f'Found a Python job {i}:', job.find('h2', class_='title is-5').text) # print job title

# Note: To run this code, ensure you have the 'requests' and 'beautifulsoup4' libraries installed.
