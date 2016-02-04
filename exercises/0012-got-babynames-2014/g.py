from os.path import join
import string

dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

f_dict = {}
m_dict = {}

for line in open(bname):
    name, sex, babies = line.strip().split(',')
    letter = name[-1]
    if sex == 'F':
        if f_dict.get(letter):
            f_dict[letter] += int(babies)
        else:
            f_dict[letter] = int(babies)
    if sex == 'M':
        if m_dict.get(letter):
            m_dict[letter] += int(babies)
        else:
            m_dict[letter] = int(babies)

print((str('letter').ljust(8)), (str('F').rjust(8)), (str('M').rjust(8)))
print('--------------------------')
for letter in string.ascii_lowercase:
    fem = f_dict.get(letter)
    mal = m_dict.get(letter)
    print((str(letter).ljust(8)), (str(fem).rjust(8)), (str(mal).rjust(8)))