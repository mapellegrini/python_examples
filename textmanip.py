#!/usr/bin/python

def getline(substr, text):
  point = text.find(substr)
  if (point == -1):
    return ""
  left = text.rfind("\n", 0, point) + 1
  right = text.find("\n", point)
  if (right == -1):
    right = len(text)
  return text[left:right]


def width(mystr, length):
  if (len(mystr) >= length):
    return mystr[0:length]
  else:
    retstr = mystr
    while (len(retstr) < length):
      retstr += " "
    return retstr



longline='''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 
'''

print getline("voluptate", longline)

print width(longline, 20)
print width("Hello", 20)


