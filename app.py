from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for, send_file, session
import os

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
#actuall gamre realated things
@app.route('/games')
def games():

    import os
    games_dir = os.path.join(os.path.dirname(__file__), 'games')
    games_list = [name for name in os.listdir(games_dir) if os.path.isdir(os.path.join(games_dir, name))]
    return jsonify(games_list)
@app.route('/games/<path:game_name>/')
def game_page(game_name):
    # Serve the game's index.html as a static file
    # Optionally, you can inject a base URL for dependencies
    return send_from_directory(os.path.join('games', game_name), 'index.html')

# Serve game dependencies, e.g. /games/<game_name>/<path:dep_path>
@app.route('/games/<path:game_name>/<path:dep_path>')
def game_dependency(game_name, dep_path):
    # Securely serve any dependency file from the game's folder
    return send_from_directory(os.path.join('games', game_name), dep_path)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)