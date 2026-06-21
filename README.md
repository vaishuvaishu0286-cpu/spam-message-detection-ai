Spam Message Detection Using Artificial Intelligence

Problem Statement

Many users receive unwanted spam messages daily through SMS and social media. These spam messages may contain advertisements, fake offers, or harmful links. Identifying spam manually is difficult and time-consuming. This project uses Artificial Intelligence and Machine Learning to automatically detect whether a message is spam or genuine.

Impact of the Problem

- Helps users avoid unwanted and harmful messages.
- Improves message security.
- Saves time by automatically filtering spam messages.
- Uses AI techniques for smart message classification.

Key Outcomes

- Detects spam and genuine messages automatically.
- Improves user security from fake or unwanted messages.
- Saves time by filtering spam messages quickly.
- Uses Artificial Intelligence for message classification.
- Enhances digital communication safety.

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- Machine Learning
- Streamlit

Project Structure

spam-message-detection-ai/

├── dataset/
│   └── spam.csv

├── notebooks/
│   └── spam_detection.ipynb

├── src/
│   ├── preprocess.py
│   ├── train_model.py
│   └── predict.py

├── requirements.txt
├── README.md
└── app.py

Machine Learning Workflow

Dataset
↓
Preprocessing
↓
CountVectorizer
↓
Train-Test Split
↓
Naive Bayes Model
↓
Prediction
↓
Spam / Ham Output

Requirements

Add the following to "requirements.txt":

pandas
numpy
scikit-learn
nltk
streamlit

Install libraries using:

pip install -r requirements.txt

Dataset

SMS Spam Collection Dataset from Kaggle.

Model Description

1. Load the dataset.
2. Clean and prepare the data.
3. Convert text into numerical vectors using CountVectorizer.
4. Split data into training and testing sets.
5. Train a Multinomial Naive Bayes model.
6. Predict whether messages are Spam or Ham.
7. Evaluate model accuracy.

Expected Output

Input:

Congratulations! You won a free prize.

Output:

Spam

Input:

Hello, how are you today?

Output:

Ham

Future Enhancements

- Real-time spam detection
- Deep Learning models
- Email spam detection
- Mobile application integration
- Web-based dashboard using Streamlit

GitHub Upload Commands

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_LINK
git push -u origin main