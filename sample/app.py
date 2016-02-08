#!/bin/env python2
# -*- coding: utf-8 -*-

from sample import app


@app.route("/", methods=["GET"])
def index():
    return "This is a test"
