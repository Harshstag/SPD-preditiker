import streamlit as st
from datetime import date
import requests

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news



def app():

	invalidTicker = False
	START = "2015-01-01"
	TODAY = date.today().strftime("%Y-%m-%d")
	st.write("<h style=' color: #0078ff; font-size:50px;'>Stock Price Prediction</h>", unsafe_allow_html=True)

	selected_stock = st.text_input("Enter ticker", "MSFT")

	n_years = st.slider("Years of prediction:", 1, 4)
	period = n_years * 365

	@st.cache
	def load_data(ticker):
		data = yf.download(ticker, START, TODAY)
		data.reset_index(inplace = True)
		if data.empty:
			st.write("invalid ticker")
			invalidTicker = True
		else:
			return data

	data = load_data(selected_stock)
	stock = yf.Ticker(selected_stock)

	if invalidTicker == True:
		st.write("enter a valid ticker")

	else:
		stock = yf.Ticker(selected_stock)
		data_load_state = st.info("Load data...")
		data = load_data(selected_stock)
		data_load_state.success("Loading data...done!")
		longname = stock.info['longName']
		stock_name = selected_stock
		exchange = stock.info['exchange']
		timezone = stock.info['exchangeTimezoneName']

		
		st.markdown("<hr/>", unsafe_allow_html=True)

		
		col1, col2 = st.beta_columns([1,3])


		with col1:
			st.markdown("&nbsp")
			st.image(stock.info['logo_url'],use_column_width='auto')#st.markdown("![Alt Text]("+stock.info['logo_url']+")")
		
		with col2:
			st.markdown("&nbsp")
			st.markdown(f"<h style='text-align: center; font-size:40px; '>**{longname}**</h>", unsafe_allow_html=True)
			st.markdown(f"<h style='text-align: center; font-size:15px; color: #0078ff; '>**EXCHANGE : {exchange}: {stock_name}  |  {timezone}**</h>", unsafe_allow_html=True)
        	

		#Forecasting
		df_train = data[['Date', 'Close']]
		df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

		m = Prophet()
		m.fit(df_train)
		future = m.make_future_dataframe(periods=period)
		forecast = m.predict(future)

		st.markdown("<hr/>", unsafe_allow_html=True)
		st.markdown("&nbsp ")
		st.write("<h style=' color: #0078ff; font-size:50px;'>Forecast Data</h>", unsafe_allow_html=True)
		fig1 = plot_plotly(m, forecast)
		st.plotly_chart(fig1)

		st.markdown("<hr/>", unsafe_allow_html=True)
		st.markdown("&nbsp ")
		st.write("<h style=' color: #0078ff; font-size:50px;'>Raw Data</h>", unsafe_allow_html=True)
		st.write(data.tail())

		st.markdown("<hr/>", unsafe_allow_html=True)
		st.markdown("&nbsp ")
		st.write("<h style=' color: #0078ff; font-size:50px;'>Raw Forecast Data</h>", unsafe_allow_html=True)
		st.write(forecast.tail())

		st.markdown("<hr/>", unsafe_allow_html=True)
		st.markdown("&nbsp ")
		st.write("<h style=' color: #0078ff; font-size:50px;'>Forecast Components</h>", unsafe_allow_html=True)
		fig2 = m.plot_components(forecast)
		st.write(fig2)	
		st.markdown("<hr/>", unsafe_allow_html=True)



