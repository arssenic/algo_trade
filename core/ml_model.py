import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run_ml_model(df, symbol):
    df = df.dropna()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    features = df[['RSI', '20DMA', '50DMA']]
    labels = df['Target']
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return accuracy_score(y_test, preds)