from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

if __name__ == "__main__":
    app.run()

venv/bin/pip3 freeze > requirements.txt
venv/bin/pip3 install -r requirements.txt