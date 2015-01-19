import os 
def run( **args):
  with open("test.py", "r") as files:
    dates = files.read()
  retrun str(dates)
