class Stock:
    def __init__(self, symbol, company, price, date, comment, prev_close, avg_volume):
        self.symbol = symbol
        self.company = company
        self.price = price
        self.date = date
        self.comment = comment
        self.prev_close = prev_close
        self.avg_volume = avg_volume

    def __str__(self):
        return (f'Symbole:{self.symbol}, Compagnie:{self.company}, Price:{self.price}, Date:{self.date},'
                f' Comment:{self.comment}, Prev Close:{self.prev_close}, Avg Volume:{self.avg_volume}')


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
