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


sentence = input("Enter your string:")
sentence = sentence.replace(" ", "")

dict = set(line.strip() for line in open('dictionary.txt',encoding="utf-8"))

######## start #############

#################### forward search #####################
for_words=[]
temp = ""
trash = ""
highest = 0
index = 0
flag = False #true = word found
for_count=0

while(True):
    for x in range(index, len(sentence)): #search for word
        temp += sentence[x]
        if(x==len(sentence)-1 or ((not is_token_after_consonant(sentence[x+1])) and not is_token_before_consonant(sentence[x]))):
            if(temp in dict):
                #print('in' + temp)
                highest = x
                flag = True
    if(not flag):  ###if no word is found
        cnt=0
        #check for adjacent vowels and tone marks
        for x in range(index, len(sentence)):
            cnt+=1
            if(x>=len(sentence)-1 or ((not is_token_after_consonant(sentence[x+1])) and not is_token_before_consonant(sentence[x]))):
                break
        trash+=sentence[index:index+cnt]
        index+=cnt
    else:  ###word is found
        if(trash != ""):
            for_words.append(trash) ##append the non-word string
            trash=""
        for_words.append(sentence[index:highest+1])
        for_count+=1
        index = highest+1
    if(index>len(sentence)-1):
        if(trash != ""):
            for_words.append(trash) ##append the non-word string
        break
    else:
        flag=False
    temp = ""

    
######################## backward search ###################
back_words=[]
temp = ""
trash = ""
lowest = 0
index = len(sentence)-1
flag = False #true = word found
back_count=0

while(True):
    for x in range(index, -1,-1): #search for word
        temp = sentence[x]+temp
        if(x==0 or ((not is_token_after_consonant(sentence[x])) and not is_token_before_consonant(sentence[x-1]))):
            if(temp in dict):
                #print('in' + temp)
                lowest = x
                flag = True
    if(not flag):  ###if no word is found
        cnt=0
        #check for adjacent vowels and tone marks
        for x in range(index, -1,-1): 
            cnt+=1
            if(x==0 or ((not is_token_after_consonant(sentence[x])) and not is_token_before_consonant(sentence[x-1]))):
                break
        trash=sentence[index-cnt+1:index+1]+trash
        index-=cnt
    else:  ###word is found
        if(trash != ""):
            back_words.append(trash) ##append the non-word string
            trash=""
        back_words.append(sentence[lowest:index+1])
        back_count+=1
        index = lowest-1
    if(index<=-1):
        if(trash != ""):
            back_words.append(trash) ##append the non-word string
        break
    else:
        flag=False
    temp = ""

back_words.reverse()

for_count = for_count/len(for_words)
back_count = back_count/len(back_words)

if(for_count>back_count):
    print(for_words)
else:
    print(back_words)
