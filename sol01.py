f = open("input01.txt","r")
text = f.read()
f.close()

text_list = text.split()
digits = list(map(lambda x: ''.join(filter(str.isdigit, x)), text_list))

atwo_digits = list(map(lambda x: int(x[0] + x[-1]), digits)) 
print(sum(atwo_digits))
rep_dict = {
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9' 
}
tokens = ['one','1', 'two','2', 'three','3', 'four','4', 'five','5', 'six','6', 'seven','7', 'eight','8', 'nine','9'] 

def word2digits(word):
    for key in rep_dict:
         word = word.replace(key, rep_dict[key])
    return word

def first_last(word):
    first = ""
    first_ind = len(word)
    last = ""
    last_ind = 0
    for tok in tokens:
        ind = word.find(tok)
        indr = word.rfind(tok)
        if ind != -1 and ind <= first_ind:
           first_ind = ind
           first = tok
        if indr != -1 and indr >= last_ind:
            last_ind = indr
            last = tok
    return first + last

fl_digits = list(map(lambda w: first_last(w), text_list))
two_digits = list(map(lambda x: int(word2digits(x)), fl_digits))

print(sum(two_digits))
