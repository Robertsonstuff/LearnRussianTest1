rus_list = ['shto', 'priyet', 'koshka']
eng_list = ['what', 'hi', 'cat']
lst = []
sum = len(eng_list)

for i, x in zip(rus_list, eng_list, ):
    print("\nWhat does", i, 'mean? ')
    input()
    print('the correct answer is: ', x)
    ele = input('\ndid you get it right? (y or n) ')
    lst.append(ele)

print(f"\nYou\'ve answered {lst.count('y')} out of {sum} correct!!")
