# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 01:00:37 2020
@author: snikkho
To read and analyze Robinhood portfolio
"""

#importing the libraries 
import os
import pandas as pd
import robin_stocks as rs


#logging in
rs.login(username='saberkhoshdel@gmail.com',
         password='',
         expiresIn=3600,
         by_sms=True)


# Get all the positions/holdings
#allPositions = rs.account.get_all_positions()
dictPositions = rs.account.build_holdings()
portfo_df = pd.DataFrame(dictPositions)
#position_df.to_csv('new_dataframe.csv')

#Converting row values to numbers
portfo_df.loc['percent_change'] = pd.to_numeric(portfo_df.loc['percent_change'], errors='coerce')
portfo_df.loc['equity'] = pd.to_numeric(portfo_df.loc['equity'], errors='coerce')
portfo_df.loc['equity_change'] = pd.to_numeric(portfo_df.loc['equity_change'], errors='coerce')

#Various sorting
percentChange_df= portfo_df.sort_values(by = ['percent_change'], axis= 1, ascending= False)
equity_df= portfo_df.sort_values(by = ['equity'], axis= 1, ascending= False)
equityChange_df= portfo_df.sort_values(by = ['equity_change'], axis= 1, ascending= False)

#Write to CSV
percentChange_df.to_csv('percentChange.csv')
equity_df.to_csv('equity.csv')
equityChange_df.to_csv('equityChange.csv')

# log out of Robinhood API
rs.logout()

print('Complete!')