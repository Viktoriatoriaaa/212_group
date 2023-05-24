class Object:
    def first(self,obj):
        if isinstance(obj,str):
            if sum(i in set('aouei') for i in obj.lower())*sum(i not in set('aouei') for i in obj.lower()) <= self.second(obj):
                return [i for i in obj if i.lower() in set('aouei')]
            else:
                return [i for i in obj if i.lower() not  in set('aouei')]
        elif isinstance(obj,int):
            return sum(int(i) for i in str(obj) if int(i)%2 == 0)*self.second(obj)
    def second(self,obj):
        return len(str(obj))

Primer = Object()
Primer_1 = Primer.first('abcdef')
Primer_2 = Primer.first(123)

print(Primer_1)
print(Primer_2)

