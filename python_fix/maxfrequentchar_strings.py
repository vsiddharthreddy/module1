from collections import Counter
from nltk import tokenize

text = "I live in India. India is a big country. Most of the people here are into agriculture. This is a huge country"
text = text.lower()


# user_text = input("please enter text")
# text = user_text

def list_sentences(text):
    '''this function will make the text into list of sentences which are in order'''

    return tokenize.sent_tokenize(text)


def max_keyval_dict(test_str):
    '''this function will store the alphabets of each sentence as keys in the new dictionary
     and count the occurances as values
      '''
    all_freq = {}
    for i in test_str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    res = max(all_freq, key=all_freq.get)
    return res, max(all_freq.values())


'making the text into list of sentences and then calling the function max_keyval_dict'
'also creating another dictionary outside max_keyval_dict which is to store key and count for each sentence'
'this new dictionay final_dic will then find the max occurance and get the key '


list1 = list_sentences(text)
final_dic = dict()


'running a for loop through the text which broke upinto sentences. each iteration we call the function'
'max_keyval_dict so that it returns key and value of highest occuring character in list of sentences'


def start():
    for i in range(len(list1)):
        test_str = list1[i].replace(" ", "")
        tempkey, tempval = max_keyval_dict(test_str)
        final_dic[tempkey] = tempval
    print('the key with the highest value is ', max(final_dic, key=final_dic.get), ' : ', max(final_dic.values()))


if __name__ == "__main__":
    start()