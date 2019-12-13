import flask
import json
import requests


API_URL='http:/localhost:8000'


app = flask.Flask(__name__)
@app.route('/')

def index ():
    stats = requests.get (f'{API_URL}/api/vl/stats')
    hasil = ('data berhasil diakses')
    if stats.status_code ==200:
        stats = json.loads(stats.text)
        hasil = f'terdapat {len(stats)}data'

    return render_template('index.html' ,jumlah_stats=hasil)