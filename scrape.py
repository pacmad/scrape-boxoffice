import requests

url = "https://www.boxofficemojo.com/year/world/2020/"

def url_to_file(url, filename="page_content.html"):
	r = requests.get(url)
	if r.status_code == 200:
		html_text = r.text
		with open(filename, 'w') as f:
			f.write(html_text)
		return html_text
	return ""

url_to_file(url)

