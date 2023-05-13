from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask of pypy!'


app.run(host='0.0.0.0', port=80000)

if __name__=="__main__" :
   app.rn(debug=True)

