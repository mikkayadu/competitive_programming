# list_of_words = []
# for i in range(int(input())):
#     word = input()
#     list_of_words.append(word)
order = "worldabcefghijkmnpqstuvxyz"
d = dict()
counter = 1
for letter in order:
    d[letter] =counter; counter+=1


def sort_key(x):
    return d[x]

print(sort_key('l'))
mylist = ['word', 'world']
print(min(mylist, key=lambda x : [order.index(char) for char in x]))