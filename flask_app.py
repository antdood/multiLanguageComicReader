from flask import Flask
from flask import render_template
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def main():
	return 'manhwas_list'

@app.route('/manhwas/<manhwa_name>')
def show_manhwa(manhwa_name):
	pages = os.listdir(f"{BASE_DIR}/static/manhwas/{manhwa_name}")
	return render_template(f'manhwa.html', pages = pages, manhwa_name = manhwa_name)
