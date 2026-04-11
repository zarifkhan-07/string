def cal(price, S):
    n=len(price)
    st=[]
    st.append(0)
    S[0]=1
    for i in range(1,n):
        while(len(st)>0 and price[st[-1]]<=price[i]):
            st.pop()
        S[i]=i+1 if len(st)==0 else(i-st[-1])
        st.append[i]
def print(Arr,n):
    for i in range(0,n):
        print(Arr[i],end="")
price=[10,20,30,40,50]
S=[0 for i in range(len(price)+1)]

cal(price,S)
print(S,len(price))