import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

data = {
    "problem":[
        "heart attack",
        "chest pain",
        "accident injury",
        "pregnancy delivery",
        "surgery operation",
        "fever cold",
        "infection"
    ],

    "ward":[
        "ICU",
        "ICU",
        "Emergency",
        "Maternity",
        "OT",
        "General",
        "General"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["problem"])

model = MultinomialNB()
model.fit(X, df["ward"])

pickle.dump(model, open("ml_model/ward_model.pkl","wb"))
pickle.dump(vectorizer, open("ml_model/vectorizer.pkl","wb"))

print("Model trained successfully")