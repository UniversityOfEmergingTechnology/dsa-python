class TwoStacks :
    def __init__(self , n):
        # intialize two stacks in one list of size n
        self.size  = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = n

    def push1 (self , x):
        if self.top1 < self.top2 - 1 :
            self.top1 += 1
            self.arr[self.top1] = x
        else :
            return "Stack overflow"
        
    def push2 (self , x):
        if self.top1 < self.top2 - 1 :
            self.top2 -= 1
            self.arr[self.top2] = x
        else :
            return "Stack overflow"
    
    def pop1 (self ):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return x
        else :
            return "Stack underflow"
    
    def pop2 (self ):
        if self.top2 >= 0:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else :
            return "Stack underflow"
        
st = TwoStacks(5)

st.push1(1)
st.push1(2)
st.push1(3)
st.push2(4)
st.push2(5)

st.pop1()
print(st.arr)
st.push2(100)
print(st.push2(100))

print(st.arr)




