from bs4 import BeautifulSoup
import requests
from pprint import pprint

res = requests.get("https://www.unite.ai/")
soup = BeautifulSoup(res.text, "html.parser")

news = []


def scrap_header_news():
    header_rows = soup.find_all(
        "div", class_="mvp-widget-feat1-cont left relative")

    # Row 1 => 2 heading news
    header_news_r1 = header_rows[0].find_all(
        "div", class_="mvp-widget-feat1-top-text left relative")

    for news_block in header_news_r1:
        news_url = news_block.parent.parent["href"]
        news_title = news_block.find("h2").get_text()
        news_section = news_block.find(
            "span", class_="mvp-cd-cat left relative").get_text().strip()
        news_date = news_block.find(
            "span", class_="mvp-cd-date left relative").get_text().replace("::before", "").replace('"', "")
        news.append({"url": news_url, "title": news_title,
                    "section": news_section, "date": news_date})

    pprint(news)

    # Row 2 => 4 heading news


scrap_header_news()
