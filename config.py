DEBUG = True
#DATABASE_URI = 'sqlite:///test.db'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
DATABASE_URI = 'postgres://test:test@localhost:5432/ieddit'
SQLALCHEMY_DATABASE_URI = 'postgres://test:test@localhost:5432/ieddit'
# This will be unique every time create_db.py is ran when testing
# to force clear sessions
SECRET_KEY = 'not-a-real-key-|r|BICcM1fQS3|r|'
URL = 'http://dev.ieddit.com'
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SESSION_COOKIE_SAMESITE='Lax'
CACHE_TYPE = 'simple'
RATE_LIMIT = False
RATE_LIMIT_TIME = 5
LIMITER_DEFAULTS = ['600 per minute']
CAPTCHA_ENABLE = False
CAPTCHA_NUMERIC_DIGITS = 8
SESSION_TYPE = 'sqlalchemy'
USE_PROXIES = True
with open('proxies.txt', 'r') as p:
	proxy = p.read().strip()
	PROXIES = {'http':'http://' + proxy, 'https':'https://' + proxy}
PHEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}