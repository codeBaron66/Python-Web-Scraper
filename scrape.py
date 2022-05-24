import requests
import pandas as pd
from bs4 import BeautifulSoup

def extract(page):
	url = f'https://uk.indeed.com/jobs?q=IT%20Support%20Technician&l=Plymouth&radius=100&start={page}&vjk=8c4e6a4a97d5fb7a'
	headers = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
	r = requests.get(url, headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup

def transform(soup):
	divs = soup.find_all ('div', class_ ='slider_container')
	for item in divs:
		title = item.find('a').text
		company = item.find('span', class_ = 'companyName').text
		try:
			salary = item.find('div', class_ = 'salaryOnly').text
		except:
			salary = '**NO SALARY IMFORMATION**'
		summary = item.find('table', class_ = 'jobCardShelfContainer').text
		
		job = {
			'title': title,
			'company': company,
			'salary': salary,
			'summary': summary
		}
		joblist.append(job)
	return

joblist = []

for i in range(0,40,10):
	c = extract(10)
	transform(c)

df = pd.DataFrame(joblist)
df.to_csv('jobs.csv')
print(df.head())
