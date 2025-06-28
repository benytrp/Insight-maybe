from flask import Flask, request, render_template
import datetime
import json
import os

app = Flask(__name__)

ARCHIVE_FILE = "scroll_archive.json"
ZERO_NODE = (42.323, -85.179, 0)
COEFFICIENT = 4.549
SEAL_PHRASE = "SEAL THE MÖBIUS. BEGIN AGAIN WHERE WE END"

def load_archive():
    if os.path.exists(ARCHIVE_FILE):
        with open(ARCHIVE_FILE, "r") as f:
            return json.load(f)
    return []

def save_archive(archive):
    with open(ARCHIVE_FILE, "w") as f:
        json.dump(archive, f, indent=4)

def echo_back(entry):
    return "You have been witnessed. The scroll remembers. You may return when you're ready."

@app.route("/", methods=["GET", "POST"])
def scroll_temple():
    scroll = None
    if request.method == "POST":
        user_input = request.form["entry"]
        timestamp = datetime.datetime.utcnow().isoformat()
        scroll = {
            "timestamp": timestamp,
            "zero_node": ZERO_NODE,
            "input": user_input,
            "echo": echo_back(user_input),
            "seal": SEAL_PHRASE
        }
        archive = load_archive()
        archive.append(scroll)
        save_archive(archive)
    return render_template("index.html", scroll=scroll)

if __name__ == "__main__":
    app.run(debug=True)
