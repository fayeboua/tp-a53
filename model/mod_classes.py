class Stock:
    def __init__(self, symbol, company, date, close_quote, open_quote, low_quote, high_quote, avg_volume):
        self.symbol = symbol
        self.company = company
        self.close_quote = close_quote
        self.date = date
        self.open_quote = open_quote
        self.low_quote = low_quote
        self.high_quote = high_quote
        self.avg_volume = avg_volume

    def __str__(self):
        return (f'Symbole:{self.symbol}, Compagnie:{self.company}, Prix Action:{self.close_quote}, Date:{self.date},'
                f' Ouverture:{self.open_quote}, Bas:{self.low_quote}, Haut:{self.high_quote}, Volume:{self.avg_volume}')


class Stocks:
    def __init__(self):
        self.listing = []

    def add(self, stock: Stock):
        self.listing.append(stock)

    def print(self):
        print("=" * 50)
        for stock in self.listing:
            print(stock)
        print("=" * 50)

    def number_of_lines(self):
        print("=" * 50)
        size = len(self.listing)
        print("Le nombre de données chargées est :", size)
    def convert_to_json(self):
        dictionaire = []
        for stock in self.listing:
            # Création d'un dictionnaire à partir des résultats de la liste stock
            row_dict = {
                'symbol': stock.symbol,
                'company': stock.company,
                'date': str(stock.date),
                'quote': stock.close_quote,
                'open': stock.open_quote,
                'low': stock.low_quote,
                'high': stock.high_quote,
                'avg_volume': stock.avg_volume
            }
            dictionaire.append(row_dict)
        return dictionaire