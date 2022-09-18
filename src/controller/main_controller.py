from flask import render_template, jsonify
from app import app

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )