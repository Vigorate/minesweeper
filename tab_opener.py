import bs4, requests

# Read the command line arguments from sys.argv.
# Fetch the search result page with the requests module.
# Find the links to each search result.
# Call the webbrowser.open() function to open the web browser.

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res = requests.get('https://www.reddit.com/', headers=headers)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: {}'.format(exc))
if res.status_code == requests.codes.ok:
    print("Went through")
soup = bs4.BeautifulSoup(res.text, "html.parser")
links = soup.select('a')
for i in links:
    print(i.get('href'))