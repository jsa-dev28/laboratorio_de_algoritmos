from pathlib import Path
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)
lines = contents.splitlines()
for line in lines:
    print(line)
string = ''
for line in lines:
    string += line.lstrip()
print(string.replace('Python', 'C'))