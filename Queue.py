ar=[0 for _ in range(10)]
n=10

front=-1
rear=-1

def enqueue(item):
    global n
    global front
    global rear

    if rear==n-1:
        print("Overflow", end='')
        print("\n", end='')
        return
    
    else:
        if front==-1 and rear==-1:
            front=0
            rear=0
        
        else:
            rear+=1
        
        ar[rear]=item
        print("Element inserted")

def dequeue():
    global front
    global n
    global rear

    if front==-1 or front > rear:
        print("Underflow", end='')
        return
    
    else:
        item=ar[front]
        print("Element deleted from queue is:",end='')
        print(item,end="")
        print("\n",end='')
        if rear==front:
            rear=-1
            front=-1
        
        else:
            front=front+1
            front+=1

def display():
    global n
    global rear
    global front

    