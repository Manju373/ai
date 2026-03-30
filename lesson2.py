from textblob import TextBlob
def ai(text):
    blob = TextBlob(text) 
    sentiment = blob.sentiment.polarity 
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
text=input("Enter a sentence to analyze its sentiment: ")
print(ai(text))