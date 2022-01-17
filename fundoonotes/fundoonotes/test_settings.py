from .settings import *

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': BASE_DIR / 'db.postgresql_psycopg2',
    }
}
EMAIL_BACKEND = 'django.core.mail.backends.locmem.Emailbackend'

