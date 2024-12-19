import nltk
nltk.download('punkt_tab')
import os
from random import randrange
from mastodon import Mastodon

base_url = 'https://mastodon.ocert.at'

app = Mastodon.create_app(
    'pytooterapp',
    api_base_url = base_url,
)

mastodon = Mastodon(client_id = app[0], client_secret = app[1], api_base_url =
                    base_url)
token = mastodon.log_in(
    os.environ['NISARGADATTA_EMAIL'],
    os.environ['NISARGADATTA_PWD'],
)

mastodon = Mastodon(access_token = token, api_base_url = base_url)


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
