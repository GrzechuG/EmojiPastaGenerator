

def is_ascii(s):
    return all(ord(c) < 128 for c in s)
def hasNormalLetters(strin):
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    for l in letters:
        if l in strin:
            return True
    return False;

emojiBase1 = open("emojiExamples.txt", "r").read()
emojiBase=(emojiBase1.split(" "))

path1 = input("Path to file with text to remake:")
path2 = input("File to write generated text to:")
text = open(path1, "r").read()
out = ""
chosen = False
for word in text.split(" "):
    chosen = False
    for i in range(len(emojiBase)-1):#emojiWord in emojiBase:
        #print(i)
        #print(word, emojiBase[i])
        if word.lower() == emojiBase[i].lower() and is_ascii(word) and not '🅾️' in emojiBase[i+1] and not hasNormalLetters(emojiBase[i+1] ):
            out += word+" "+emojiBase[i+1]+" ";
            chosen=True
            break
    if not chosen:
        out+=word+" "


out = out.replace("o", "🅾")
out = out.replace("O", "🅾")
open(path2, "w+").write(out)
print("Done.")
