import sys
from PyQt5 import QtWidgets
import requests
from bs4 import BeautifulSoup

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currency Check and Convert Application")
        self.url_currency = "https://kur.doviz.com"
        self.url_stock = "https://borsa.doviz.com/endeksler"
        self.init_ui()
        self.connection_top()
        self.connection_cur()

    def connection_top(self):
        stock_list = list()
        new_s_l = list()

        response_stock = requests.get(self.url_stock)
        stock_content = response_stock.content

        soup1 = BeautifulSoup(stock_content, "html.parser")
        headers_stock = soup1.find_all("span", {"class": "value"})

        for i in headers_stock:
            stock_list.append(i)
        for i in stock_list:
            for j in i:
                new_s_l.append(j)

        xu_100 = new_s_l[4]
        btc = new_s_l[5]
        gold =new_s_l[0].replace(".", "")
        gold = gold.replace(",", ".")
        dolares = new_s_l[1].replace(".", "")
        dolares = dolares.replace(",", ".")
        gram_gold = float(gold) / float(dolares)
        gram_gold = "{:.2f}".format(gram_gold)

        self.s30.setText(xu_100)
        self.s50.setText(btc)
        self.s100.setText("$" + gram_gold)


    def connection_cur(self):

        currency_list = list()
        new_c_l = list()

        response_currency = requests.get(self.url_currency)
        currency_content = response_currency.content

        soup1 = BeautifulSoup(currency_content, "html.parser")
        headers_currency = soup1.find_all("td", {"class": "text-bold"})

        for i in headers_currency:
            currency_list.append(i)
        for i in currency_list:
            for j in i:
                new_c_l.append(j)

        self.dollar = new_c_l[1].replace(",", ".")
        self.euro = new_c_l[4].replace(",", ".")
        self.pound = new_c_l[7].replace(",", ".")
        self.canada = new_c_l[13].replace(",", ".")
        self.japan = new_c_l[34].replace(",", ".")
        self.china = new_c_l[88].replace(",", ".")
        self.aus = new_c_l[22].replace(",", ".")



    def init_ui(self):

        self.stock_title = QtWidgets.QLabel("Stock Market - BTC - Gold")

        self.stock30 = QtWidgets.QLabel("XU-100")
        self.stock50 = QtWidgets.QLabel("BTC")
        self.stock100 = QtWidgets.QLabel("Gram Gold")
        self.s30 = QtWidgets.QLabel("")
        self.s50 = QtWidgets.QLabel("")
        self.s100 = QtWidgets.QLabel("")

        stock_hbox = QtWidgets.QHBoxLayout()
        stock_hbox.addWidget(self.stock30)
        stock_hbox.addWidget(self.stock50)
        stock_hbox.addWidget(self.stock100)

        stock_hbox2 = QtWidgets.QHBoxLayout()
        stock_hbox2.addWidget(self.s30)
        stock_hbox2.addWidget(self.s50)
        stock_hbox2.addWidget(self.s100)

        stock_vboxtop = QtWidgets.QVBoxLayout()
        stock_vboxtop.addWidget(self.stock_title)
        stock_vboxtop.addStretch()
        stock_vboxtop.addLayout(stock_hbox)
        stock_vboxtop.addLayout(stock_hbox2)
        stock_vboxtop.addStretch()


        self.currency_title = QtWidgets.QLabel("Currency Check and Convert")
        self.btext = QtWidgets.QLabel("Base currency")
        self.base = QtWidgets.QLineEdit()

        self.tusd = QtWidgets.QLabel("USD: ")
        self.teur = QtWidgets.QLabel("EUR: ")
        self.tgbp = QtWidgets.QLabel("GBP: ")
        self.tcad = QtWidgets.QLabel("CAD: ")
        self.tjpy = QtWidgets.QLabel("JPY: ")
        self.tcny = QtWidgets.QLabel("CNY: ")
        self.taud = QtWidgets.QLabel("AUD: ")
        self.ttry = QtWidgets.QLabel("TRY: ")

        self.usd = QtWidgets.QLabel("")
        self.eur = QtWidgets.QLabel("")
        self.gbp = QtWidgets.QLabel("")
        self.cad = QtWidgets.QLabel("")
        self.jpy = QtWidgets.QLabel("")
        self.cny = QtWidgets.QLabel("")
        self.aud = QtWidgets.QLabel("")
        self.tur = QtWidgets.QLabel("")

        self.tamount = QtWidgets.QLabel("Amount")
        self.amount = QtWidgets.QLineEdit()
        self.convert = QtWidgets.QPushButton("Convert")
        self.result = QtWidgets.QLabel("")

        text_vbox = QtWidgets.QVBoxLayout()
        text_vbox.addStretch()
        text_vbox.addWidget(self.currency_title)
        text_vbox.addWidget(self.btext)
        text_vbox.addWidget(self.base)
        text_vbox.addStretch()

        curt_vbox = QtWidgets.QVBoxLayout()
        curt_vbox.addStretch()
        curt_vbox.addWidget(self.tusd)
        curt_vbox.addWidget(self.teur)
        curt_vbox.addWidget(self.tgbp)
        curt_vbox.addWidget(self.tcad)
        curt_vbox.addWidget(self.tjpy)
        curt_vbox.addWidget(self.tcny)
        curt_vbox.addWidget(self.taud)
        curt_vbox.addWidget(self.ttry)
        curt_vbox.addStretch()

        cur_vbox = QtWidgets.QVBoxLayout()
        cur_vbox.addStretch()
        cur_vbox.addWidget(self.usd)
        cur_vbox.addWidget(self.eur)
        cur_vbox.addWidget(self.gbp)
        cur_vbox.addWidget(self.cad)
        cur_vbox.addWidget(self.jpy)
        cur_vbox.addWidget(self.cny)
        cur_vbox.addWidget(self.aud)
        cur_vbox.addWidget(self.tur)
        cur_vbox.addStretch()

        cur_hbox = QtWidgets.QHBoxLayout()
        cur_hbox.addStretch()
        cur_hbox.addLayout(curt_vbox)
        cur_hbox.addLayout(cur_vbox)
        cur_hbox.addStretch()

        vmain_box = QtWidgets.QVBoxLayout()
        vmain_box.addStretch()
        vmain_box.addLayout(stock_vboxtop)
        vmain_box.addStretch()
        vmain_box.addWidget(self.currency_title)
        vmain_box.addWidget(self.btext)
        vmain_box.addWidget(self.base)
        vmain_box.addLayout(cur_hbox)
        vmain_box.addStretch()
        vmain_box.addWidget(self.tamount)
        vmain_box.addWidget(self.amount)
        vmain_box.addWidget(self.convert)
        vmain_box.addWidget(self.result)

        self.setLayout(vmain_box)

        self.convert.clicked.connect(self.currency_convert)

        self.show()

    def currency_convert(self):

        amount = self.amount.text()
        base = self.base.text()

        if len(base) == 0:
            self.result.setText("Please insert a base currency.")

        elif (base == "TRY" or base == "try") and (len(amount) == 0):
            base_cur = str(1)

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(base_cur)

        elif (base == "TRY" or base == "try") and (len(amount) != 0):
            base_cur = str(1)

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        elif (base == "USD" or base == "usd") and (len(amount) == 0):
            base_cur = self.dollar

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(str(float(base_cur)))

        elif (base == "USD" or base == "usd") and (len(amount) != 0):
            base_cur = self.dollar

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        elif (base == "EUR" or base == "eur") and (len(amount) == 0):
            base_cur = self.euro

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(str(float(base_cur)))

        elif (base == "EUR" or base == "eur") and (len(amount) != 0):
            base_cur = self.euro

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        elif (base == "GBP" or base == "gbp") and (len(amount) == 0):
            base_cur = self.pound

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(str(float(base_cur)))

        elif (base == "GBP" or base == "gbp") and (len(amount) != 0):
            base_cur = self.pound

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        elif (base == "CAD" or base == "cad") and (len(amount) == 0):
            base_cur = self.canada

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(str(float(base_cur)))

        elif (base == "CAD" or base == "cad") and (len(amount) != 0):
            base_cur = self.canada

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        elif (base == "JPY" or base == "jpy") and (len(amount) == 0):
            base_cur = self.japan

            self.usd.setText(str(float(base_cur)/float(self.dollar)/100))
            self.eur.setText(str(float(base_cur)/float(self.euro)/100))
            self.gbp.setText(str(float(base_cur)/float(self.pound)/100))
            self.cad.setText(str(float(base_cur)/float(self.canada)/100))
            self.jpy.setText(str(float(base_cur)/float(self.japan)/100))
            self.cny.setText(str(float(base_cur)/float(self.china)/100))
            self.aud.setText(str(float(base_cur)/float(self.aus)/100))
            self.tur.setText(str(float(base_cur)/100))

        elif (base == "JPY" or base == "jpy") and (len(amount) != 0):
            base_cur = self.japan

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)/100))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)/100))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)/100))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)/100))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)/100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)/100))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)/100))
            self.tur.setText(str(float(base_cur)*float(amount)/100))

        elif (base == "CNY" or base == "cny") and (len(amount) == 0):
            base_cur = self.china

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(str(float(base_cur)))

        elif (base == "CNY" or base == "cny") and (len(amount) != 0):
            base_cur = self.china

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        elif (base == "AUD" or base == "aud") and (len(amount) == 0):
            base_cur = self.aus

            self.usd.setText(str(float(base_cur)/float(self.dollar)))
            self.eur.setText(str(float(base_cur)/float(self.euro)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)))
            self.cad.setText(str(float(base_cur)/float(self.canada)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)))
            self.aud.setText(str(float(base_cur)/float(self.aus)))
            self.tur.setText(str(float(base_cur)))

        elif (base == "AUD" or base == "aud") and (len(amount) != 0):
            base_cur = self.aus

            self.usd.setText(str(float(base_cur)/float(self.dollar)*float(amount)))
            self.eur.setText(str(float(base_cur)/float(self.euro)*float(amount)))
            self.gbp.setText(str(float(base_cur)/float(self.pound)*float(amount)))
            self.cad.setText(str(float(base_cur)/float(self.canada)*float(amount)))
            self.jpy.setText(str(float(base_cur)/float(self.japan)*float(amount)*100))
            self.cny.setText(str(float(base_cur)/float(self.china)*float(amount)))
            self.aud.setText(str(float(base_cur)/float(self.aus)*float(amount)))
            self.tur.setText(str(float(base_cur)*float(amount)))

        else:

            self.result.setText("Please insert a correct currency.")

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())









