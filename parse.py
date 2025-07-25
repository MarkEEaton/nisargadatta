import nltk
nltk.download('punkt_tab')
import os
from random import randrange
from mastodon import Mastodon


base_url = 'https://mastodon.ocert.at'
mastodon = Mastodon(access_token = os.environ['NISBOTSECRET'], api_base_url = base_url)

with open("iamspaced.txt", "r") as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)

random_toot = randrange(0, len(sentences) - 1)
sentence = sentences[random_toot]

while ("Questioner:" or "Maharaj:") in sentence:
    print("toot failed: " + sentence)
    random_toot = randrange(0, len(sentences) - 1)
    sentence = sentences[random_toot]
else:
    mastodon.toot(sentence)
    print("toot succeeded: " + sentence)
