from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    with open("MainPage.html") as f:
        html = f.read()
    return html
    
if __name__ =='__main__':
    app.run(host="0.0.0.0")