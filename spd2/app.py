import streamlit as st
from multiapp import MultiApp
from apps import home_page, prediction, stock_overview, calculator, news_module # importing app modules

app = MultiApp()

st.set_page_config(page_title="PrediTicker", page_icon=None, layout='wide', initial_sidebar_state='collapsed')

app.add_app("Home", home_page.app)
app.add_app("Stock Overview", stock_overview.app)
app.add_app("Prediction", prediction.app)
app.add_app("Brokrage Calculator", calculator.app)
app.add_app("News & More", news_module.app)

app.run()

