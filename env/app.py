from flask import Flask

app = FLASK(__name__)

@app.route('/')
def index():
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)
