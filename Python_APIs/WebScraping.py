# API is like a mediator
# web scraping is like using crud operations in html content
# the process of extracting data from websites (live apps)
# without using APIs we can get data using web scraping
# html tags are important in this data type

# beautifulsoup is html parser
# install BeautifulSoup4 package

"""

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://risenshinetechnologies.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

# Extract specific elements from the page
# For example, let's say you want to extract all links (anchor tags)
links = soup.find_all('a')

# Print out all the links
for link in links:
    print(link.get('href'))

# printing head content text only
metatag = soup.find("h1", attrs='rns-h1')
print(metatag.text)

"""


# finding all jobs in python website

import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.python.org/jobs/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup)

# finding jobs from python website
#finding_company = soup.find_all("h2", attrs='listing-company')
finding_jobs = soup.find_all("h2", class_='listing-company')
#print(finding_jobs)

#print(type(finding_jobs))

for job_post in finding_jobs:
    print(job_post.a.text)

# finding date and time from python website

finding_posted_date = soup.find_all("span", class_='listing-posted')

#print(finding_posted_date)

for posted_date in finding_posted_date:
    print(posted_date.time.text)


# combine above two lists in to one like side by side
for job_post, posted_date in zip(finding_jobs, finding_posted_date):
    print(job_post.a.text, posted_date.time.text)

