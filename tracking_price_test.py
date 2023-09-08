import smtplib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from price_parser import Price
import datetime

def main():
    PRODUCT_URL_CSV = r"products_test.csv"
    SAVE_TO_CSV = True
    #SAVE_TO_CSV = False
    PRICES_CSV = "prices_test.csv"
    df = get_urls(PRODUCT_URL_CSV)
    df_updated = process_products(df)
    if SAVE_TO_CSV:
        df_save(PRICES_CSV, df_updated)   
    #SEND_MAIL = True
    #if SEND_MAIL:
    #    send_mail(df_updated)


def df_save(save_csv,df):
    df_temp = df[['name','product','color', 'price','date', 'url']]
    df_temp.to_csv(save_csv, mode='a', index=False, header=False)

def get_urls(csv_file):
    df = pd.read_csv(csv_file,sep=r';',)
    return df
    
def get_response(url):
    response = requests.get(url)
    return response.text
    
def get_price(html,df):
    x = df['name']
    soup = BeautifulSoup(html, "lxml")
    if x == 'sunspel':
        el = soup.select_one(".prd-Detail_Price")
    #elif x == 'MackWeldon':
        #el = soup.select_one(".productInfo__priceBox")
    price = Price.fromstring(el.text)
    return price.amount_float

def process_products(df):
    updated_products = []

    for product in df.to_dict("records"):
        html = get_response(product["url"])    
        product["price"] = get_price(html,product)
        product["alert"] = product["price"] < product["alert_price"]
        product["date"] = datetime.date.today()
        updated_products.append(product)
    return pd.DataFrame(updated_products)
    
    
if __name__=="__main__":
    main()
    