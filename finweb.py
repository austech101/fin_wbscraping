
import csv
from bs4 import BeautifulSoup
import requests

site_url = "https://www.google.com/finance/?hl=en"

page = requests.get(site_url)

if page.status_code == 200:
    print("Page fetched successfully")
else:
    print(f"Failed to fetch. Status code: {page.status_code}")

# Parsing the webpage
bsoup = BeautifulSoup(page.content, "lxml")

#list to store financial data
financial_data = [] 
# Getting financial news heading
heading = bsoup.find("div", class_="K7jPKe")
if heading:
    financial_heading = heading.text.strip()
    print("Heading:", heading.text.strip())
else:
    financial_heading = "N/A"

# Getting top financial news stories
top_stories = bsoup.find_all("div", class_="Yfwt5")
financial_stories = []
if top_stories:
    print("\nTop Financial Stories:")
    for story in top_stories:
        financial_stories.append(story.text.strip())
else:
    financial_stories.append("N/A")

# Getting stock prices
stocks = bsoup.find_all("div", class_="ZvmM7")
stock_prices = []
if stocks:
    print("\nStock Prices:")
    for stock in stocks:
        stock_prices.append(stock.text.strip())
else:
    stock_prices.append("N/A")

# Getting financial stock percentage changes
stock_changes = bsoup.find_all("div", class_="JwB6zf")
percentage_changes = []
if stock_changes:
    for change in stock_changes:
        percentage_changes.append(change.text.strip())
else:
    percentage_changes.append("N/A")

# Getting stocks with the highest trading volume (most active)
most_active_stocks = bsoup.find_all("div", class_="YMlKec")
most_active = []
if most_active_stocks:
    for active_stock in most_active_stocks:
        most_active.append(active_stock.text.strip())
else:
    most_active.append("N/A")

for i in range(max(len(financial_stories), len(stock_prices), len(percentage_changes), len(most_active))):
    row = [
        financial_heading,
        financial_stories[i] if i < len(financial_stories) else "N/A",
        stock_prices[i] if i < len(stock_prices) else "N/A",
        percentage_changes[i] if i < len(percentage_changes) else "N/A",
        most_active[i] if i < len(most_active) else "N/A"
    ]
    financial_data.append(row)


"CSV headers"
csv_headers= ["Financial news", "Top story", "stock price","percentage change","Most active stocks"]

csv_file = "Financial_data.csv"
with open(csv_file, "w", encoding="utf-8") as fin_file:
    writer = csv.writer(fin_file)
    writer.writerow(csv_headers)
    writer.writerows(financial_data)

print(f"Data has been written to {csv_file}")

