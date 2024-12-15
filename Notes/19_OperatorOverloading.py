class number:
    def __init__(self,value):
          self.n = value
      # For add 
    def __add__(self,num):
         return self.n + num.n
   #for subration
    def __sub__(self,num):
          return self.n - num.n   
    #for division
    def __truediv__(self,num):
          return self.n/num.n
    #for floor division
    def __floordiv__(self,num):
          return self.n//num.n
    #for greater then
    def __gt__(self,num):
          return self.n>num.n
    # for less then
    def __lt__(self,num):
      return self.n<num.n
      #for greater than equal to
    def __ge__(self,num):
          return self.n>=num.n
    # for less then equal to
    def __le__(self,num):
          return self.n<=num.n
    

n = number(1)
m = number(2)
print(n+m)
print(n-m)
print(n/m)
print(n//m)
print(n<m)
print(n>m)
print(n>=m)
print(n<=m)
