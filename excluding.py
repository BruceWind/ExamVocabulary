
word_list1 = set()
word_list2 = set()



# reading the first file that has less words.
with open('CET4.txt', 'r') as f1:
  for line in f1:
        word = line.split()[0].strip()
        word_list1.add(word)

# reading the 2nd file that has more words than the first.
with open('TOEFL_excluded_IELTS.txt', 'r') as f2:
    for line in f2:
        word = line.split()[0].strip()
        word = word.replace("*", "") 
        word_list2.add(word)

# to remove duplicated words. and then write into file excluded.txt.
word_list2 = word_list2 - word_list1
with open('excluded.txt', 'w') as f3:
    for word in word_list2:
        f3.write(word + '\n')
