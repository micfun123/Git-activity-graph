from flask import Flask, stream_with_context
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
    # Save the image to a byte buffer
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    # Return the image as a stream with a content-type header
    return app.response_class(stream_with_context(img_io), mimetype='image/png')





if __name__ == '__main__':
    app.run(debug=True)