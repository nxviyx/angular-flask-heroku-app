
from flask import Flask,render_template, request, jsonify
from flask_compress import Compress

# initialize flask application
app = Flask(__name__)
Compress(app)

@app.route('/')
def test():
    return render_template("index.html")

# @app.route('/')
# def root():
#     return app.send_static_file('index.html')

@app.route('/flask/hello')
def testing():
  return "Hellow from heroku"

if __name__ == '__main__':
    # run web server
    app.run()

