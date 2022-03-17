from bs4 import BeautifulSoup
import requests

content = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(content, 'lxml')
job = soup.find("li", class_ ='clearfix job-bx wht-shd-bx')
company = job.find('h3', class_ = 'joblist-comp-name').text
skills = job.find('span', class_= 'srp-skills').text


print(f'''Company Name: {company.strip()}
Skills: {skills.strip()}''')
