# 'split', 'rsplit', 'lsplit', 'splitlines' use

text = "Hello, my name is monsur biolob.\n I'm 30 years old."

print(text.split())  # space
print(text.split(','))
print(text.rsplit(','))
print(text.splitlines(True))
print(text.splitlines(False))