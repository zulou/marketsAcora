"""Heroku settings for production."""

import os

from .base import *  # noqa

DEBUG = False

MIDDLEWARE += [ # noqa: W0401
    'whitenoise.middleware.WhiteNoiseMiddleware'
]
