def string():
    dictionary={}
    n=int(input())
    for i in range(n):
        a, b=input().split()
        dictionary[a]=b
        dictionary[b]=a
    word=input()
    print(dictionary[word])
string()
    
