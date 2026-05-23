import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
data = {
    'message': [
        'Congratulations you won a prize',
        'Hello how are you',
        'Claim your free reward now',
        'Let us meet tomorrow'
    ],
    'label': ['spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)

# Convert text into numbers
cv = CountVectorizer()
x = cv.fit_transform(df['message'])

# Labels
y = df['label']

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(x_train, y_train)

# Test message
msg = ["Win free cash prize now"]
msg_vector = cv.transform(msg)

prediction = model.predict(msg_vector)

print("Prediction:", prediction[0])