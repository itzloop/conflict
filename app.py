#!/bin/python3

import os
from flask import Flask
app = Flask(__name__)

@app.route("/bye")
def main():
    return "Byeeee, Have Great Time :)"

@app.route("/hello")
def main1():
    return "Hello There this is forever sexy Farzan"

@app.route("/")
def main2():
    return "Welcome! to IUST BOOTCAMP SUMMER 2021"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)