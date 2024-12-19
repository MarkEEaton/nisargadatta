import nltk
nltk.download('punkt_tab')
from random import randrange
from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'nisargadatta_usercred.secret',
    api_base_url = 'https://mastodon.ocert.at'
)

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
