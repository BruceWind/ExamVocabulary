
word_list1 = set()
word_list2 = set()

with open('CET.txt', 'r') as f1:
  for line in f1:
        word = line.split()[0].strip()
        word_list1.add(word)


with open('IELTS_8000.txt', 'r') as f2:
    for line in f2:
        word = line.split()[0].strip()
        word_list2.add(word)

word_list2 = word_list2 - word_list1
with open('excluded.txt', 'w') as f3:
    for word in word_list2:
        f3.write(word + '\n')
