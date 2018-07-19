def BaseConverter(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
length = 7
short_url={}
full_url={}
count=0
base62=BaseConverter("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
def genShortURL(fullURL):
    if (fullURL in full_url):
        print("ShortURL already Exists"+full_url[fullURL])
        return
    global count
    s=""
    k=count
    count+=1
    if (k==0):
        s="0000000"
        if (s not in short_url):
            short_url[s]=fullURL
            full_url[fullURL]=s
            print("short url for "+fullURL+" is https://ca.ke/"+s)
            return
    while(k!=0):
        s=base62[k%62]+s
        k=k//62
    l=len(s)
    if (l<length):
        for i in range(length-l):
            s="0"+s
    if (s not in short_url):
        short_url[s]=fullURL
        full_url[fullURL]=s
    print("short url for "+fullURL+" is https://ca.ke/"+s)

while (True):
    print("Enter 1 to shorten URL  or 2 to break")
    userInput=int(input())
    if (userInput==1):
        fullURL=input("Enter an URL to shorten it : ")
        genShortURL(fullURL)
    elif(userInput==2):
        break
    else:
        print("Invalid Input")
