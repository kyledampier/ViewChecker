from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-mnli")
model = AutoModelForSequenceClassification.from_pretrained("facebook/bart-large-mnli")

# Load and Download model, if needed
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", multi_label=True)

# DEFINE key words/associations
emotions = [
    'joy',
    'anticipation',
    'anger',
    'disgust',
    'sadness',
    'surprise',
    'fear',
    'trust'
]

other = [
    'controversial',
    'intense',
    'social',
    'challenging',
    'positive',
    'negative',
    'apologetic',
    'generous',
    'interesting'
]

categories = emotions + other

# Generates dictionary
def generate_categories(title):
    return classifier(title, categories)

