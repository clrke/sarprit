Sentiment Analyzer of Philippine Restaurants Reviews in Twitter
====
This is a system developed to find the positivity and negativity of Philippine restaurants reviews that have been written in tweet form, with additional features like Subjectivity and Clues Classifications.

## Installation
Clone this repo:

    $ git clone http://github.com/arkeidolon/sarprit

And install __Python 3.4__ along with the following dependencies:
* django 1.7
* dj-static
* dj-database-url
* psycopg2
* gunicorn
* static 0.4
* wsgiref 0.1.2
* tweepy
* nltk
* numpy 1.8.1
* scipy 0.14.0
* scikit-learn 0.14.1

#### Pip install
    $ pip install -r requirements.txt

#### Windows Installers
* http://www.lfd.uci.edu/~gohlke/pythonlibs/
    
## How to use

Copy the provided database to the root folder of the project and run the server using:

    $ cd sarprit
    $ python manage.py runserver
