#activity 1
class IOString():
    def __init__(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input("enter string:")
        
    def print_String(self):
        self.str1 = ("Result is :", self.str1.upper())
        
str1 = IOString()

str1.get_String()
str1.print_String()

#activity 2
class Employee:
    
    def __init__(self):
        print('employee created')
    
    def __del__(self):
        print("destructor called")
    
def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

#activity 3
class pair_elements:
    
    def twoSum(self, nums, target):
        lookup = {}
        
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
            
value = int(input("enter sum for witch you want to make this search:"))
print("index1=%d, index2 = %d" %pair_elements.twoSum((10, 20, 30, 40, 50, 60, 70),value))


        

        
