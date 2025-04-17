# https://docs.streamlit.io/en/stable/api.html#streamlit.slider
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# load model
@st.cache_data
def load_model():
    clf = joblib.load('ship_model.joblib')
    scaler = joblib.load('ship_scaler.joblib')
    return clf, scaler
    
     

dict1 = {'Europa':0, 'Earth':1,'Mars':2}
dict2 = {'否':0, '是':1}
dict3 = {'TRAPPIST-1e':0, 'PSO J318.5-22':1,'55 Cancri e':2}
dict4 = {'否':0, '是':1}
dict5 = {'B':0, 'F':1,'A':2, 'G':3,'E':4, 'D':5,'C':6, 'T':7}
dict6 = {'P':0, 'S':1}

def convert_planet(embark1):
    return dict1[embark1]

def convert_Cryo(embark1):
    return dict2[embark1]

def convert_destination(embark1):
    return dict3[embark1]

def convert_VIP(embark1):
    return dict4[embark1]

def convert_Deck(embark1):
    return dict5[embark1]

def convert_Side(embark1):
    return dict6[embark1]

        
clf, scaler = load_model()    

#HomePlanet	CryoSleep	Destination	Age	VIP	RoomService	FoodCourt	ShoppingMall	Spa	VRDeck	Deck	Cabin_num	Side
# 畫面設計
st.markdown('# 太空船傳送預測系統')
planet_series = pd.Series(['Europa', 'Earth','Mars'])
Cryo_series = pd.Series(['否', '是'])
destination_series = pd.Series(['TRAPPIST-1e', 'PSO J318.5-22', '55 Cancri e'])
VIP_series = pd.Series(['否', '是'])
Deck_series = pd.Series(['B', 'F', 'A', 'G', 'E', 'D', 'C', 'T'])
Side_series = pd.Series(['P', 'S'])

# '出發的星球:', HomePlanet
HomePlanet = st.sidebar.selectbox('出發的星球:', planet_series)

# '冷凍睡眠:', CryoSleep
CryoSleep = st.sidebar.selectbox('冷凍睡眠',Cryo_series)

# '目的地:', Destination
Destination = st.sidebar.selectbox('目的地', destination_series)

# '年齡:', Age
Age = st.sidebar.slider('年齡', 0, 80, 0)

# 'VIP:', VIP
VIP = st.sidebar.selectbox('VIP',VIP_series)

# 'RoomService金額:', RoomService
RoomService = st.sidebar.slider('RoomService金額', 0, 30000, 0)

# 'FoodCourt金額:', FoodCourt
FoodCourt = st.sidebar.slider('FoodCourt金額', 0, 30000, 0)

# 'ShoppingMall金額:', ShoppingMall
ShoppingMall = st.sidebar.slider('ShoppingMall金額', 0, 30000, 0)

# 'Spa金額:', Spa
Spa = st.sidebar.slider('Spa金額', 0, 30000, 0)

# 'VRDeck金額:', VRDeck
VRDeck = st.sidebar.slider('VRDeck金額', 0, 30000, 0)

# 'Deck:', Deck
Deck = st.sidebar.selectbox('Deck',Deck_series)

# 'Cabin_num:', Cabin_num
Cabin_num = st.sidebar.slider('Cabin_num', 0, 2000, 0)

# 'Side:', Side
Side = st.sidebar.selectbox('Side:', Side_series)

st.image('./ship.png')

if st.sidebar.button('預測'):
    # predict
    X = []
   
    X.append([convert_planet(HomePlanet), convert_Cryo(CryoSleep), convert_destination(Destination), Age, convert_VIP(VIP), RoomService, FoodCourt,ShoppingMall,Spa, VRDeck,convert_Deck(Deck),Cabin_num,convert_Side(Side)])
    X=scaler.transform(np.array(X))
    
    if clf.predict(X) == 1:
        st.markdown(f'### ==> **傳送, 傳送機率={clf.predict_proba(X)[0][1]:.2%}**')
    else:
        st.markdown(f'### ==> **未傳送, 傳送機率={clf.predict_proba(X)[0][1]:.2%}**')
