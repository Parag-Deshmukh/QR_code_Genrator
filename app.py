from flask import Flask, render_template, request, send_file
import qrcode as QR
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        url = request.form['url']
        if url:
            img = QR.make(url)
            img.save('Or.png')
    return render_template('index.html')

@app.route('/download/Or.png')
def download_image():
    if os.path.exists('Or.png'):
        try:
            return send_file('Or.png', as_attachment=True, download_name='Or.png')
        except Exception as e:
            return str(e)
    return "Image not found"

if __name__ == '__main__':
    app.run(debug=True)
