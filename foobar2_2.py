import random
import string
import time

def answer(names):

    score_table = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1,27)))
    word_tuplist = []

    for name in names:      # build (word, score) tuple from list of names and score table
        word_score = 0
        for chr in name:
            word_score += score_table[chr]
        word_tuplist.append((name, word_score))

    for bsort_pass in range(len(word_tuplist)-1,0,-1):  # two parm bublsort  parm1:word score/parm2:lexicographically
        for index in range(bsort_pass):
            if word_tuplist[index][1] <= word_tuplist[index+1][1]:
                if word_tuplist[index][1] < word_tuplist[index+1][1]:
                    word_tuplist[index], word_tuplist[index+1] = word_tuplist[index+1], word_tuplist[index]
                else:
                    if word_tuplist[index][0] < word_tuplist[index+1][0]:
                        word_tuplist[index], word_tuplist[index+1] = word_tuplist[index+1], word_tuplist[index]


    return [word[0] for word in word_tuplist]


def answer2(names):

    score_table = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1,27)))
    word_tuplist = []

    for name in names:      # build (word, score) tuple from list of names and score table
        word_score = 0
        for chr in name:
            word_score += score_table[chr]
        word_tuplist.append((name, word_score))


    def merge_names(mlist):

        if len(mlist) > 1:
            mid = len(mlist)//2
            left = mlist[:mid]
            right = mlist[mid:]

            merge_names(left)
            merge_names(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i][1] >= right[j][1]:
                    if left[i][1] > right[j][1]:
                        mlist[k] = left[i]
                        i += 1
                    else:
                        if left[i][0] < right[j][0]:
                            mlist[k] = left[i]
                            i += 1
                        else:
                            mlist[k] = right[j]
                            j += 1
                else:
                    mlist[k] = right[j]
                    j += 1
                k += 1
            while (i < len(left)):
                mlist[k] = left[i]
                i += 1
                k += 1
            while (j < len(right)):
                mlist[k] = right[j]
                j += 1
                k += 1
        return mlist


    merge_names(word_tuplist)

    return [word[0] for word in word_tuplist]


def answer3(names):

    score_table = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1,27)))
    word_dict = {}

    for name in names:
        word_score = 0
        for chr in name:
            word_score += score_table[chr]
        word_dict[name] = word_score

    return_list = sorted(word_dict.items(), key=lambda x: (x[1],x[0]), reverse=True)

    return [tups[0] for tups in return_list]


def answer4(names):

    score_table = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1,27)))

    word_tuplist = []

    for name in names:      # build (word, score) tuple from list of names and score table
        word_score = 0
        for chr in name:
            word_score += score_table[chr]
        word_tuplist.append((name, word_score))


    for insert_pass in range(1,len(word_tuplist)):
        left = insert_pass
        while (left > 0):
            if word_tuplist[left][1] >= word_tuplist[left-1][1]:
                if word_tuplist[left][1] > word_tuplist[left-1][1]:
                    word_tuplist[left], word_tuplist[left-1] = word_tuplist[left-1], word_tuplist[left]

                else:
                    if word_tuplist[left][0] > word_tuplist[left-1][0]:
                        word_tuplist[left], word_tuplist[left-1] = word_tuplist[left-1], word_tuplist[left]
                left -= 1
            else:
                break

    return [tup[0] for tup in word_tuplist]


s = string.ascii_lowercase
random_list = [''.join(random.sample(s,random.randint(0,8))) for i in range(1000)]

given_name_list = [["annie", "bonnie", "liz"],["abcdefg", "vi"]]
print("\n\n-----------------------------------------")
print("    Given test cases            \n")
for i in given_name_list:
    print(str(answer(i)))
t0 = time.clock()
answer(random_list)
t1 = time.clock() - t0
print("\n\nbubble sort  time:   {} \n".format(t1))
print("-----------------------------------------\n\n")


given_name_list = [["annie", "bonnie", "liz"],["abcdefg", "vi"]]
print("-----------------------------------------")
print("    Given test cases            \n")
for i in given_name_list:
    print(str(answer2(i)))
t0 = time.clock()
answer2(random_list)
t1 = time.clock() - t0
print("\n\nmerge sort time:   {} \n".format(t1))
print("-----------------------------------------\n\n")


given_name_list = [["annie", "bonnie", "liz"],["abcdefg", "vi"]]
print("-----------------------------------------")
print("    Given test cases            \n")
for i in given_name_list:
    print(str(answer3(i)))
t0 = time.clock()
answer3(random_list)
t1 = time.clock() - t0
print("\n\nsorted() & dict{{}} time:   {} \n".format(t1))
print("-----------------------------------------\n\n")


given_name_list = [["annie", "bonnie", "liz"],["abcdefg", "vi"]]
print("-----------------------------------------")
print("    Given test cases            \n")
for i in given_name_list:
    print(str(answer4(i)))
t0 = time.clock()
answer4(random_list)
t1 = time.clock() - t0
print("\n\ninsert sort time:   {} \n".format(t1))
print("-----------------------------------------\n\n")


"""
/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/cake/PycharmProjects/level2_1/2_2_2.py


-----------------------------------------
    Given test cases            

['bonnie', 'liz', 'annie']
['vi', 'abcdefg']


bubble sort(1000)  time:   0.46777399999999997 

-----------------------------------------


-----------------------------------------
    Given test cases            

['bonnie', 'liz', 'annie']
['vi', 'abcdefg']


merge sort(1000) time:   0.013773000000000035 

-----------------------------------------


-----------------------------------------
    Given test cases            

['bonnie', 'liz', 'annie']
['vi', 'abcdefg']


sorted() & dict{}(1000) time:   0.0023329999999999185 

-----------------------------------------


-----------------------------------------
    Given test cases            

['bonnie', 'liz', 'annie']
['vi', 'abcdefg']


insert sort(1000) time:   0.29763800000000007 

-----------------------------------------

Name that rabbit
================

"You forgot to give Professor Boolean's favorite rabbit specimen a name? " \
"You know how picky the professor is! Only particular names will do! Fix this immediately," \
" before you're... eliminated!"

Luckily, your minion friend has already come up with a list of possible names,
and we all know that the professor has always had a thing for names with lots of letters near
the 'tail end' of the alphabet, so to speak. You realize that if you assign the
value 1 to the letter A, 2 to B, and so on up to 26 for Z, and add up the values for all of the letters,
the names with the highest total values will be the professor's favorites.
For example, the name Annie has value 1 + 14 + 14 + 9 + 5 = 43, while the name Earz,
though shorter, has value 5 + 1 + 18 + 26 = 50.

If two names have the same value, Professor Boolean prefers the lexicographically larger name.
For example, if the names were AL (value 13) and CJ (value 13), he prefers CJ.

Write a function answer(names) which takes a list of names and returns the list sorted in descending order
of how much the professor likes them.

There will be at least 1 and no more than 1000 names.
Each name will consist only of lower case letters. The length of each name will be at least 1 and no more than 8.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) names = ["annie", "bonnie", "liz"]
Output:
    (string list) ["bonnie", "liz", "annie"]

Inputs:
    (string list) names = ["abcdefg", "vi"]
Output:
    (string list) ["vi", "abcdefg"]
"""
