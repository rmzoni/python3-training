# Splitting Strings on Any of Multiple Delimiters
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))

# Matching Text at the Start or End of a String
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

# Matching Strings Using Shell Wildcard Patterns
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# Matching and Searching for Text Patterns
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)

# Searching and Replacing Text
print(text.replace('yeah', 'yep'))
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))

# Sanatize Data
import unicodedata
a = 'pýtĥöñ is awesome\n'
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))

# Aligning Text Strings
print(text.ljust(20))
print(text.rjust(20,'='))
print(text.center(20,'*'))

# Combining and Concatenating Strings
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))