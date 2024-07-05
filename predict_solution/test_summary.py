import nltk
from transformers import pipeline
from nltk.tokenize import sent_tokenize

# Download NLTK resources
nltk.download('punkt')

# Example solutions
all_solutions = [
    'Ginger tea and crackers helped settle my stomach. I also found relief using anti-nausea medication prescribed by my doctor.',
    'Migraines are tough. Taking prescribed migraine medication and resting in a dark, quiet room helped a lot. Applying a cold pack to my head also provided some relief.',
    'Staying hydrated and resting in a quiet place helped. Over-the-counter pain relievers and ginger candies also eased my nausea and headache.',
    'I used a heating pad on my abdomen, which provided some comfort. Avoiding spicy and fatty foods and sticking to a bland diet helped reduce the pain.',
    'Staying in bed, drinking plenty of fluids, and taking fever reducers like acetaminophen helped me get through the worst of it.',
    'A warm bath with Epsom salts and taking ibuprofen helped alleviate the body aches. Gentle stretching exercises also made a difference.'
]

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Combine all solutions into a single text
combined_solutions = " ".join(all_solutions)

# Generate a summary using the summarization pipeline
summary = summarizer(combined_solutions, max_length=130, min_length=30, do_sample=False)

# Print the summary
print("Summary:", summary[0]['summary_text'])
