def spam():
  import re
  hand = open('mbox-short.txt')
  numlist = list()
  for line in hand:
    line = line.rstrip()
    stuff = re.findall('-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
  print "Maximum: ", max(numlist)

if __name__ == '__main__':
  spam()
