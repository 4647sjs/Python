class Calculator:
    def __init__(self, list):
        self.list=list

    def add(self):
        result=0
        for i in self.list:
            result+=i
        return result

    def avg(self):
        total=self.add()
        return total/len(self.list)


cal1=Calculator([1,2,3,4,5])
print(cal1.add())
print(cal1.avg())

cal2=Calculator([6,7,8,9,10])
print(cal2.add())
print(cal2.avg())