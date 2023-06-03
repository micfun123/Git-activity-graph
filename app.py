from flask import Flask, send_file
from gengraph import generate_activity_graph
import io


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

#create a api route to return a image for github acctivity graph
@app.route('/github-graph/<username>')
def github_graph(username):
    # Generate the graph
    img = generate_activity_graph(username,'github')
    # Save the image to a bytes buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    # Return the image as a bytes buffer to the client
    return send_file(buf, mimetype='image/png')


#create a api route to return a image for gitlab acctivity graph
@app.route('/gitlab-graph/<username>')
def gitlab_graph(username):
    # Generate the graph
    img = generate_activity_graph(username,'gitlab')
    # Save the image to a bytes buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    # Return the image as a bytes buffer to the client
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)