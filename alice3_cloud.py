from bs4 import BeautifulSoup
import requests
import pandas as pd
google_url = ""

url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRFptTXpJU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

topics = soup.find_all("div", attrs={"class": "W8yrY"})

list_of_news = list()
for topic_index, topic in enumerate(topics):

    mags = topic.find_all("div", class_="vr1PYe")
    titles = topic.find_all("a", class_="gPFEn")
    times = topic.find_all("time", class_="hvbAAd")

    for mag, title, time in zip(mags, titles, times):

        print(mag.text)
        print(title.text)
        print(time["datetime"], "\n")

        list_of_news.append(
            {
                "topic_id": topic_index,
                "media": mag.text,
                "title": title.text,
                "url": "https://news.google.com"+title["href"][1:],
                "time": time["datetime"]
            })

#df = pd.DataFrame(list_of_news)
#df.to_csv("news.csv")

df = pd.DataFrame(list_of_news)

def get_soup_news_df():
    print("ok")
    return df

if __name__ == "__main__":
    df = pd.DataFrame(list_of_news)
    #df.to_csv("news.csv")
    for test_new in list_of_news:
        print(test_new)
