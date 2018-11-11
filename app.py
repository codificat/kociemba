#!/usr/bin/env python

from kociemba import solve
from flask import Flask

application = Flask(__name__)

@application.route('/solve/<cubestring>')
def process(cubestring):
    result = solve(cubestring)
    return result

if __name__ == "__main__":
    application.run()
