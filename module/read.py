import os
def run(**args):
  print("[*] in read module")
  file = "test.py"
  dates = file.read()
  return dates
