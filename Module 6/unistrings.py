import unicodedata as ud

def get_by_name(value):
    name = ud.name(value)
    return(ud.lookup(name),name)