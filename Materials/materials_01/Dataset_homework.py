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

Task:

1) Create script to pars json file into DataFrame.
2) Clean text in 'headline' and 'short_description columns:
    1. Remove punctuation.
    2. Tokenize.
    3. Remove stopwords.
"""