import re

m_characters = 'abcde12345?!_@* \t\n'

"""print(re.findall('\d',m_characters))
print(re.findall('\w',m_characters))
print(re.findall('\s',m_characters))
print(re.findall('\W',m_characters))
print(re.findall('\S',m_characters))"""

print(re.findall('\d|\W',m_characters))

#match the start of string
print(re.findall("^\d",m_characters))
print(re.findall("^a",m_characters))

#end of string
print(re.findall("\t\n$",m_characters))

