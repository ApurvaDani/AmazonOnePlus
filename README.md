# AmazonOnePlus
Review Classification and Product Scraping.
Spiders folder contains the amazon_reviews.py file which has the main logic of scraping.
items.py includes temporary container for storing scrapped results.
pipelines.py is used to create pipeline between spider and MongoDB to store results.
Sentiment.py classifies the reviews into negative or positive.
textclassification.py is used to classify reviews into different categories.
