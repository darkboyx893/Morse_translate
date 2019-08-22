import tweepy
import time

#must create a twitter dev account to get key- https://developer.twitter.com/
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#insert username in string
username = ''
user = api.get_user(username)
#username of user you would like to get tweet from
tweet_username = ''
tweet = api.user_timeline(tweet_username)


try:
     list_tweets =[]
     for tweets in tweet:
         list_tweets.append(tweets.text)
#depending on text editor/complier program will crash due to certain characters not being read in program like emojis or different characters
         
except UnicodeEncodeError as e:
    print('an error has occured: ' + e)

finally:
    #checks if a new tweet is put out by storing old tweet and checking for a new tweet every minute
    def check_new_tweet():
        old_tweet= []
        for old in tweet:
            old_tweet.append(old.text)
        while True:
            time.sleep(60)
            new_tweets = api.user_timeline(tweet_username)
            new_tweet = []
            for new in new_tweets:
                new_tweet.append(new.text)
            if new_tweet[0] != old_tweet[0]:
                print(new_tweet[0])
                print(old_tweet[0])
                print('There is a new tweet! ')
                return new_tweet[0]
                break
            elif new_tweet[0] == old_tweet[0]:
                print(new_tweet[0])
                print(old_tweet[0])
                print('No new tweet... ')
                continue
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '0','1', '2', '3', '4','5', '6', '7', '8', '9', '.', ',' ,'?', ';', ':', '/', '-', '\'', '(', ')', '_', '@', '!', '&', '=', '+', '"', '$']
    morse_alphabet =['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ', '-----','.----', '..---', '...--', '....-','.....', '-.....', '--...', '---..', '----.', '.-.-.-', '--..--' ,'..--..', '-.-.-', '---...', '-..-.', '-....-', '.----.', '-.--.', '-.--.-', '..--.-', '.--.-.', '-.-.--', '.-...', '-...-', '.-.-.', '.-..-.', '...-..-']
    #takes in sentence as string and converts the list  of letters with indexes of location in alphabet then used to search in morse_alphabet for equivalence
    def translator(sentence):
        list_sentence = list(sentence.upper())
        indexes = []
        illegal_characters = []
        count = -1
        for letters in list_sentence:
            try:
                indexes.append(alphabet.index(letters))
            except ValueError:
                if letters not in alphabet:
                    count += 1
                    illegal_characters.append(letters)
                
        morse_sentence = []
        for numbers in indexes:
            morse_sentence.append(morse_alphabet[numbers])
#leaves an extra space for readability in morse code
        translated = ' '.join(morse_sentence)
        return translated

#morsified_split ensures there is not a run over in character limit to increase or decrease limit change the numbers to desired character limit; twitter limit currently is 259 so each morsefied is split at length 255; to add more or add less change the number in morsified_split
     #also waits 30 seconds to post in between each morsified_split
while True:
    try:
        moresified = translator(check_new_tweet())
        moresified_split = [moresified[i:i+255] for i in range(0, len(moresified), 255)]
        for words in moresified_split:
            print(words)
            time.sleep(30)
            api.update_status(words)
        print(check_new_tweet())
    except Exception as e:
        print(e)
        continue


