import urllib
f = urllib.urlopen('http://www.exercicioonline.com')

for line in f:
  print line.strip()
