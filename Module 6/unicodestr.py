char = '\u1E03'
charname = '\N{LATIN SMALL LETTER B WITH DOT BELOW}'

#print(char + " " + charname)

import unicodedata

#print(unicodedata.name("a"))
#print(unicodedata.lookup(unicodedata.name("a")))



"""##encode to bytes
my_str = "hello".encode("utf-8")
print(my_str)
print(my_str.decode("utf-8"))

french_str = "mang\u00e9"
print(french_str.encode("utf-8"))
print(french_str)

###
laugh = '\U0001F602'
print(laugh)
print(len(laugh))
print(laugh.encode('utf-8'))
print(len(laugh.encode('utf-8')))

print("Ignore: ",laugh.encode('ascii','ignore'))
print("Replace: ",laugh.encode("ascii","replace"))

emoji_combo = '\U0001F602 and \U0001F923'
print(emoji_combo)
print("Ignore: ",emoji_combo.encode('ascii','ignore'))
print("Replace: ",emoji_combo.encode("ascii","replace"))"""

import html

print(html.unescape('e&#769'))

print(html.escape("Hello><$"))

######Normalization
my_accent = chr(233)
my_accent2 = '\u00e9'
my_accent3 = html.unescape('e&#769')
my_accent4 = html.unescape('&#233')
print(my_accent,my_accent2,my_accent3,my_accent4)

print(my_accent == my_accent2)
print(my_accent2 == my_accent3)
print(my_accent2 == my_accent4)