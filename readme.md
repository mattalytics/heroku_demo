**Install Heroku**

https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Do you have an older version installed? Type `which heroku` to find and delete it.

**Get Code**

cd to your code directory

https://github.com/mattalytics/heroku_demo

`git clone https://github.com/coding-boot-camp/heroku-bot`

`cd heroku_bot`

`conda create -n herokuapi python=3.4`

`source activate herokuapi`

`heroku login`

`heroku create`

**Set Env Variables**

heroku config:set consumer_key=

heroku config:set consumer_secret=

heroku config:set access_token=

heroku config:set access_token_secret=

Make some edits to file to print out a few lines

`git push heroku master`

`heroku ps:scale worker=1`

`heroku logs`

If you see your print statements in the logs, it worked!

**OPTIONAL - Create an API Server**

`pip install gunicorn flask tweepy`

add `app.py`

add line to procfile: `web: gunicorn app:app --log-file=-`

`pip freeze > requirements.txt`

commit your changes and push

`heroku ps:scale web=1`

voila, an extremely basic api accessible to all
