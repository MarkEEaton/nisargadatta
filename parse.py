import nltk
nltk.download('punkt_tab')
import os
from random import randrange
from mastodon import Mastodon

base_url = 'https://mastodon.ocert.at'
mastodon = Mastodon(access_token=os.environ['NISBOTSECRET'], api_base_url=base_url)

try:
    with open("iamspaced.txt", "r") as f:
        text = f.read()
    
    if not text.strip():
        raise ValueError("Input file is empty")
    
    sentences = nltk.sent_tokenize(text)
    
    if not sentences:
        raise ValueError("No sentences found in the input file")
    
    # Filter out sentences containing the unwanted phrases
    filtered_sentences = [s for s in sentences if "Questioner:" not in s and "Maharaj:" not in s]
    
    if not filtered_sentences:
        raise ValueError("No valid sentences found after filtering")
    
    # Select a random sentence from the filtered list
    random_toot = randrange(0, len(filtered_sentences))
    sentence = filtered_sentences[random_toot]
    
    mastodon.toot(sentence)
    print("toot succeeded: " + sentence)
    
except FileNotFoundError:
    print("Error: iamspaced.txt file not found")
except KeyError:
    print("Error: NISBOTSECRET environment variable not set")
except Exception as e:
    print(f"Error occurred: {e}")
