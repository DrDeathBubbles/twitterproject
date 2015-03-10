import tweepy
import shelve



def main():
	keys = shelve.open('key.txt')
	auth = tweepy.OAuthHandler(keys['consumer_key'],keys['consumer_secret'])
	auth.secure = True
	auth.set_access_token(keys['access_token'],keys['access_secret'])	
	api = tweepy.API(auth)

	# If the authentication was successful, you should
	# see the name of the account print out
	print(api.me().name)


	return api 

if __name__ == '__main__':
	main()
