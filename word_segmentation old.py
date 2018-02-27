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
index = 0
highest = 0
temp = ""
flag = False
for_words=[]
for_count=0
#################### forward search #####################
while(3>2):
    for x in range(index, len(sentence)):
        temp += sentence[x]
        if(x==len(sentence)-1 or ((not is_token_after_consonant(sentence[x+1])) and not is_token_before_consonant(sentence[x]))):
            if(temp in dict):
                #print('in' + temp)
                highest = x
                flag = True
    if(not flag):
        cnt=0
        for x in range(index, len(sentence)):
            cnt+=1
            if(x>=len(sentence)-1 or ((not is_token_after_consonant(sentence[x+1])) and not is_token_before_consonant(sentence[x]))):
                break
        for_words.append(sentence[index:index+cnt])
        index+=cnt
    else:
        for_words.append(sentence[index:highest+1])
        for_count+=1
        index = highest+1
    if(index>len(sentence)-1):
        break
    else:
        flag=False
    temp = ""

back_words=[]
temp=""
lowest=0
index = len(sentence)-1
flag=False
back_count=0
############################ backward search ###################
while(3>2):
    for x in range(index, -1,-1):
        temp = sentence[x]+temp
        if(x==0 or ((not is_token_after_consonant(sentence[x])) and not is_token_before_consonant(sentence[x-1]))):
            if(temp in dict):
                #print('in' + temp)
                lowest = x
                flag = True
                
    if(not flag):
        cnt=0
        for x in range(index, -1,-1):
            cnt+=1
            if(x==0 or ((not is_token_after_consonant(sentence[x])) and not is_token_before_consonant(sentence[x-1]))):
                break
        back_words.append(sentence[index-cnt+1:index+1])
        index-=cnt
    else:
        back_words.append(sentence[lowest:index+1])
        back_count+=1
        index = lowest-1
    if(index<=-1):
        break
    else:
        flag=False
    temp = ""

back_words.reverse()

if(for_count>back_count):
    print(for_words)
else:
    print(back_words)
