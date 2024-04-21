import streamlit as st
import pandas as pd
from ipynb.fs.full.scraping import player_input
from ipynb.fs.full.Forecast import result

st.set_page_config('Score Predictor')

st.title('Performance Estimator')
st.header("Predict your player's score of today's match")


no_of_players = st.text_input('Enter the No of Players')

player_list = []

for i in range(int('0'+no_of_players)):
    player_list.append(st.text_input('Enter Player '+str(i+1)+':'))
s=0
if st.button('Submit'):
    s=player_input(player_list)
if s==2:
    result()
    res1 = pd.read_csv('bat_result.csv')
    res1.columns=['Player','runs','balls']
    res2 = pd.read_csv('bowl_result.csv')
    res2.columns=['Player','ovrs','consumed_runs','wkts']
    st.write('Forecasting:')
    st.write('Batting:')
    st.dataframe(res1)
    st.write('Bowling:')
    st.dataframe(res2)
    st.write('Note: The Above Predictions are estimated only by the considering thier form of a Player')

    # final_res = pd.concat([res1.iloc[:,1:],res2.iloc[:,1:]],axis=1)
    # final_res.index = player_list
    # st.write(final_res)