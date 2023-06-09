from PyDictionary import PyDictionary
dictionary = PyDictionary()

def get_word_meaning(word):
    """
    使用PyDictionary库获取单词的中文释义
    """
    meanings = dictionary.meaning(word)

    if meanings:
        # 取第一个释义作为中文释义
        return meanings[list(meanings.keys())[0]][0]
    else:
        return "未找到该单词的中文释义"


word = "apple"

meaning = get_word_meaning(word)



word_list = set()
# reading the first file that has less words.
with open('IELTS_excluded_TOEFL.txt', 'r') as f1:
  for line in f1:
        word = line.split()[0].strip()
        word_list.add(word)

num = 0
## this step is slow.
with open('IELTS_excluded_TOEFL_meant.txt', 'w') as f3:
    for word in word_list:
        f3.write(word + ':  ' + get_word_meaning(word) +'\n')
        num+=1
        if num % 5 == 0:
          print("Translation with index: %d." % num)



