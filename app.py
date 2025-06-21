from flask import Flask, render_template
import os

'''
RVC GUI by Tiger14n at https://github.com/Tiger14n/RVC-GUI
The Weeknd (RVC) 1000 Epochs by clubbedsam#4419 at https://docs.google.com/spreadsheets/d/1leF7_c2Qf5iQRVkmOF51ZSynOvEjz8fHqwriX1wUMPw/edit#gid=1227575351
AudioSet by Google at https://research.google.com/audioset/download.html
'''

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))