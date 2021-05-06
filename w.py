import re
text = "私の名前は__名前__です。"

def mad(mls):
    hint = re.findall("__.*?__",mls)
    if hint is not None:
        for word in hint:
            q = "{}を入力".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        #print("\n")
        #mls = mls.replace("\n","")
        print(mls)
mad(text)