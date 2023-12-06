import time

import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


ALPHA_API_KEY = "Z6APOLEE9VA1B53D"
NEWS_API_KEY = "992b893efece4269989d5c355bc1dca9"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_data)
print(yesterday_closing_price)
# Get the day before yesterday's closing stock price

day_before_yestarday_data = data_list[1]
day_before_yestarday_closing_price = day_before_yestarday_data["4. close"]
print(day_before_yestarday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(float(yesterday_closing_price) - float(day_before_yestarday_closing_price))
print(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = difference / float(yesterday_closing_price) * 100
print(diff_percent)

# If percentage is greater than 5 then print("Get News").
# Use the News API to get articles related to the COMPANY_NAME.
if diff_percent > 1:
    news_params = {
        "apiKey":NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles =[f"Headline: {article['title']}.\n Brief: {article['description']}" for article in three_articles]

for article in formatted_articles:
    print(article)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

