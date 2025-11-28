from flask import Flask

app = Flask(__name__)

@app.route("/")   # This is the home page
def home():
    return "Home page!"

@app.route("/about")  # This is the about page
def about():
    return "About page!"

if __name__ == "__main__":
    app.run(debug=True)
