from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

GENERATORDB = 'characterGenerator.db'

@app.route('/')
def index():
    db = sqlite3.connect(GENERATORDB)
    print(db)

    selectedRace = db.execute('SELECT raceName FROM races ORDER BY RANDOM() LIMIT 1')
    selectedClass = db.execute('SELECT className FROM classes ORDER BY RANDOM() LIMIT 1')
    selectedBackground = db.execute('SELECT backgroundName FROM backgrounds ORDER BY RANDOM() LIMIT 1')


    db.close()
    return render_template('index.html', disclaimer='may contain traces of nuts', selectedRace=selectedRace, selectedClass=selectedClass, selectedBackground=selectedBackground)
