#!/bin/python3

import os
from flask import Flask
app = Flask(__name__)


@app.route("/hello")
def main():
    return "Hello There..."


@app.route("/")
def main():
    return "Welcome! to IUST BOOTCAMP SUMMER 2021"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
