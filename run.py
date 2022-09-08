from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

GENERATORDB = 'characterGenerator.db'

@app.route('/')
def index():
    db = sqlite3.connect(GENERATORDB)
    print(db)

    selectedRace = []
    selectedClass = []
    selectedBackground = []
    selectedRaceDesc = []
    selectedClassDesc = []
    randomRace = db.execute('SELECT raceName, raceDesc FROM races ORDER BY RANDOM() LIMIT 1')
    for race in randomRace:
        selectedRace.append(list(race))
    randomClass = db.execute('SELECT className, classDesc FROM classes ORDER BY RANDOM() LIMIT 1')
    for rClass in randomClass:
        selectedClass.append(list(rClass))
    randomBackground = db.execute('SELECT backgroundName FROM backgrounds ORDER BY RANDOM() LIMIT 1')
    for background in randomBackground:
        selectedBackground.append(list(background))


    db.close()
    return render_template('index.html', selectedRace=selectedRace, selectedClass=selectedClass, selectedBackground=selectedBackground)
