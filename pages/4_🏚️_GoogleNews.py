import streamlit as st
from alice3_cloud import get_soup_news_df
# 載入模型與標準化轉換模型


news_df = get_soup_news_df()
news_df = news_df.drop(['topic_id','url'], axis=1)
news_df.columns = list(['媒體','標題','時間'])
st.title('Google台灣新聞摘要')
st.table(news_df)
