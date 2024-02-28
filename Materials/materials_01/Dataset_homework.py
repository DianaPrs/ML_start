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

Task 3:
1) Get random sample of data for each category. Example: https://www.youtube.com/watch?v=CBCCcssjXQY
2) Vectorize it with TF-IDF https://www.linkedin.com/learning/nlp-with-python-for-machine-learning-essential-training/inverse-document-frequency-weighting?dApp=53239054&leis=LAA&resume=false&u=2113185

More info about data sampling: 
    Basics: https://www.youtube.com/watch?v=qhzkCebkSWE
    Sampling error: https://www.youtube.com/watch?v=uGuWrPFStdg
    Sampling methods: https://www.youtube.com/watch?v=be9e-Q-jC-0
    

Task 4:
Lesson from course: https://www.linkedin.com/learning/nlp-with-python-for-machine-learning-essential-training/random-forest-with-holdout-test-set?autoplay=true&resume=false&u=2113185
1) Split dataset to train and test with train_test_split. 
2) Fit train set to the RandomForest model and get the score for test set.
    - you can use this starting parametrs: 
        rf_model = RandomForestClassifier(n_estimators=100, n_jobs=-1, verbose=2)
        rf_model = rf_model.fit(X_train, y_train)
        rf_model.score(X_test, y_test)
"""