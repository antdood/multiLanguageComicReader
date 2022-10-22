from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def main():
	return 'manhwas_list'

@app.route('/manhwas/<manhwa_name>')
def show_manhwa(manhwa_name):
	pages = os.listdir(f"/home/kaede/multiLanguageComicReader/manhwas/{manhwa_name}")
	return flask.render_template('manhwa.html', pages = pages)