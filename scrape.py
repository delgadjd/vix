import newsapi
import requests
from prettytable import PrettyTable
from flask import Flask, render_template, request
from newsapi import NewsApiClient




def coin_info():
    coins = []

    #create table
    tableobj = PrettyTable()
    api_endpoint = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=fa2186b8-20ab-4297-a3c2-4d9a4ff32387'

    #test string concatenation
    #api_endpoint

    json_data = requests.get(api_endpoint).json()

    #requests.get(api_endpoint).json()

    cryptodata = json_data['data']

    for currency in cryptodata:
        curr_name = currency['name']
        curr_price = currency['quote']['USD']['price']
        curr_change_1h = currency['quote']['USD']['percent_change_1h']
        curr_change_24h = currency['quote']['USD']['percent_change_24h']
        curr_change_7d = currency['quote']['USD']['percent_change_7d']
        tableobj.add_row([curr_name, curr_price, curr_change_1h, curr_change_24h, curr_change_7d])
        this_coin = [curr_name, curr_price, curr_change_1h, curr_change_24h, curr_change_7d]
        coins.append(this_coin)
    tableobj.field_names = ['Currency Name', 'Currency Price', 'Currency 1h Change', 'Currency 24h Change', 'Currency 7d Change']

    print(tableobj)
    htmlCode = tableobj.get_html_string(attributes={"class": "table"}, format=True)
    #print(htmlCode)
    # Open prettyTable.html file
    f = open("tableobj.html", "w")
    # Write "htmlCode" to prettyTable.html
    f.write(htmlCode)
    # Close prettyTable.html
    f.close()
    return coins


coins = coin_info()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/crypto')
def coin():
    return render_template('tableobj2_working.html', coins=coins)

@app.route('/news')
def news():
    newsapi = NewsApiClient(api_key="1554402b1dd04f24be1d385f7e14264a")
    topheadlines = newsapi.get_top_headlines(category='business', language='en', country='us')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('news_search.html', context=mylist)

@app.route('/results/', methods=['POST'])
def get_results():
    newsapi = NewsApiClient(api_key="1554402b1dd04f24be1d385f7e14264a")
    keyword = request.form['keyword']  # getting input from user

    news = newsapi.get_top_headlines(q=keyword,
                                     category='business',
                                     language='en',
                                     country='us')
    # print(news['articles'])
    return render_template('news_search.html', news=news['articles'])


@app.route('/stocks')
def stocks():
    return render_template('stocks.html')


if __name__ == "__main__":
    app.run(debug=True)


