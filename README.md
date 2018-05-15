# Movie Sentiment Aggregator

## Set-Up
Run:
	pip install -r requirements.txt

## Sources
* Box Office Mojo: http://www.boxofficemojo.com/
* BoxOffice Pro: https://pro.boxoffice.com/
* Rotten Tomatoes: https://www.rottentomatoes.com/
* The Movie Database (TMDb): https://www.themoviedb.org/

## Accessing EC2 Instance
ssh -i twitter/tweet_listener.pem ec2-user@ec2-18-191-87-151.us-east-2.compute.amazonaws.com

scp -i twitter/tweet_listener.pem twitter/tweet_listener.py ec2-user@ec2-18-191-87-151.us-east-2.compute.amazonaws.com:tweet_listener.py