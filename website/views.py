from flask import Blueprint, session,render_template,request ,redirect, url_for
import requests

views = Blueprint('views', __name__)

@views.route('/', methods=["GET","POST"])
def home():
    if session.get("user"):
        user = session["user"]
        return render_template('index.html')
    else:
        return redirect(url_for("auth.login"))

@views.route('<user>', methods=["GET","POST"])
def user(user):
        if session.get("user",None):
            symbol = request.form.get("symbol")
            print(symbol)
            api_key = session['API_KEY']
            if symbol:
                BASE_URL = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={api_key}'
                resp = requests.get(BASE_URL).json()
                return resp
            else:
                return render_template('index.html')
        else:
            return redirect(url_for("auth.login"))
    
@views.route('basics', methods=["GET","POST"])
def basics():
    if session.get("user"):
        if request.method == 'POST':
            symbol = request.form.get("symbol")
        else:
            symbol = session.get('symbol', None)
        api_key = session['API_KEY']
        if symbol:
                session["symbol"] = symbol
                BASE_URL = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={api_key}'
                resp = requests.get(BASE_URL).json()
                data = resp['bestMatches']
                headings = ("Symbol", "Name", "Type","Region","MarketOpen","MarketClose","TimeZone","Currency","matchScore")
                return render_template('basics.html',headings=headings, data=data)
        else:
            return render_template('basics.html')
    else:
        return redirect(url_for("auth.login"))

    
@views.route('quote/', methods=["GET",'POST'])
def quote():
    if session['user']:
        if request.method == 'POST':
            symbol = request.form.get("symbol")
        else:
            symbol = session.get('symbol', None)
        api_key = session['API_KEY']
        if symbol:
                BASE_URL = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
                resp = requests.get(BASE_URL).json()
                data = resp['Global Quote']
                headings = ('Symbol', "Open", "High", "Low", "Price", "Volume", "Latest Trading Day", "Previous Close", "Change", "Chang Percent")
                return render_template('current_quote.html',headings=headings, data=data)
        else:
            return render_template('current_quote.html')

    else:
        return redirect(url_for("auth.login"))
    


@views.route('historical-daily',methods=["GET",'POST'])
def historical_daily():
    if session['user']:
        if request.method == 'POST':
            symbol = request.form.get("symbol")
        else:
            symbol = session.get('symbol', None)
        api_key = session['API_KEY']
        if symbol:
                BASE_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
                resp = requests.get(BASE_URL).json()
                headings_top = resp.keys()
                data_meta = resp['Meta Data']
                data_main = resp['Time Series (Daily)']
                headings_meta = ("Info", "Symbol", "Last Refreshed","output size" ,"Timezone")
                headings_main = ("Open", "High", "Low", "Close", "Volume")
                return render_template('historical_daily.html',headings_main=headings_main,data_meta=data_meta, data_main=data_main, headings_meta=headings_meta
                                       , headings_top=headings_top)
        else:

            return render_template('historical_daily.html')
    else:
        return redirect(url_for("auth.login"))

@views.route('historical-weekly',methods=["GET",'POST'])
def historical_weekly():
    if session['user']:
        if request.method == 'POST':
            symbol = request.form.get("symbol")
        else:
            symbol = session.get('symbol', None)
        api_key = session['API_KEY']
        if symbol:
                BASE_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={api_key}'
                resp = requests.get(BASE_URL).json()
                headings_top = resp.keys()
                data_meta = resp['Meta Data']
                data_main = resp['Weekly Time Series']
                headings_meta = ("Info", "Symbol", "Last Refreshed" ,"Timezone")
                headings_main = ("Open", "High", "Low", "Close", "Volume")
                return render_template('historical_weekly.html',headings_main=headings_main,data_meta=data_meta, data_main=data_main, headings_meta=headings_meta
                                       , headings_top=headings_top)
        else:

            return render_template('historical_weekly.html')
    else:
        return redirect(url_for("auth.login"))


@views.route('historical-monthly',methods=["GET",'POST'])
def historical_monthly():
    if session['user']:
        if request.method == 'POST':
            symbol = request.form.get("symbol")
        else:
            symbol = session.get('symbol', None)
        api_key = session['API_KEY']
        if symbol:
                BASE_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}'
                resp = requests.get(BASE_URL).json()
                headings_top = resp.keys()
                data_meta = resp['Meta Data']
                data_main = resp['Monthly Time Series']
                headings_meta = ("Info", "Symbol", "Last Refreshed", "Timezone")
                headings_main = ("Open", "High", "Low", "Close", "Volume")
                return render_template('historical_monthly.html',headings_main=headings_main,data_meta=data_meta, data_main=data_main, headings_meta=headings_meta
                                       , headings_top=headings_top)
        else:

            return render_template('historical_monthly.html')
    else:
        return redirect(url_for("auth.login"))



@views.route('technical')
def technical(user):
    if session['user']:
        BASE_URL = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo'
        user = session["user"]
        print(session)
        print(session.keys())
        resp = requests.get(BASE_URL).json()
        return resp
        # return render_template("index.html")
    else:
        return redirect(url_for("auth.login"))