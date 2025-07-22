from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for, send_file, session


app = Flask(__name__)

def portal():
    return render_template('index.html')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(f'files/{filename}', as_attachment=True)
# Android captive check
@app.route("/generate_204")
def android_check():
    return portal(), 200

# Windows captive check
@app.route("/ncsi.txt")
def windows_ncsi_check():
    return "Microsoft NCSI"
@app.route("/connecttest.txt")
def windows_check():
    return portal(), 200

# Apple captive check
@app.route("/hotspot-detect.html")
@app.route("/library/test/success.html")
@app.route("/success.html")
def apple_check():
    return portal(), 200
@app.route("/redirect")
def msft_redirect():
    return portal(), 200

#version and admin control/information
@app.route('/chrome-variations/seed')
def machine_info():
    os = request.args.get('osname', '').strip('/')
    channel = request.args.get('channel', '').strip('/')
    chrome_ver = request.args.get('chrome_ver', '').strip('/')
    return "", 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)