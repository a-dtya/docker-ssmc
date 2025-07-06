from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from container-dev1 made change"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

    
