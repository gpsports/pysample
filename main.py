import tweepy
import json

afc_east = ("patriots", "miamidolphins", "buffalobills", "nyjets")
afc_west = ("chiefs", "chargers", "broncos", "raiders")
afc_north = ("ravens", "steelers", "browns", "bengals")
afc_south = ("houstontexans", "colts","titans", "jaguars")
afc = afc_east + afc_west + afc_north + afc_south

nfc_east = ("dallascowboys", "eagles", "redskins", "giants")
nfc_west = ("rams", "seahawks", "49ers", "cardinals")
nfc_north = ("chicagobears", "vikings", "packers", "lions")
nfc_south = ("saints", "atlantafalcons", "panthers", "buccaneers")
nfc = nfc_east + nfc_west + nfc_north + nfc_south

nfl = afc + nfc

#with open('keys.json') as f:
#    data = json.load(f)

# Setup the authentication
#auth = tweepy.OAuthHandler(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
#auth.set_access_token(data["ACCESS_TOKEN"], data["ACCESS_SECRET"])

# Create an authenticated connection to the Twitter API using Tweepy
#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

def do_something():
    ''' This is a function that prints Hello World to the console
    '''
#    statuses = api.user_timeline(screen_name='timbull')
#    print(statuses)
    print("Hello world!")

if __name__ == '__main__':
    # Entry point for command line
    do_something()
