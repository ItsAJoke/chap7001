import os
def run(**args):
	print("[*] in dirlist")
	files = os.listdir(".")
	return str(files)
