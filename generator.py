#迭代器
class Myiterator:
    def __init__(self,n=10):
        self.a=0
        self.b=1
        self.n=n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>self.n:
            raise StopIteration
        return self.a
hu=Myiterator(100)
for each in hu:
	print(each)
#生成器
#def generator():
#    a=0
#    b=1
#    while True:
#        a,b=b,a+b
#        yield a
#
#for each in generator():
#    if each>100:
#        break
#    print(each)
