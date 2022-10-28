from flask import Flask
from flask import render_template
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def main():
	manhwa_list = os.listdir(f"{BASE_DIR}/static/manhwas")
	return render_template(f'main.html', manhwa_list = manhwa_list)

@app.route('/manhwas/<manhwa_name>')
def show_chapters(manhwa_name):
	chapter_list = os.listdir(f"{BASE_DIR}/static/manhwas/{manhwa_name}")
	return render_template(f'chapters.html', chapter_list = chapter_list, manhwa_name = manhwa_name)

@app.route('/manhwas/<manhwa_name>/<chapter_name>')
def show_chapter(manhwa_name, chapter_name):
	eng_pages = os.listdir(f"{BASE_DIR}/static/manhwas/{manhwa_name}/{chapter_name}/eng")
	kor_pages = os.listdir(f"{BASE_DIR}/static/manhwas/{manhwa_name}/{chapter_name}/kor")
	return render_template(f'manhwa.html', eng_pages = eng_pages, kor_pages = kor_pages, manhwa_name = manhwa_name, chapter_name = chapter_name)
