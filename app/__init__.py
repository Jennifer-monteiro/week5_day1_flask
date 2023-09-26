from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index_html():
    return render_template('index.html')


@app.route('/favorite5')
def favorite5():
    headings = ("FOOD", "BOOKS", "TRAVEL", "WHALES", "MOVIES")
    data = (
    ("Pizza", "Paradise","Scotland","Orcas","5 meters above the sky"),
    ("Pasta","The alchemist","Norway","Whale SHark","Matrix"),
    ("Steak","Harry Potter","Netherlands","Blue Whale","Harry Potter"),
    ("Steak again","Pride and Prejudice","Brazil","Humpback Whale","Pride and Prejudice"),
    ("Cheesesteak","To kill a mockinbird","Canada","Sperm Whale","The Great Gatsby")
    )
    return render_template('favorite5.html', headings = headings, data = data)

@app.route('/login')
def login_html():
    return render_template('login.html')