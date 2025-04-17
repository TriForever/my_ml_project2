# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
import streamlit as st
import numpy as np 
import joblib
import base64

def get_image_html(page_name, file_name):
    with open(file_name, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<a href="{page_name}"><img src="data:image/png;base64,{data_url}" style="width:300px"></a>'

data_url = get_image_html("分類", "./panguin.png")
data_url_2 = get_image_html("迴歸", "./taxi.png")
data_url_3 = get_image_html("鳶尾花", "./iris.png")
data_url_4 = get_image_html("GoogleNews", "./google.png")
data_url_5 = get_image_html("英文辨識", "./abc.png")
data_url_6 = get_image_html("shippredict", "./ship.png")
st.set_page_config(
    page_title="我的學習歷程",
    page_icon="👋",
)

st.title('Machine Learning 學習歷程')   

col1, col2 ,col3= st.columns(3)
with col1:
    # url must be external url instead of local file
    # st.markdown(f"### [![分類]({url})](分類)")
    st.markdown('### [(分類)企鵝品種辨識](分類)')
    st.markdown('''
    ##### 特徵(X):
        - 島嶼
        - 嘴巴長度
        - 嘴巴寬度
        - 翅膀長度
        - 體重
        - 性別
    ##### 預測類別(Class):
        - Adelie
        - Chinstrap
        - Gentoo
        ''')
    # st.image('iris.png')
    st.markdown(data_url, unsafe_allow_html=True)
    
    
    
    
    
    
    st.markdown('### [Google台灣新聞摘要](GoogleNews)')
    st.markdown(data_url_4, unsafe_allow_html=True)
with col2:
    st.markdown('### [(迴歸)計程車小費預測](迴歸)')
    st.markdown('''
    ##### 特徵(X):
        - 車費
        - 性別
        - 吸菸
        - 星期
        - 時間
        - 同行人數
    ##### 目標：預測小費金額
        ''')
    # st.image('taxi.png')
    st.markdown(data_url_2, unsafe_allow_html=True)
    
    
    
    
    
    
    st.markdown('### [cnn英文辨識](英文辨識)')
    st.markdown(data_url_5, unsafe_allow_html=True)
with col3:
    # url must be external url instead of local file
    # st.markdown(f"### [![分類]({url})](分類)")
    st.markdown('### [(鳶尾花)鳶尾花品種辨識](鳶尾花)')
    st.markdown('''
    ##### 特徵(X):
        - 花萼長度
        - 花萼寬度
        - 花瓣長度
        - 花瓣寬度
    ##### 預測類別(Class):
        - setosa
        - versicolor
        - virginica
        ''')
    #st.image('iris.png')
    st.markdown(data_url_3, unsafe_allow_html=True)
    
    
    st.markdown('### [TitanicShip預測](shippredict)')
    st.markdown('''
    ##### 特徵(X):
        - 出發的星球
        - 冷凍睡眠
        - 目的地
        - 年齡
        - VIP
        - RoomService金額
        - FoodCourt金額
        - ShoppingMall金額
        - Spa金額
        - VRDeck金額
        - Deck
        - Cabin_num
        - Side
    ##### 目標：預測是否被傳送到其他維度空間
        ''')
    #st.image('ship.png')
    st.markdown(data_url_6, unsafe_allow_html=True)

