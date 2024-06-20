import urllib.request
import pandas as pd
import yfinance as yf

# URL du fichier TXT contenant la liste des compagnies du NASDAQ
url = "ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt"

# Télécharger le fichier TXT
local_filename, headers = urllib.request.urlretrieve(url, 'nasdaq_companies.txt')

# Lire le fichier TXT avec pandas, en spécifiant le délimiteur de champ
df = pd.read_csv(local_filename, sep='|')

# Retirer la dernière ligne de pied de page
df = df[:-1]

# Afficher les premières lignes pour vérifier
print(df.head())

# Parcourir les tickers et obtenir des informations avec yfinance
for ticker in df['Symbol']:
    try:
        company = yf.Ticker(ticker)
        info = company.info
        print(f"Company: {info.get('shortName')}, Ticker: {ticker}, Sector: {info.get('sector')}")
    except Exception as e:
        print(f"Could not retrieve data for ticker {ticker}: {e}")
