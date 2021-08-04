from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/news/al-jazeera')
def index():
    newsapi=NewsApiClient(api_key='1554402b1dd04f24be1d385f7e14264a')
    topheadlines=newsapi.get_top_headlines(category='business')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len((articles))):
        my_articles = articles[i]

        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])

    my_list = zip(news, desc, img)

    return render_template('news.html', context=my_list)

if __name__ == "__main__":
    app.run(debug=True)