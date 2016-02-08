#!/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

__version__ = "0.0.1"

from sample.app import *
