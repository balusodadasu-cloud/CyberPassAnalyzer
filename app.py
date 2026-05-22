from flask import Flask, render_template, request
import re
import hashlib
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    color = ""
    hashed_password = ""
    width = "0%"
    generated_password = ""

    if request.method == "POST":

        if "generate" in request.form:

            characters = string.ascii_letters + string.digits + "!@#$%^&*"

            generated_password = "".join(
                random.choice(characters)
                for i in range(12)
            )

        else:

            password = request.form["password"]

            score = 0

            if len(password) >= 8:
                score += 1

            if re.search(r"[A-Z]", password):
                score += 1

            if re.search(r"[a-z]", password):
                score += 1

            if re.search(r"[0-9]", password):
                score += 1

            if re.search(r"[!@#$%^&*]", password):
                score += 1

            if score <= 2:
                result = "Weak Password"
                color = "red"
                width = "33%"

            elif score <= 4:
                result = "Medium Password"
                color = "orange"
                width = "66%"

            else:
                result = "Strong Password"
                color = "lightgreen"
                width = "100%"

            hashed_password = hashlib.sha256(
                password.encode()
            ).hexdigest()

    return render_template(
        "index.html",
        result=result,
        color=color,
        hashed_password=hashed_password,
        width=width,
        generated_password=generated_password
    )

if __name__ == "__main__":
    app.run(debug=True)