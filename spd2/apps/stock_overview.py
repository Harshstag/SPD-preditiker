import streamlit as st
from datetime import date
import requests
from yahoo_fin import stock_info as si


import yfinance as yf
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news

def app():

    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    st.write("<h style=' color: #0078ff; font-size:50px;'>Stock Overview</h>", unsafe_allow_html=True)
    
    selected_stock = st.text_input("Enter ticker","MSFT")
    
    
    

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace = True)
        return data

    data = load_data(selected_stock)

    stock = yf.Ticker(selected_stock)

    stock_name = selected_stock
    longname = stock.info['longName']
    exchange = stock.info['exchange']
    timezone = stock.info['exchangeTimezoneName']
    currency = stock.info['currency']
    current_price = str(round(si.get_live_price(selected_stock),2))
    open_today = str(round(stock.info['open'],2))
    previousclose = str(round(stock.info['previousClose'],2))



    st.markdown(f"<h style='text-align: center; font-size:40px; '>**{longname}**</h>", unsafe_allow_html=True)
    st.markdown(f"<h style='text-align: center; font-size:15px; color: #0078ff; '>**EXCHANGE : {exchange}: {stock_name}  |  {timezone}**</h>", unsafe_allow_html=True)
        

    
    st.markdown("<hr/>", unsafe_allow_html=True)

    kpi01, kpi02, kpi03, kpi04 = st.beta_columns([1,1,1,1])


    with kpi01:

        ##st.markdown(f"<h style='text-align: center; font-size:15px; '>**EXCHANGE : {exchange}: {stock_name}  |  {timezone}**</h>", unsafe_allow_html=True)
        st.image(stock.info['logo_url'],use_column_width='auto')#st.markdown("![Alt Text]("+stock.info['logo_url']+")")


    with kpi02:
       
        st.markdown("**CURRENT PRICE**")
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{current_price} {currency}**</h>", unsafe_allow_html=True)
        
    
    

    with kpi03:
        
        st.markdown("**TODAY OPEN**")
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{open_today} {currency}**</h>", unsafe_allow_html=True)

    with kpi04:    

        st.markdown("**PEVIOUS CLOSE**")
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{previousclose} {currency}**</h>", unsafe_allow_html=True)
        
        
       
    
    

    

    st.markdown("&nbsp ")

    st.markdown("<hr/>",unsafe_allow_html=True)
    st.markdown(f"<h style='text-align: center; font-size:40px; '>Price Summary</h>", unsafe_allow_html=True)

    kpi1, kpi2, kpi3, kpi4 = st.beta_columns(4)
    with kpi1:
        st.markdown("**TODAY'S HIGH**")
        number1 = str(round(stock.info['regularMarketDayHigh'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number1}**</h>", unsafe_allow_html=True)
    
    with kpi2:
        st.markdown("**TODAY'S LOW**")
        number2 = str(round(stock.info['regularMarketDayLow'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number2}**</h>", unsafe_allow_html=True)
    
    with kpi3:
        st.markdown("**52 WEEK HIGH**")
        number3 = str(round(stock.info['fiftyTwoWeekHigh'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number3}**</h>", unsafe_allow_html=True)

    with kpi4:
        st.markdown("**52 WEEK LOW**")
        number4 = str(round(stock.info['fiftyTwoWeekLow'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number4}**</h>", unsafe_allow_html=True)
    
    st.markdown("<hr/>",unsafe_allow_html=True)

    
    st.markdown(f"<h style='text-align: center; font-size:40px; '>Company Essentials</h>", unsafe_allow_html=True)

    kpi5, kpi6, kpi7, kpi8, kpi9, kpi10 = st.beta_columns(6)
    with kpi5:
        st.markdown("**P/E RATIO**")
        number5 = (str(stock.info['pegRatio'])) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number5}**</h>", unsafe_allow_html=True)
    
    with kpi6:
        st.markdown("**P/B RATIO**")
        number6 = str(round(stock.info['priceToBook'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number6}**</h>", unsafe_allow_html=True)
    
    with kpi7:
        st.markdown("**E ON QTR GROTH**")
        number7 = str(round(stock.info['earningsQuarterlyGrowth'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number7}**</h>", unsafe_allow_html=True)

    with kpi8:
        st.markdown("**BOOK VALUE**")
        number8 = str(round(stock.info['bookValue'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number8}**</h>", unsafe_allow_html=True)

    with kpi9:
        st.markdown("**TRAILING  EPS**")
        number9 = str(round(stock.info['trailingEps'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number9}**</h>", unsafe_allow_html=True)

    with kpi10:
        st.markdown("**FORWARD EPS**")
        number10 = (str(stock.info['forwardEps'])) 
        st.markdown(f"<h style='text-align: center; font-size:40px; color:#0078ff; '>**{number10}**</h>", unsafe_allow_html=True)

    st.markdown("<hr/>",unsafe_allow_html=True)


    
    st.markdown(f"<h style='text-align: center; font-size:40px; '>Company Summary</h>", unsafe_allow_html=True)

    kpi11, kpi12, kpi13, kpi14 = st.beta_columns(4)
    with kpi11:
        st.markdown("**MARKET CAP**")
        number11 = str(round(stock.info['marketCap'],2)) 
        st.markdown(f"<h style='text-align: center; font-size:20px; color:#0078ff; '>**{number11}**</h>", unsafe_allow_html=True)

    with kpi12:
        st.markdown("**SECTOR**")
        number12 = stock.info['sector'] 
        st.markdown(f"<h style='text-align: center; font-size:20px; color:#0078ff; '>**{number12}**</h>", unsafe_allow_html=True)

    with kpi13:
        st.markdown("**QUOTE TYPE**")
        number13 = stock.info['quoteType'] 
        st.markdown(f"<h style='text-align: center; font-size:20px; color:#0078ff; '>**{number13}**</h>", unsafe_allow_html=True)
    
    with kpi14:
        st.markdown("**INDUSTRY**")
        number14 = stock.info['industry'] 
        st.markdown(f"<h style='text-align: center; font-size:20px; color:#0078ff; '>**{number14}**</h>", unsafe_allow_html=True)
    

   
    stock_website = stock.info['website']
    

    st.markdown("<hr/>",unsafe_allow_html=True)
    st.markdown(f"<h style='text-align: center; font-size:40px; '>Business summary</h>", unsafe_allow_html=True)
    st.write(stock.info['longBusinessSummary'])
    st.markdown(f"<h style='text-align: center; color: #0078ff; font-size:15px; '>Visit {stock_name} Website {stock_website}</h>", unsafe_allow_html=True)
    st.markdown("<hr/>",unsafe_allow_html=True)

    
    st.markdown(f"<h style='text-align: center; font-size:40px; '>Top Headlines - {stock_name} stock</h>", unsafe_allow_html=True)
    st.markdown("<hr/>",unsafe_allow_html=True)
    retrieve_news(stock.info['shortName'],stock.info['symbol'])

    