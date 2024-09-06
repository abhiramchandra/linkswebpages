import requests as rq
from bs4 import BeautifulSoup

url = input("Enter Link: ")

# Ensure the URL starts with http:// or https://
if not (url.startswith("http://") or url.startswith("https://")):
    url = "https://" + url

# Fetch the page
data = rq.get(url)

# Parse the page with BeautifulSoup
soup = BeautifulSoup(data.text, "html.parser")

# Find all links and add them to the list
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:  # Make sure href is not None
        links.append(href)

# Save the links to a file
with open("myLinks.txt", 'a') as saved:
    print(links[:10], file=saved)  # Print only the first 10 links
