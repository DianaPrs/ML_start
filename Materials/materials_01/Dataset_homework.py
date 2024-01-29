"""
Content:

This dataset contains around 210k news headlines.
Each record in the dataset consists of the following attributes:

'category': category in which the article was published.
'headline': the headline of the news article.
'authors': list of authors who contributed to the article.
'link': link to the original news article.
'short_description': Abstract of the news article.
'date': publication date of the article.

Task 1:

1) Create script to pars json file into DataFrame.
2) Clean text in 'headline' and 'short_description columns:
    1. Remove punctuation.
    2. Tokenize.
    3. Remove stopwords.

Task 2:
1) Try to apply Lemmatizing.
2) Make EDA (Exploratory Data Analysis):
    1. Categories count
    2. Create plot
    3. Join headlines and description to get statistic: 
        - is there any missing data
        - 3 most frequent words for categoty
        - max/min/median word length for category

for inspiration:
https://towardsdatascience.com/a-data-scientists-essential-guide-to-exploratory-data-analysis-25637eee0cf6
https://www.kaggle.com/code/ekami66/detailed-exploratory-data-analysis-with-python
https://saturncloud.io/blog/a-quick-guide-to-exploratory-data-analysis-using-jupyter-notebook/


"""