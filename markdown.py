

"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags
"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line
def converthyphens3(line):
  line=re.sub(r'###(.*)',r'<h3>\1</h3>',line)
  return line
def converthyphens2(line):
  line=re.sub(r'##(.*)',r'<h2>\1</h2>',line)
  return line

def converthyphens(line):
  line=re.sub(r'#(.*)',r'<h1>\1</h1>',line)
  return line
    
    
    
x=0
#y=0;
#lines2=fileinput.readlines();
line_count=0;
#num_lines=sum(1 for line in (fileinput.input()))
previous_line=''
for line in fileinput.input():
  if ((('>')==line[0])):
    if (x==0):
      x=2
      print '<blockquote>'
    
  if (x==2):
    if ('>'!=line[0]):
      x=0
      line = line.rstrip() 
        
      line = convertStrong(line)
      line = convertEm(line)
      
      line=converthyphens3(line)
      line=converthyphens2(line)
      line=converthyphens(line)
      print '<p>' + line + '</p>'
      print '</blockquote>'
      continue
    #print
  if (x==2): #& ('>'==line[0])):
    line=re.sub(r'^[>](.*)',r'\1',line)
    
  
  line = line.rstrip() 
  
  line = convertStrong(line)
  line = convertEm(line)
  
  line=converthyphens3(line)
  line=converthyphens2(line)
  line=converthyphens(line)

  print '<p>' + line + '</p>',
  previous_line=line
    
    

if (x==2):
  print '</blockquote>'
