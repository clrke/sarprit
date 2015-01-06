def search(query):
	consumer_key = 'AZNFBjn5uLouEBKdbTGVcz8NJ'
	consumer_secret = 'BUi5uemYVb4XhmZjV2oOihLB8QnTbsqXD32mFozQfl5UKEU5mo'
	access_token = '2478853242-ITK4Gso8QzT04XnAg7eAUK6HJ4u64MM6SzzVi2f'
	access_token_secret = 'cNuxOZy3350diWxHFW2owaQHsz6JIfhogMQ5Enwu5T2uV'
	import tweepy

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	return api.search(q=query, rpp=20, show_user=True)
