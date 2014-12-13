Sentiment Analyzer of Philippine Restaurants Reviews in Twitter
====
This is a system developed to find the positivity and negativity of Philippine restaurants reviews that have been written in tweet form.

## Installation
Clone this repo:

    $ git clone http://github.com/arkeidolon/sarprit

And install __Python 3.4__ along with the following dependencies:
* django 1.7
* numpy
* scipy
* sklearn

#### Pip install
    $ pip install django numpy scipy scikit-learn

#### Windows Installers
* http://www.lfd.uci.edu/~gohlke/pythonlibs/
    
## How to use

Sync the database and run the server:

    $ cd sarprit
    $ python manage.py syncdb
    $ python manage.py runserver
