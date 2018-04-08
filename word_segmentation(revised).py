import unicodedata as u

print("Importing Dictionary")
print("Array-izing dictionary")

def is_consonant(ch):
    if(ord(ch) >= 3585 and ord(ch) <= 3630):
       return True
    else: return False

def is_token_after_consonant(ch):
    if((ord(ch) >= 3632 and ord(ch) <= 3642) or ord(ch)==3653 or (ord(ch)>=3655 and ord(ch)<=3662)):
       return True
    else: return False

def is_token_before_consonant(ch):
    if(ord(ch) >= 3648 and ord(ch) <= 3652):
       return True
    else: return False

def is_number(ch):
    if((ord(ch) >= 48 and ord(ch) <= 57) or ord(ch)==44 or ord(ch)==46):
       return True
    else: return False


sentence = input("Enter your string:")
sentence = sentence.replace(" ", "")

dict = set(line.strip() for line in open('dictionary.txt',encoding="utf-8"))

######## start #############

def search(text,option):
    #option: 1=forward, 2=backward
    words=[]        #create array output words
    trash = ""      #group of junk letters(can't form a word)
    edge = 0        #index of first char of word(forward) / last char of word(backward)
    flag = False    #true = word found
    count=0         #number of words in array
    temp = ""
    
    start=0 #start index
    stop=0  #stop index
    step=0  #step
    if(option==1):
        start=0
        stop=len(text)
        step=1
    elif(option==2):
        start=len(text)-1
        stop=-1
        step=-1
    else:
        return "Invalid Option"
    
    while(True): #------------------start while-------------------------------------
        for x in range(start,stop,step): #search for word
            if(option==1):#---forward
                temp += text[x]
                rim = len(text)-1    #check if index=last
                after = x+1             #index for is_token_after_consonant(text[after])
                before = x              #index for is_token_before_consonant(text[before])
            else:#------------backward
                temp = text[x]+temp
                rim = 0                 #check if index=first
                after = x
                before = x-1
            if(x==rim or ((not is_token_after_consonant(text[after])) and not is_token_before_consonant(text[before]))):
                if(is_number(text[start])):
                    edge = x
                    flag = True
                    break
                if(temp in dict):
                    edge = x
                    flag = True
        if(not flag):   #word not found
            cnt=0       #count how many letters(index) are in trash
            #check for adjacent vowels and tone marks
            for x in range(start,stop,step):
                cnt+=1
                if(option==1):#---forward
                    rim = len(text)-1    #check if index=last
                    after = x+1             #index for is_token_after_consonant(text[after])
                    before = x              #index for is_token_before_consonant(text[before])
                else:#------------backward
                    rim = 0                #check if index=first
                    after = x
                    before = x-1
                if(x==rim or ((not is_token_after_consonant(text[after])) and not is_token_before_consonant(text[before]))):
                    break
            if(option==1):#---forward
                trash+=text[start:start+cnt]
                start+=cnt
            else:#-------------backward
                trash=text[start-cnt+1:start+1]+trash
                start-=cnt
        else:  ###word is found
            if(trash != ""): ##append the non-word string
                words.append(trash) 
                trash=""
            count+=1    #count for words found in dict
            if(is_number(text[edge])):
                if(option==1):
                    add=1
                else:
                    add=-1
                while(True): #for grouping the number together
                    if(edge!=rim and is_number(text[edge+add])):
                            edge+=add
                    else:
                        break
            if(option==1):
                words.append(text[start:edge+1])
                start = edge+1
            else:#------------backward
                words.append(text[edge:start+1])
                start = edge-1
        #----check if all chars are checked-----
        if(start-stop==0): #start reaches stop index
            #append the non-word string(if any)
            if(trash != ""): words.append(trash) 
            break
        else:
            flag=False
        temp=""
    #----------------------------------------end while----------------------
    if(option==2): words.reverse()
    #append number of words found in dict to last index
    words.append(count)
    return words

for_words = search(sentence,1)
back_words = search(sentence,2)

#pfor = percent of for_words
pfor = float(for_words.pop()/len(for_words))
#pback = percent of back_words
pback = float(back_words.pop()/len(back_words))

if(pfor>pback):
    print(for_words)
else:
    print(back_words) 
    


