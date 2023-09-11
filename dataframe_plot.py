import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price
import datetime
from selenium import webdriver
from time import sleep
import matplotlib.pyplot as plt
import seaborn as sns



def main():
    file = r"C:\Users\tinhox\OneDrive - Intel Corporation\Desktop\tracking_price\prices.csv"
    df_origin = pd.read_csv(file, sep = ",", encoding='latin-1')
    df = df_origin[df_origin["name"] == 'sunspel']

    sns.lineplot( x = "date",
             y = "price",
             hue = "product",
             data = df);    
    plt.show()

if __name__=="__main__":
    main()