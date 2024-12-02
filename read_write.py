import os
fout = open('output.txt', 'w')
line1 = "This here's the wattle, \n"

line2 = "the emblem of our land. \n"

x = 53
cwd = os.getcwd()
abso = os.path.abspath('output.txt')
walk = os.walk()

fout.write(line1)
fout.write(line2)
fout.write(str(x))
fout.write('\n')
fout.write(cwd)
fout.write('\n')
fout.write(abso)
print(list(walk))