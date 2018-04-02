if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist=list(arr)
    mylist=list(set(mylist)) 
    mylist.sort(reverse=True)
    print(mylist[1])
    
