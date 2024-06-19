import requests
import yfinance as yf
from bs4 import BeautifulSoup
from collections import namedtuple

from dao.dao import create
from model.mod_classes import Stock, Stocks

symboles = ['MSFT', 'AAPL', 'AMZN', 'META', 'AVGO', 'GOOGL', 'GOOG', 'COST', 'TSLA', 'NFLX']
compagnies = ['Microsoft Corp', 'Apple Inc', 'Amazon.Com Inc', 'Meta Platforms Inc', 'Broadcom Inc', 'Alphabet Inc',
              'Alphabet Inc', 'Costco Wholesale Corp', 'Tesla Inc', 'Netflix Inc']


def job():
    # Remplacez 'AAPL' par le symbole boursier de l'action que vous souhaitez récupérer
    ticker_symbol = 'AAPL'

    # Récupération des données historiques
    ticker_data = yf.Ticker(ticker_symbol)

    # Récupération des données historiques sur une période spécifique (par exemple, 1 an)
    historical_data = ticker_data.history(period='1y')

    print('Données Apple:', historical_data['Open'])

    # Appel de la fonction pour obtenir la valeur de l'action de compagnies du NASDAQ
    print('\n')
    print('=' * 50)
    print('Actions compagnies du NASDAQ')
    print('=' * 50, '\n')
    stocks = Stocks()

    for index in range(0, len(symboles), 1):
        symbol = symboles[index]
        stocks.add(get_stock(symbol))

    create(stocks)


def get_stock(symbol):

    # URL de la page Google Finance pour la compagnie dont le symbole NASDAQ est spécifié
    url = 'https://www.google.com/finance/quote/' + symbol + ':' + 'NASDAQ'

    # Faire la requête GET pour obtenir le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête s'est bien déroulée
    if response.status_code == 200:
        # Analyser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        symbol = get_symbol(soup)
        price = get_price(soup)
        date = get_date(soup)
        company = get_company(soup)
        comment = get_comment(soup)
        prev_close = get_prev_close(soup)
        avg_volume = get_avg_volume(soup)

        stock = Stock(symbol=symbol, company=company, price=price, date=date, comment=comment,
                      prev_close=prev_close, avg_volume=avg_volume)
        print("=" * 80)
        return stock

    else:
        print("=" * 80)
        return "Erreur lors de la requête GET.", None




def get_avg_volume(soup):
    # Trouver l'élément contenant le AVG VOLUME
    avg_volume_element = soup.find('div', class_='gyFHrc')
    avg_volume_text = ''
    if avg_volume_element:
        # Extraire le texte contenant le AVG VOLUME
        avg_volume_text = avg_volume_element.text.strip()
        print('AVG Volume:', avg_volume_text)
    else:
        print("Impossible de récupérer le AVG VOLUME.")
    return avg_volume_text


def get_prev_close(soup):
    # Trouver l'élément contenant le PREVIOUS CLOSE
    prev_close_element = soup.find('div', class_='P6K39c')
    prev_close_text = ''
    if prev_close_element:
        # Extraire le texte contenant le PREVIOUS CLOSE
        prev_close_text = prev_close_element.text.strip()
        print('PREV CLOSE:', prev_close_text)
    else:
        print("Impossible de récupérer le PREVIOUS CLOSE.")
    return prev_close_text


def get_comment(soup):
    # Trouver l'élément contenant un commentaire sur l'action de la compagnie
    comment = ''
    comment_element = soup.find('div', class_='F2KAFc')
    if comment_element:
        # Extraire le texte contenant le commentaire sur la compagnie
        comment = comment_element.text
    print('Commentaire:', comment)
    return comment


def get_company(soup):
    # Trouver l'élément contenant le nom de la compagnie
    company_name = ''
    company_name_element = soup.find('div', class_='zzDege')
    if company_name_element:
        # Extraire le texte contenant le nom de la compagnie
        company_name = company_name_element.text
    else:
        print("Impossible de récupérer le nom de la compagnie.")
    print('Compagnie:', company_name)
    return company_name


def get_date(soup):
    # Trouver l'élément contenant la date et l'heure
    time_element = soup.find("div", class_="ygUjEc")
    # Extraire la date et l'heure
    current_time = ''
    if time_element:
        current_time = time_element.text.strip()
    else:
        current_time = "Impossible de trouver la date et l'heure de la cotation."
    print('Date:', current_time)
    return current_time


def get_price(soup):
    # Trouver l'élément contenant la valeur de l'action
    price_element = soup.find("div", class_="YMlKec fxKbKc")
    stock_price = ''
    # Extraire la valeur de l'action
    if price_element:
        stock_price = price_element.text.strip()
    else:
        stock_price = "Impossible de trouver la valeur de l'action."
    #stock_price = stock_price.strip('$')
    print("Prix de l'action:", stock_price)
    return stock_price


def get_symbol(soup):
    # Extraire le texte de la balise <title>
    title_text = soup.title.text
    # Extraire le symbole NASDAQ du contenu de la balise <title>
    title = title_text.split()
    symbol = ''
    for index in range(0, len(title), 1):
        # Vérifier si l'élément contient le symbole NASDAQ, exple: "(TSLA)"
        if 'Stock' == title[index]:
            symbol = title[index - 1].strip('()')  # Enlever les parenthèses autour du symbole si nécessaire
            break  # Arrêter la boucle dès que le symbole est trouvé
    print('Symbole:', symbol)
    return symbol
