import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import date
import requests

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from .fetch_news import retrieve_news



def app():
    

    st.write("<h style=' color: #0078ff; font-size:50px;'>Brokrage Calculator</h>", unsafe_allow_html=True)
    st.subheader("Use the brokerage calculator to calculate exactly how much you will pay in brokerage and your breakeven")
    st.markdown("<hr/>", unsafe_allow_html=True)
    

    st.subheader("Select Broker")
    option = st.selectbox("  ",('Select','Online Broker','Offline Broker')) 


  ##   Calculator Home Page Algo  Select
    
    if option == 'Select':
        st.markdown("<hr/>", unsafe_allow_html=True)
        
        st.write("<h style=' color: #0078ff; font-size:50px;'>All About Brokrage Calculation</h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>It is an online tool that brokers and other investment platforms provide at the disposal of traders to facilitate brokerage calculation in advance of carrying out a trade. However, a brokerage calculator is not merely limited to calculating brokerage. It also calculates stamp duty charges, transaction fees, SEBI turnover fee, GST, and Securities Transaction Tax (STT). </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>Therefore, a brokerage charges calculator simplifies the process of calculating the cost of trade significantly. An individual would need to input the following information in an online brokerage calculator to compute their cost of trading –  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>Such a calculator provides accurate information about such costs instantaneously, thus facilitating speedy and timely trading. Therefore, it is paramount for traders who rely on timing extensively to carry out their trades, like intraday traders. They can use an intraday brokerage calculator to ease the process of cost analysis before buying and selling securities. </h>", unsafe_allow_html=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.write("<h style=' color: #0078ff; font-size:50px;'>How It Works</h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>As mentioned earlier, brokerage charges are the fees that brokers collect from traders to facilitate trade. Therefore, investors need to pay brokerage fees both when selling securities and when buying them. However, specific brokers might consider excluding one event from any charges. Nevertheless, most brokers levy a certain percentage of the trade value as their brokerage fees. Depending on the scale of trade value, such percentages might vary. Regardless, the formula for calculation of brokerage in share market is as follows –  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>Brokerage = Number of shares sold/bought x Price of one unit of stock x brokerage percentageShare brokerage calculators employ this formula for both intraday trading and delivery trading brokerage calculations. Example: Ria decides to purchase 20 shares of Hindustan Unilever Limited at Rs.2000 each, and within 10 days, she sells those off at Rs.2100. She does so via a Broker Z who charges 0.5% as brokerage fees. In this example, Ria’s total trade value stands to be: Rs. [(20 x 2000) + (20 x 2100)] Or, Rs. (40,000 + 42000) = Rs.82,000Since Broker Z charges 0.5% as brokerage, the total fee she pays to the broker is:Rs. (82000 x 0.5%) = Rs.410Therefore, Ria would pay Rs.410 as a brokerage for carrying out transactions worth Rs.82000. However, if she carried out a transaction on which brokerage by standard means is too low, then a broker would charge the minimum amount applicable, which is usually Rs.20 – Rs.30. Nevertheless, to simplify this tedious process of calculating brokerage, individuals can use a stock brokerage calculator.  </h>", unsafe_allow_html=True)
        st.markdown("<hr/>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>  </h>", unsafe_allow_html=True)
        st.write("<h style=' font-size:15px;'>  </h>", unsafe_allow_html=True)



  ##   Online Broker Algo

    if option == 'Online Broker':
        st.subheader("Select Online Broker")

        option = st.selectbox("  ",('Select','Zerodha','Upstox','Groww'))
        
                
        if option == 'Select':
             st.subheader("Select Online Broker algo")

            
        
        if option == 'Zerodha':
            
            st.markdown("<hr/>", unsafe_allow_html=True)
            st.write("<h style=' color: #0078ff; font-size:30px;'>Zerodha Brokerage calculator. List of all charges and taxes</h>", unsafe_allow_html=True)                    
               ### top row 
            st.markdown("<hr/>", unsafe_allow_html=True)           #########################################################

            first_kpi, second_kpi, third_kpi, fourth_kpi  = st.beta_columns(4)


            with first_kpi:   ##   Intraday equity
                
                st.info(f"""**Intraday equity**""")
                st.markdown("<hr/>", unsafe_allow_html=True)
                buy1 = st.number_input("BUY", min_value=0, max_value=10000, value=1000) 
                sell1 = st.number_input("SELL", min_value=0, max_value=10000, value=1100)
                que1 = st.number_input("QUANTITY", min_value=0, max_value=10000, value=400)


                market = st.radio(" ",('NSE', 'BSE'))

                turnover = (round((buy1*que1)+(sell1*que1),2))
                brokerage = (round((0.03/100)*(buy1*que1),2))
                stt_total = (round((0.025/100)*(sell1*que1),2))
                txn = (round(0.00345/100*((buy1*que1)+(sell1*que1)),2))
                gst = (round(18/100*(brokerage+txn),2))
                sebi = (round(0.000001*((buy1*que1)+(sell1*que1)),2))
                stamp = (round(0.00003*(buy1*que1),2))
                direct_pl = (round((sell1*que1)-(buy1*que1),2))
                direct_disc = (round(brokerage-20,2))

                total = ( (brokerage) + (stt_total) + (txn) + (gst) + (sebi) + (stamp) )
                total2 = ( 40 + (stt_total) + (txn) + (gst)  + (sebi) + (stamp) )

                net_pl = ((direct_pl) - (total))
                net_pl2 = ((direct_pl) - (total2))


                st.markdown(f"""Turnover : {turnover}""")

                if brokerage < 20:
                        st.markdown(f"""Brokerage : {brokerage}""")
                else:
                        st.markdown(f"""Brokerage : 40""")

                st.markdown(f"""STT total : {stt_total}""")
                st.markdown(f"""Exchange txn charge : {txn}""")
                st.markdown(f"""Clearing charges : 0""")

                if brokerage < 20:
                    gst = (18/100*(brokerage+txn))
                    st.markdown(f"""GST : {gst}""")
                else:
                    gst = (0.18 * ( 20 + txn))
                    st.markdown(f"""GST : {gst}""")

                   
                    st.markdown(f"""SEBI charges : {sebi}""")
                    st.markdown(f"""Stamp duty : {stamp}""")
                    st.markdown(f"""DP Charges : 00 """)
                    st.markdown(f"""**Direct P&L : {direct_pl}**""")

                if brokerage < 20:
                    st.markdown(f"""**Direct Discount : 00**""")
                else:
                    st.markdown(f"""**Direct Discount : {direct_disc}**""")

                if brokerage < 20:
                    st.markdown(f"""**Total tax and charges {total}**""")
                else:
                    st.markdown(f"""**Total tax and charges {total2}**""")

                    st.markdown("")
                if brokerage < 20:
                    st.info(f"""**NET P&L : {net_pl}**""")
                else:
                    st.info(f"""**Net P&L : {net_pl2}**""")
                
            st.markdown(f"""<hr/>""", unsafe_allow_html=True)         

            with second_kpi:  ##  dilevry equity 
                st.info(f"""**Dilevry equity**""")
                st.markdown("<hr/>", unsafe_allow_html=True)
                buy2 = st.number_input("BUY ", min_value=0, max_value=10000, value=1000) 
                sell2 = st.number_input("SELL ", min_value=0, max_value=10000, value=1100)
                que2 = st.number_input("QUANTITY ", min_value=0, max_value=10000, value=400)

                turnover2 = (round((buy2*que2)+(sell2*que2),2))
                brokerage2 = (0)
                stt_total2 = (round((0.1/100)*(turnover2),2))
                txn2 = (round(0.00345/100*((buy2*que2)+(sell2*que2)),2))
                gst2 = (round(18/100*(brokerage2+txn2),2))
                sebi2 = (round(0.000001*((buy2*que2)+(sell2*que2)),2))
                stamp2 = (round(0.00015*(buy2*que2),2))
                direct_pl2 = (round((sell2*que2)-(buy2*que2),2))

                total222 = (round( (brokerage2) + (stt_total2) + (txn2) + (gst2) + (sebi2) + (stamp2) + 15.93 ,2))
                net_pl2 = (round((direct_pl2) - (total222),2))

                market2 = st.radio("  ",('NSE', 'BSE'))

                st.markdown(f"""Turnover : {turnover2}""")
                st.markdown(f"""Brokerage : {brokerage2}""")
                st.markdown(f"""STT total : {stt_total2}""")
                st.markdown(f"""Exchange txn charge : {txn2}""")
                st.markdown(f"""Clearing charges : 00""")
                st.markdown(f"""GST : {gst2}""")
                st.markdown(f"""SEBI charges : {sebi2}""")
                st.markdown(f"""Stamp duty : {stamp2}""")
                st.markdown(f"""DP Charges : 15.93 """)
                st.markdown(f"""**Direct P&L : {direct_pl2}**""")
                st.markdown(f"""**Direct Discount : 00**""")
                st.markdown(f"""**Total tax and charges : {total222}**""")
                st.markdown("")
                st.info(f"""**Net P&L : {net_pl2}**""")
                
                



             

            with third_kpi:       ##  F&O - Futures
                st.info(f"""**F&O - Futures**""")
                st.markdown("<hr/>", unsafe_allow_html=True)
                buy3 = st.number_input("BUY  ", min_value=0, max_value=10000, value=1000) 
                sell3 = st.number_input("SELL  ", min_value=0, max_value=10000, value=1100)
                que3 = st.number_input("QUANTITY  ", min_value=0, max_value=10000, value=400)

                market3 = st.radio("     ",('NSE', 'BSE'))

                turnover3 = (round(buy3*que3)+(sell3*que3),2)
                brokerage3 = round((0.03/100)*(buy3*que3),2)
                stt_total3 = (round((0.01/100)*(sell3*que3),2))
                txn3 = (round(0.002/100*((buy3*que3)+(sell3*que3)),2))
                gst3 = (round(18/100*(brokerage3+txn3),2))
                sebi3 = (round(0.000001*((buy3*que3)+(sell3*que3)),2))
                stamp3 = (round(0.00002*(buy3*que3),2))
                direct_pl3 = (round((sell3*que3)-(buy3*que3),2))
                direct_disc3 = (brokerage3-20)

                total333 = (round((brokerage3)+(stt_total3)+(txn3)+(gst3)+(sebi3)+(stamp3),2))
                total2333 = (round(40+(stt_total3)+(txn3)+(gst3)+(sebi3)+(stamp3),2))

                net_pl333 = round((direct_pl3) - (total333),2)
                net_pl2333 = (round((direct_pl3) - (total2333),2))


                st.markdown(f"""Turnover : {turnover3}""")

                if brokerage < 20:
                        st.markdown(f"""Brokerage : {brokerage3}""")
                else:
                        st.markdown(f"""Brokerage : 40""")

                st.markdown(f"""STT total : {stt_total3}""")
                st.markdown(f"""Exchange txn charge : {txn3}""")
                st.markdown(f"""Clearing charges : 0""")

                if brokerage < 20:
                    gst3 = (round(18/100*(brokerage3+txn3),2))
                    st.markdown(f"""GST : {gst3}""")
                else:
                    gst3 = (round(0.18 * ( 40 + (txn3)),2))
                    st.markdown(f"""GST : {gst3}""")

                   
                    st.markdown(f"""SEBI charges : {sebi3}""")
                    st.markdown(f"""Stamp duty : {stamp3}""")
                    st.markdown(f"""DP Charges : 00 """)
                    st.markdown(f"""**Direct P&L : {direct_pl3}**""")

                if brokerage < 20:
                    st.markdown(f"""**Direct Discount : 00**""")
                else:
                    st.markdown(f"""**Direct Discount : {direct_disc3}**""")

                if brokerage < 20:
                    st.markdown(f"""**Total tax and charges {total333}**""")
                else:
                    st.markdown(f"""**Total tax and charges {total2333}**""")

                    st.markdown("")
                if brokerage < 20:
                    st.info(f"""**NET P&L : {net_pl333}**""")
                else:
                    st.info(f"""**Net P&L : {net_pl2333}**""")


                
                    
                
            with fourth_kpi:    ##  f&o options
                st.info("**F&O - Options**")
                st.markdown("<hr/>", unsafe_allow_html=True)
                buy4 = st.number_input("BUY   ", min_value=0, max_value=10000, value=1000) 
                sell4 = st.number_input("SELL   ", min_value=0, max_value=10000, value=1100)
                que4 = st.number_input("QUANTITY   ", min_value=0, max_value=10000, value=400)

                market4 = st.radio("              ",('NSE', 'BSE'))

                turnover4 = (round((buy4*que4)+(sell4*que4),2))
                brokerage4 = (40)
                stt_total4 = (round((0.05/100)*(sell4*que4),2))
                txn4 = (round(0.053/100*((buy4*que4)+(sell4*que4)),2))
                gst4 = (round(18/100*(brokerage4+txn4),2))
                sebi4 = (round(0.000001*((buy4*que4)+(sell4*que4)),2))
                stamp4 = (round(0.00003*(buy4*que4),2))
                direct_pl4 = (round((sell4*que4)-(buy4*que4),2))

                total444 = (round((brokerage4) + (stt_total4) + (txn4) + (gst4) + (sebi4) + (stamp4),2))
                net_pl444 = (round((direct_pl4) - (total444),2))

                st.markdown(f"""Turnover : {turnover4}""")
                st.markdown(f"""Brokerage : {brokerage4}""")
                st.markdown(f"""STT total : {stt_total4}""")
                st.markdown(f"""Exchange txn charge : {txn4}""")
                st.markdown(f"""Clearing charges : 00""")
                st.markdown(f"""GST : {gst4}""")
                st.markdown(f"""SEBI charges : {sebi4}""")
                st.markdown(f"""Stamp duty : {stamp4}""")
                st.markdown(f"""DP Charges : 00 """)
                st.markdown(f"""**Direct P&L : {direct_pl4}**""")
                st.markdown(f"""**Direct Discount : 00**""")
                st.markdown(f"""**Total tax and charges : {total444}**""")
                st.markdown(f""" """)
                st.info(f"""**Net P&L : {net_pl444}**""")
                   