# pysample
This is a basic python sample app with instructions for you to test and set your
environment up.

Once configured, you can complete the assignment.

## Setting up basic python (assuming a mac)

- [ ] Setup [Brew](https://brew.sh/) if you don't already have it installed.
- [ ] Install Python3

```
$ brew install Python
```

- [ ] [Virtual Environment for Python](https://virtualenv.pypa.io/en/latest/installation/)
- [ ] Clone this repository and then just copy individual files locally to the new directory and push to your own github account (don't fork as we don't want others to copy your solution). Make sure you copy the .gitignore hidden file.

## Check everything is good to go...

- [ ] Change to the directory of your new copy.
- [ ] Activate the virtual environment.

```
$ virtualenv env -p python3
$ source ./bin/env/activate
```

Use pip to install the required python modules (tweepy)

```
$ pip install -r requirements.txt
```

Running python --version should now return version 3.7 (or similar)

```
$ python --version
Python 3.7.1
```

Now run main.py

```
$ python main.py
Hello World!
```

If you've got here, you now have an isolated Python environment that's setup correctly and good to go!

If you want to get out of the virtual environment, just type:

```
$ deactivate
```

## Preparing Twitter

1. Setup a Twitter App.

You'll need a Twitter account and create a Twitter app go to [developer.twitter.com](https://developer.twitter.com/en/apps)

2. Create a file in your project directory called keys.json, copy the following json code and fill in the values the information from the new Twitter App.

```
{"CONSUMER_KEY" : "YOUR_CONSUMER_KEY",
"CONSUMER_SECRET" : "YOUR_CONSUMER_SECRET",
"ACCESS_TOKEN" : "YOUR_ACCESS_TOKEN",
"ACCESS_SECRET" : "YOUR_ACCESS_SECRET"}
```

3. In the main.py, uncomment the following lines:
```
#with open('keys.json') as f:
#    data = json.load(f)

# Setup the authentication
#auth = tweepy.OAuthHandler(data["CONSUMER_KEY"], data["CONSUMER_SECRET"])
#auth.set_access_token(data["ACCESS_TOKEN"], data["ACCESS_SECRET"])

# Create an authenticated connection to the Twitter API using Tweepy
#api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
```
Run main.py again, you should have no errors (will see Hello World! again).  You're authenticating to twitter now.

4. Now uncomment the following two lines in the do_something function.

```
#    statuses = api.user_timeline(screen_name='timbull')
#    print(statuses)
```
Comment out (or delete) the following from the do_something function.

```
print('Hello World!')
```
If everything is set up correctly, you'll now get a print of twitter.com/timbull last 20 tweets.

# The assignment

You'll be working with the Twitter Statuses endpoint, [documented here](https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html) to extract and process tweets from NFL teams.

## General expectations
The expectations of the assignment are:
1. Well commented code. Explain your thinking as needed and what you're doing.
2. Well structured code. Use clear variable names and good use of functions.
3. You MUST include at least one [module](https://docs.python.org/3/reference/import.html) you create from a sub-directory (to demo code organization). It should contain some of your code and functions. Ideally this will contain a [python class](https://docs.python.org/3/tutorial/classes.html) you use to manage Tweepy (consider moving the Tweepy initialization into the __init__ of the class and pass the various KEYS to the class when you use it).
4. You're free to rename functions etc. (in fact it's encouraged).  
5. There should be some basic error handling. In particular, handle an error for bad keys or a failed call to Tweepy (failed network condition perhaps or just twitter derping out). What happens if you run with your network (wifi) turned off?

## Task
1. Using the NFL list at the top of main (feel free to move this list to another module if you like), you should
  * Iterate through all the teams and fetch the last 20 (should be the default) tweets from each team.
2. Each tweet contains a lot of data. Extract from the JSON just the following from each of these tweets:
  * Tweet ID
  * Name of the team.
  * Date and time of the tweet formatted to PST.
  * The JSON MAY contain a [Twitter Media object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/entities-object#media). If it does contain a media object, I'd like to know the TYPE of the media (photo, video etc.)
  * The text of the tweet (watch out for emoji's)
3. Write our a CSV file call results.csv which contains the information from 2 in a CSV format (I should be able to load this into Google Sheets and see the list of Tweets extracted)
