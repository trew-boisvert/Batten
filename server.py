from flask import Flask, render_template, jsonify, session, request

app = Flask(__name__)

app.secret_key = "damngoodmarmalade"

@app.route("/")
def homepage():
    """Simple greeting page."""
    
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)