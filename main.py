from src.tools.tools import search_web_tavily, scrape_url

#output = search_web_tavily("Lastest news on AI research")
#print(output)


#output = scrape_url("https://ai.google/research")

output = search_web_tavily.invoke("Lastest news on Periodontics research")

print(output)