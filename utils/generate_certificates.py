import requests, bs4
from datetime import date

today = date.today()
today_field = today.strftime('%d %b %Y')

def generate(names):
	for name in names:
		request = requests.get('https://certificatemagic.com/personalize.php?design=1')
		request.raise_for_status()

		soup = bs4.BeautifulSoup(request.text)
		fields = soup.select('div.formFields input')

		# update data
		fields[0] =  'Certificate of Competition'
		fields[1] = 'THIS IS TO CERTIFY THAT'
		fields[2] = name
		fields[3] = 'has completed Python Programming'
		fields[4] = today_field
