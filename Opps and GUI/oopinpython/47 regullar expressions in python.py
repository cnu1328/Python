import re
print(dir())

line = 'Cats are more smarter than dogs'

matchobj = re.match('dogs',line,re.M|re.I)

if matchobj :
    print('match --> matchobj.group() : ' , matchobj.group())
else:
    print('NO match found in match function')

searchobj = re.search('dogs',line,re.M|re.I)
if searchobj  :
    print('search --> searchobj.group() : ' , searchobj.group())
else:
    print('Nothing found in search function')


phone = '2020-123-840 # This is phone number'

num = re.sub(r'#.*$',"",phone)

print('phone Num : ' , num)

num = re.sub(r'\D','',phone)

print('phone Num : ',num)

import re

line = 'Cats are smarter than dogs'

searchobj = re.search('(.*) are (.*?) .*',line,re.M|re.I)

if searchobj :
    print('searchobj.group() : ', searchobj.group())
    print('searchobj.grops() : ', searchobj.groups())
    print('searchobj.gropus() : ', searchobj.group(1))
    print('searchobj.gropus() : ', searchobj.group(2))
    print('searchobj.gropus() : ', searchobj.group(1))

else:
    print('Nothing Found..!')



import re

text = 'abaaabaaaabaaaaaa'

pattern = 'ab'

for match in re.findall(pattern,text):
    print('found {}'.format(match))

for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print('found %s at %d : %d'%(match.group(),s,e))



#Regular expressions in python

import re

str = 'I\'m very good person'

obj = re.match('go',str,re.M|re.I)

if obj :
    print('match function : ' ,obj.group())
else:
    print('Nothing Found')









































    
