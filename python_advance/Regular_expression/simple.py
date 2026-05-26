import re
a="I am not selected to the company yet Kindly help me to get selected"
# print(re.search("help",a))   #<re.Match object; span=(44, 48), match='help'>
# print(re.search("helps",a))  #None
print(re.findall("selected",a))  #['selected', 'selected']
print(re.findall('ii',a))  #[]


print(re.sub("help","please help",a))  #I am not selected to the company yet Kindly please help me to get selected