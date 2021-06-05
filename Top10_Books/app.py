import random
import os

here = os.path.dirname(os.path.abspath(__file__))

file = os.path.join(here, 'library.txt')

file1=open(file,'r',encoding='utf-8')
top10=[]          # books at index 0 is most read book and so on...
Library={}            # to store all the books and their corresponding count 

def add_to_fav(name,count):
    book=[name,count] # if there is nothing in top10 thend add directly
    if len(top10)==0:
        top10.append(book)
        return
    if len(top10)<10:       #if there are less than 10 books in top10 then add the coming book at correct position
        for x in range(len(top10)):
            if book[1]>=top10[x][1]:
                top10.insert(x,book)
                return
    elif book[1]>top10[9][1]:           # if there are already 10 books in top10 then add the coming book if eligible at
        for x in range(10):             # correct positiona, after addition there will be 11 books in top 10 so remove the
            if book[1]>=top10[x][1]:    #  last book from top10 to maintain top10.
                top10.insert(x,book)
                top10.pop(10)
                return
    else:
        return

def read_book(book):                # if someone read a 'book' then this will increase it's count by one 
    Library[book]=Library.get(book, 0)+1 #and also add to favorite if it's eligible
    add_to_fav(book,Library[book]) 
   
while True:
    try:
        line = file1.readline()
        if not line:
            break
        name=line.split('-')[0]
        freq=random.randint(0,10000)
        Library[name]=freq
        add_to_fav(name,freq)

    except Exception as e:
        print('error: ',e,)
        continue

for x in top10:
    print(x[0])
