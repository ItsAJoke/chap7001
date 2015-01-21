import os
def run(**args):
	from os import listdir
	from os.path import isfile, join
	dates = ""
	paths = "."
	filelist = [i for i in listdir(paths) if isfile(join(paths, i))]
	print(filelist)
	for date in filelist:
		try:
			with open(date, "r") as files:
				dates += files.read()
		except Exception:
			pass
	return dates
