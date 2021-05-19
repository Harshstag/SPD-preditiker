import streamlit as st
from .fetch_news import retrieve_business_news
import requests
import pandas as pd
from datetime import date
import yfinance as yf
from yahoo_fin import stock_info as si
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news
from PIL import Image

def app():						
	
	kpit1, kpit2 = st.beta_columns([1,6])
	with kpit1:

		image = Image.open('logo.png')
		st.image(image, caption=' ', width=110)

	with kpit2:
		st.write("<h style=' color: #0078ff; font-size:60px;'>**PrediTicker**</h>", unsafe_allow_html=True)


	##st.write("<h style=' color: #0078ff; font-size:60px;'>PrediTickerr</h>", unsafe_allow_html=True)
	st.markdown("<hr/>", unsafe_allow_html=True)
	st.write("&nbsp")

	stock = yf.Ticker("^IXIC")
	#st.write(stock.info)
	def load_data(component):
		component_data=si.get_quote_data(component)
		return component_data

	NASDAQ_data = load_data("^IXIC")
	NIFTY50_data = load_data("^NSEI")
	BSESENSEX_data = load_data("^BSESN")


	
	

	#st.write(NASDAQ_data)

	def write_data(component):

		

		shortname = (str(component['shortName']))
		marketstate = component['marketState']
		regularmarketprice = str(round(component['regularMarketPrice'],2))
		Changepercent = str(round(component['regularMarketChangePercent'],2))
		regularMarketChange = str(round(component['regularMarketChange'],2))

		if component['regularMarketChange'] > 0:
			

			

			st.markdown(f"<h style='text-align: center; font-size:20px; color: green; '>**{shortname}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:20px; color: green; '>**CURRENT PRICE : {regularmarketprice}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:15px; color: green; '>**{marketstate} : HIGH : {regularMarketChange} / {Changepercent}%**</h>", unsafe_allow_html=True)	
				
		else:
			st.markdown(f"<h style='text-align: center; font-size:20px; color: red; '>**{shortname}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:20px; color: red; '>**CURRENT PRICE : {regularmarketprice}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:15px; color: red; '>**{marketstate} : LOW : {regularMarketChange} / {Changepercent}%**</h>", unsafe_allow_html=True)

	
	
	
	
	
	
	
	col1, col2, col3 = st.beta_columns(3)


	with col1:
		 
		write_data(NASDAQ_data)
	with col2:
		write_data(NIFTY50_data)
	with col3:
		write_data(BSESENSEX_data)






	image2 = Image.open('homebg.png')
	st.image(image2, caption=' ')



	gainer_col, loser_col, active_col = st.beta_columns([1,1,1])
	st.markdown("<hr/>", unsafe_allow_html=True)

	gainers=si.get_day_gainers().head(10)
	gainers.drop(gainers.columns[[6,8]], axis=1, inplace=True)
	with gainer_col:
		st.write("<h style=' color: green; font-size:40px;'>**Top Gainers**</h>", unsafe_allow_html=True)
		st.dataframe(gainers)

	losers=si.get_day_losers().head(10)
	with loser_col:
		st.write("<h style=' color: red; font-size:40px;'>**Top Losers**</h>", unsafe_allow_html=True)
		st.dataframe(losers)

	active=si.get_day_most_active().head(10)
	with active_col:
		st.write("<h style=' color: #DACB4A; font-size:40px;'>**Top Active**</h>", unsafe_allow_html=True)
		st.dataframe(active)

	st.markdown("&nbsp ")
	st.write("<h style=' color: #0078ff; font-size:50px;'>Trending News</h>", unsafe_allow_html=True)
	st.markdown("<hr/>", unsafe_allow_html=True)
	retrieve_business_news()
	st.markdown("<hr/>", unsafe_allow_html=True)