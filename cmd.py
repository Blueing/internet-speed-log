import subprocess

def run(command):
		proccess = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		return proccess.stdout.read()
