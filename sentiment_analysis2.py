import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import nltk


import pandas 
from pandas import DataFrame 
from GoogleNews import GoogleNews
from datetime import date, timedelta
from newspaper import Article, Config
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Handle SSL certificate verification issue
ssl._create_default_https_context = ssl._create_default_https_context

# Extracting news for a specific company
now = date.today()
yesterday = date.today() - timedelta(days=1)
google_news = GoogleNews(start=yesterday, end=now)
google_news.search("intel")
result = google_news.result()
df = DataFrame(result)

# Code snippet for summarizing articles

# Creating an empty list
article_list = [] 

# Iterating over the dataframe
for i in df.index:
    article_dict = {} 
    article_obj = Article(df['link'][i], config=Config())
    
    try:
        # Disable SSL verification
        article_obj.download(verify=False)
        article_obj.parse()
        article_obj.nlp()
    except:
        pass 
    
    # Storing results in the dictionary
    pandas.set_option('display.max_columns', None)

    article_dict['Date'] = df['date'][i] 
    article_dict['Media'] = df['media'][i]
    article_dict['Title'] = article_obj.title
    article_dict['Article'] = article_obj.text
    article_dict['Summary'] = article_obj.summary
    article_dict['Key_words'] = article_obj.keywords
    article_list.append(article_dict)

# Creating a dataframe
news_df = DataFrame(article_list)
print(news_df)

# Initializing variables
positive = 0
negative = 0
neutral = 0
news_list = []
neutral_list = []
negative_list = []
positive_list = []

# Iterating over the news summaries
for news in news_df['Summary']:
    news_list.append(news)
    analyzer = SentimentIntensityAnalyzer().polarity_scores(news)
    neg = analyzer['neg']
    neu = analyzer['neu']
    pos = analyzer['pos']

    if neg > pos:
        negative_list.append(news)
        negative += 1
    elif pos > neg:
        positive_list.append(news)
        positive += 1
    elif pos == neg:
        neutral_list.append(news)
        neutral += 1

positive_percentage = (positive / len(news_df)) * 100
negative_percentage = (negative / len(news_df)) * 100
neutral_percentage = (neutral / len(news_df)) * 100

print("Positive Sentiment:", '%.2f' % positive_percentage, end='\n')
print("Neutral Sentiment:", '%.2f' % neutral_percentage, end='\n')
print("Negative Sentiment:", '%.2f' % negative_percentage, end='\n')