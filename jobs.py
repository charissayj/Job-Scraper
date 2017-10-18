from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

jobs_url = 'https://www.indeed.com/jobs?q=web+developer&l=Roanoke%2C+TX'

#opening connection and grabbing the page
uClient = uReq(jobs_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grab all divs with a class of result
results = page_soup.findAll("div", {"class": "result"})
#print len(results)

filename = "jobs.csv"
f = open(filename, "w")

headers = "Title, Company, Location, Experience, Link \n"

f.write(headers)

for result in results:
    title = result.a["title"]

    company = result.findAll('span', {'class':'company'})
    company_name = company[0].text.strip()

    location = result.findAll('span', {'class':'location'})
    location_name = location[0].text.strip()

    summary = result.findAll('span', {'class':'summary'})
    job_summary = summary[0].text.strip()

    exp = result.findAll('span', {'class':'experienceList'})
    experience = exp[0].text.strip()

    link = result.a['href']
    job_link = ("https://www.indeed.com" + link)

    print title
    print company_name
    print location_name
    print job_summary
    print experience
    print job_link

    f.write(title + "," + company_name + "," + location_name + "," + experience + "," + job_link + "\n")

f.close()