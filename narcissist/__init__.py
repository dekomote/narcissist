# -*- coding: utf-8 -*-

"""
narcissist
----------

Set up the narcissist module. We only need the app.

"""

import os

if not os.environ.get("NARCISSIST_SETTINGS"):
    os.environ["NARCISSIST_SETTINGS"] = 'project_template/settings.py'

from .main import app

