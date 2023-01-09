print ("Hello, World!")
def char_count(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i,0) + 1
    return dict

def possible(lword,charset):
    for word in lword:
        flag=1
        chars = char_count(word)
        for key in chars:
            if key not in charset:
                flag = 0
            else:
                if charset.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)

if __name__ == "__main__":
    input = ['hello', 'bye', 'me', 'eaten', 'goal', 'boy', 'run','milton','riya','tiger']
    charset = ['e', 'o', 'b', 'a', 'm', 'g', 'l','h','y','l']
    possible(input,charset)
