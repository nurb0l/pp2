#task 1
import re

def a_or_ab(txt):
    patt = "(^ab*)$"
    res = re.findall(patt, txt)
    return res

txt = str(input())
print(a_or_ab(txt))
#task 2
import re

def a_or_ab(txt):
    patt = "ab{2,3}"
    res = re.findall(patt, txt)
    return res
    
txt = str(input())
print(a_or_ab(txt))
#task 3
import re

def a_b(txt):
    patt = "^[a-z]+_[a-z]+$"
    res = re.findall(patt, txt)
    return res
    
txt = str(input())
print(a_b(txt))

#task 4
import re

def a_b(txt):
    patt = "^[A-Z][a-z]+$"
    res = re.findall(patt, txt)
    return res
    
txt = str(input())
print(a_b(txt))
#task 5
import re

def a_b(txt):
    patt = "^a.*b$"
    res = re.findall(patt, txt)
    return res
    
txt = str(input())
print(a_b(txt))
#task 6
import re

def a_b(txt):
    
    res = re.sub("[ .,]", ":" , txt)
    return res
    
txt = str(input())
print(a_b(txt))
#task 7
def snake_to_camel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))
#task 8
import re
def split_by_upper(txt):
    return re.findall("[A-Z][^A-Z]*", txt)
txt=str(input())
print(split_by_upper(txt))
#task 9
import re

def space_between_capital(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

txt=str(input())

print(space_between_capital(txt))
#task 10
def camel_to_snake(txt):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',re.sub('([A-Z]+)', r' \1',txt.replace('-', ' '))).split()).lower()

