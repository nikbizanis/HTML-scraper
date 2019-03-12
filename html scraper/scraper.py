
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import sys




def is_html_response(resp):
# Returns true if the response seems to be an HTML document

	content_type = resp.headers['Content-Type'].lower()
	if content_type.find('html'):
		return True
	else:
		return False



def simple_get(url):
# Gets the URL given as an argument via HTTP GET and if the response is
# an HTML document, it returns its text content

	with closing(get(url, stream=True)) as resp:
		if is_html_response(resp):
			return resp.content
		else:
			return None


page_content = simple_get(sys.argv[1])

html_doc = BeautifulSoup(page_content, "html.parser")

for element in html_doc.select("img"):
	print(element["src"])

print("\n\n")

for element in html_doc.select("a"):
	print(element["href"])
