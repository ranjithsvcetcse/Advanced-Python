class Sample:
    #public variable
    rollno=None
    #private variable
    __name=None
    
    def display(self):
        print(Sample.rollno,self.__name)

#main
obj=Sample()
obj.display()
obj.__name="Hello"
obj.display()

#Output
'''
None None
'''

