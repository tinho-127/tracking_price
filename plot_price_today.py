import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price
import datetime
from datetime import timedelta
from selenium import webdriver
from time import sleep
import matplotlib.pyplot as plt
import seaborn as sns

def main():    
    pd.set_option('display.max_rows', 1000)
    
    #fig, ax = plt.subplots(figsize=(19,10))
    file_name = r"prices.csv"
    today = datetime.date.today()
    #today = today - timedelta(days = 1)
    yesterday = today - timedelta(days = 1)
    
    df = pd.read_csv(file_name, sep=",")
    
    df1 = df[(df['date'] == str(yesterday))]
    df1 = df1.drop_duplicates()
    df1['name'] = df1['name'].astype(str) +" "+ df1['product'].astype(str) +" "+ df1['color'].astype(str)

    df2 = df[(df['date'] == str(today))] 
    df2 = df2.drop_duplicates()
    df2['name'] = df2['name'].astype(str) +" "+ df2['product'].astype(str) +" "+ df2['color'].astype(str)
    
    df_final = pd.merge(df1,df2, on='name',how='left')
    df_final = df_final[ (df_final['price_x'] > 0) & (df_final['price_y'] > 0 )]
    
    plt.figure(figsize=(19,10))
    sns.lineplot(x = 'name',
            y = 'price_x',
            data = df_final,
            marker='o',
            label=yesterday)
            
    sns.barplot(x = 'name',
            y = 'price_y',
            data = df_final)

    plt.xticks(rotation=90, horizontalalignment="center", fontsize = 5)
    plt.show()

if __name__=="__main__":
    main()
    