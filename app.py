from flask import Flask
from gengraph import generate_activity_graph
import io

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

#create a api route to return a image for github acctivity graph
@app.route('/github-graph/<username>')
def github_graph(username):
    #get the image from github
    return 'Hello, world!'

@app.route('/gitlab-graph/<username>')
def gitlab_graph(username):
    return 'Hello, world!'
