
fran = "books/frankenstein.txt"
    
    
def count_letters(word:str):
    ret = {}
    alphabet = "qwertzuiopasdfghjklyxcvbnm"
    for i in word.lower():
        if i not in alphabet:
            continue
        if not i in ret.keys():
            ret[i] = 1
        else:
            ret[i] +=1
    return ret

def chunks(lst, n):
    ret = []
    for i in range(0, len(lst), n):
        ret.append(lst[i:i + n])
    return ret

def counting(words):
    ret = {}
    alphabet = "qwertzuiopasdfghjklyxcvbnm"

    for word in words:
        for i in word.lower():
            if i not in alphabet:
                continue
            if not i in ret.keys():
                ret[i] = 1
            else:
                ret[i] +=1
    return ret

def report(data:dict, words):
    print("---- The report: -----")
    print(f"{words} were found")
    for entry in data:
        print("the letter '{}' was found {} times".format(entry, data[entry]))
def main():
    with open(fran, 'r') as file:
        text = file.read()
    words = text.split()
    data = counting(words)
    report(data, len(words))    


if __name__ == "__main__":
    main()