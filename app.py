from flask import Flask, render_template
import articles

app = Flask(__name__)

@app.route('/')
def index():
    # Call function to collect article links
    Rlinks = articles.reddit_article_links
    Mlinks=articles.main_articles
    Tlinks=articles.trending_articles
    TTlinks=articles.trending_tech_articles
    return render_template('index.html', Rlinks=Rlinks, Mlinks=Mlinks, Tlinks=Tlinks, TTlinks=TTlinks)

if __name__ == '__main__':
    app.run(debug=True)