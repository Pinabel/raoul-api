from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
 return 'Hello, Raoul is alive!'

@app.route('/raoul')
def raoul():
 return 'Raoul balance sa punchline : "T’as cru que j’étais un bot lambda ?"'

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
