import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report

def analyze_reviews(df,col):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df[col])
    
    # Dummy sentiment labels for demonstration (replace with actual sentiment labels)
    y = [1 if i % 2 == 0 else 0 for i in range(len(df))]  
    
    model = SVC()
    model.fit(X, y)
    y_pred = model.predict(X)

    report = classification_report(y, y_pred, output_dict=True)
    df['sentiment'] = y_pred

    print("Analyzed DataFrame with Sentiments:")
    print(df.head())

    return pd.DataFrame(report).transpose(), df

def recommend_movies(df):
    positive_reviews = df[df['sentiment'] == 1]
    
    print("DataFrame with Positive Reviews:")
    print(positive_reviews.head())
    
    return positive_reviews.head(5)
