# Import flask
from flask import Flask, render_template, redirect, request, session

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo

# Import the python scraping files (scrape_stock.py, hashtag.py)
import scrape_stock
import hashtag
import multisite_scraping

import os


print(__name__)
# Create an instance of our Flask app.
app = Flask(__name__, template_folder='examples')
app.secret_key = os.urandom(24)
stock_data = {}
ml_data = {}
data = []

# Set route to query mongoDB and make an HTML template
@app.route("/")
def home():


    # Create the empty templates for the stock and twitter scrapes
    return render_template("1-dashboard.html")

# Create a route called /scrape
@app.route("/scrapestock")
def scrape():
    global stock_data
    global data
    global stock_data
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # stock scraping function and store in session
    stock_data = scrape_stock.scrape_stock()
    
    # retrieve the value of data from session
    

    # update mongo database
    # stock_info.update({}, stock_data, upsert=True)

    # redirect back to home page
    return render_template("8-stockticker-tweeter.html", stock_info=stock_data, data=data, eco_scrape_dict=ml_data)

@app.route("/multiscrape")
def multi_scrape():
    global ml_data
    global data
    global stock_data
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # stock scraping function and store in session
    ml_data = multisite_scraping.scrape_bonds()
    ml_data = multisite_scraping.scrape_fedrate()
    ml_data = multisite_scraping.scrape_unemployment()
    ml_data = multisite_scraping.scrape_gold()
    ml_data = multisite_scraping.scrape_cpi()
    ml_data = multisite_scraping.scrape_inflation()
    ml_data = multisite_scraping.scrape_gdp()
    ml_data = multisite_scraping.scrape_housesales()
    ml_data = multisite_scraping.scrape_housestarts()
    ml_data = multisite_scraping.scrape_earnings()
    ml_data = ml_data[0]
    

    # retrieve the value of data from session
    

    # update mongo database
    # stock_info.update({}, stock_data, upsert=True)

    # redirect back to home page
    return render_template("8-stockticker-tweeter.html", stock_info=stock_data, data=data, eco_scrape_dict=ml_data)
    # Create a route called /scrape
@app.route("/scrapetweet")
def scrapetweet():
    global ml_data
    global data
    global stock_data
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # twitter scraping function and store it in session
    n = int(request.args.get('n'))
    search = request.args.get('search')
    data = hashtag.get_tweets(n, search)

    # retrieve the previous value of stock_data from session
    #stock_data=session.get('stock_dara')

    # update mongo database
    # stock_info.update({}, stock_data, upsert=True)

    # redirect back to home page
    return render_template("8-stockticker-tweeter.html", stock_info=stock_data, data=data, eco_scrape_dict=ml_data)

@app.route("/map")
def unemploymentMap():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("2-unemployment-map.html")   

@app.route("/gdpmap")
def gdpMap():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("4-gdp-map.html")   

@app.route("/educationmap")
def ueducationMap():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("5-education-map.html")   

@app.route("/incomemap")
def incomeMap():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("9-income-map.html")   

@app.route("/gdp")
def gdp():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("3-gdp.html")   

@app.route("/indicators")
def econIndicators():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("6-economic-indicators.html")

@app.route("/aboutus")
def aboutus():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("7-about-us.html")

@app.route("/presentation")
def presentation():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("10-presentation.html")

@app.route("/blog")
def blog():
    # execute scrape funcions
    # stock_info = mongo.db.stock_info

    # redirect back to home page
    return render_template("11-blog.html")

@app.route("/stocktweeter")
def stocktweeter():
    global ml_data
    global data
    global stock_data
    # execute scrape funcions
    # find and store the data in stock_info mongo db
    # stock_info = mongo.db.stock_info.find_one()
    print(stock_data)
    print(data)
    print(ml_data)

    # redirect back to home page
    return render_template("8-stockticker-tweeter.html", stock_info=stock_data, data=data, eco_scrape_dict=ml_data)

#if __name__ == "__main__":
print("1...")
app.run(debug=True)