@app.route('/')
def main():
    return "manhwas_list"


@app.route('/manhwas/<manhwa_name>')
def show_manhwa(manhwa_name):
    return '{manhwa_name}'