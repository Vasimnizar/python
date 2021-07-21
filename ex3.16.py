f = open("test.txt", "r")

txt= ""
for line in f:
  stripped_line = line.rstrip()
  txt += stripped_line
f.close()

print(txt)
