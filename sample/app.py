#!/bin/env python2
# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "This is a test"


def main():
    app.run()
