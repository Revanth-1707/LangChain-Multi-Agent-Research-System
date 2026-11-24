from src.tools.tools import web_search, scrape_url
from rich import print


r = web_search.invoke('What is the latest research on using AI for climate change mitigation')
print(r)