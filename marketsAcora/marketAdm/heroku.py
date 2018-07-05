"""Heroku settings for production."""

import os

from .base import *  # noqa

DEBUG = False

MIDDLEWARE += [ # noqa: W0401
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASES = {
    'default': db_from_env
}