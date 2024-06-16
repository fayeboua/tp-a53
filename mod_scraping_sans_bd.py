
import requests
from bs4 import BeautifulSoup
from collections import namedtuple
 
symboles = ['MSFT', 'AAPL', 'AMZN', 'META', 'AVGO', 'GOOGL', 'GOOG', 'COST', 'TSLA','NFLX']
compagnies = ['Microsoft Corp', 'Apple Inc', 'Amazon.Com Inc', 'Meta Platforms Inc', 'Broadcom Inc', 'Alphabet Inc','Alphabet Inc','Costco Wholesale Corp','Tesla Inc','Netflix Inc']

Meteo = namedtuple('Meteo', ['prevision', 'location', 'temperature'])


def afficher_meteo(curseur):
    for doc in curseur:
        print(doc)


def main():
    print_header()
    #code = input('Indiquer votre code postal pour avoir la météo (H4N1L4)? ')
    code="H1kXC"
    html = get_html_from_url("https://meteo.gc.ca/city/pages/qc-147_metric_f.html" )
    print('------ Html content ------')
    #print(html)
    report = get_meteo_from_html(html)

    print('Condition météo: {} \n Location:{} \n Temperature:{}'.format(
        report.prevision ,report.location, report.temperature
    ))
    #Insertion BD mongo

    # Appel de la fonction pour obtenir la valeur de l'action de compagnies du NASDAQ
    print('\n')
    print('='*50)
    print('Actions compagnies du NASDAQ')
    print('='*50,'\n')
    for index in range (0, len(symboles),1):
        compagnie = compagnies[index]
        symbole = symboles[index]
        get_stock_price(compagnie, symbole)


def get_stock_price(compagnie, symbole):
    # URL de la page Google Finance pour la compagnie dont le symbole NASDAQ est spécifié
    #url = "https://www.google.com/finance/quote/MSFT:NASDAQ"
    url = 'https://www.google.com/finance/quote/'+symbole+':'+'NASDAQ'

    # Faire la requête GET pour obtenir le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête s'est bien déroulée
    if response.status_code == 200:
        # Analyser le contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Trouver l'élément contenant la valeur de l'action
        price_element = soup.find("div", class_="YMlKec fxKbKc")

        stock_price=''
        # Extraire la valeur de l'action
        if price_element:
            stock_price = price_element.text.strip()
        else:
            stock_price = "Impossible de trouver la valeur de l'action."

        # Trouver l'élément contenant la date et l'heure
        #time_element = soup.find("div", class_="nzPR9d")
        time_element = soup.find("div", class_="ygUjEc")

        # Extraire la date et l'heure
        current_time=''
        if time_element:
            current_time = time_element.text.strip()
        else:
            current_time = "Impossible de trouver la date et l'heure de la cotation."

        # Trouver l'élément contenant le nom de la compagnie
        company_name=''
        company_name_element = soup.find('div', class_='ZvmM7')
        if company_name_element:
            # Extraire le texte contenant le nom de la compagnie
            company_name = company_name_element.text.strip()
        else:
            print("Impossible de récupérer le nom de la compagnie.")

        #return stock_price, current_time, day range
        print('->Compagnie:',company_name)
        print("Prix de l'action:",stock_price)
        print('Date:',current_time)

        # Trouver l'élément contenant le PREVIOUS CLOSE
        prev_close_element = soup.find('div', class_='P6K39c')
        if prev_close_element:
            # Extraire le texte contenant le PREVIOUS CLOSE
            prev_close_text = prev_close_element.text.strip()
            print('PREV CLOSE', prev_close_text)
        else:
            print("Impossible de récupérer le PREVIOUS CLOSE.")
        # Trouver l'élément contenant le AVG VOLUME
        avg_volume_element = soup.find('div', class_='gyFHrc')
        if avg_volume_element:
            # Extraire le texte contenant le AVG VOLUME
            avg_volume_text = avg_volume_element.text.strip()
            print('AVG Volume', avg_volume_text)
        else:
            print("Impossible de récupérer le AVG VOLUME.")

    else:
        return "Erreur lors de la requête GET.", None

def print_header():
    print('---------------------------------')
    print('           METEO TOTO')
    print('---------------------------------')
    print()


def get_html_from_url(url):
    url= url
    response = requests.get(url).content
    # Parse the html content

    soup =  BeautifulSoup(response, "html.parser")
    print("=" * 50)
    print(soup.title.get_text())
    print("=" * 50)
    return soup



def get_meteo_from_html(html):
    prevision = html.find("div",attrs={"class": "col-xs-12"}).findChildren("a",
                                        attrs={"class": "linkdate"})[0]
    location= html.find("h1",attrs={"id": "wb-cont"})
    #temperature = html.find("p", attrs={"class": "mrgn-tp-md mrgn-bttm-sm conds-lead"})
    temperature = html.find("p", attrs={"class": "mrgn-bttm-sm lead mrgn-tp-sm"})
    # print((prevision.get_text(),location.get_text(), temperature.get_text()))
    report=Meteo(prevision.get_text(),location.get_text(), temperature.get_text())
    return report


def trouver_ville_prov(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()