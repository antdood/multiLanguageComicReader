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
	eng_pages = os.listdir(f"{BASE_DIR}/static/manhwas/eng/{manhwa_name}")
	kor_pages = os.listdir(f"{BASE_DIR}/static/manhwas/kor/{manhwa_name}")
	return render_template(f'manhwa.html', eng_pages = eng_pages, kor_pages = kor_pages, manhwa_name = manhwa_name)
