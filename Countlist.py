class Countlist:
    def __init__(self,*arge):
        self.value=[x for x  in arge ]
        self.count={}.fromkeys(range(len(self.value)),0)

    def __len__(self):
        return len(self.value)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.value[key]
