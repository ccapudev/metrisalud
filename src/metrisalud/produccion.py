from .settings import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dlildqdj',
        'USER': 'dlildqdj',
        'PASSWORD': 'iQknH28ZDN5EpknnKToP2qfUdQ9UxdDr',
        'HOST': 'stampy.db.elephantsql.com',
        'PORT': '',
        # 'URL': 'postgres://gjdctids:zWBbB0cHJIxiDA-pGTBK2F_TgI8-unOF@stampy.db.elephantsql.com:5432/gjdctids',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}