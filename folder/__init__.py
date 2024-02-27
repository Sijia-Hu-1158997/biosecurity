from flask import Flask
from flask import render_template


app = Flask(__name__)

from folder import adminview
from folder import staffview
from folder import apiaristview