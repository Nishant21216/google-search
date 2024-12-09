from googlesearch import search as s 

keyword=input("Enter Your Query")

result= s(keyword,5)

for i in result:
    print(i)