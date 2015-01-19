import os 
def run( **args):
  with open("test.py", "r") as files:
    dates = files.read()
  return str(dates)
