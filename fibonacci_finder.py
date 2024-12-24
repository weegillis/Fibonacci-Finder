# fibonacci finder

def fibonacci_finder(n):
  def fib(lim):
    a = 0
    b = 1
    i = 0
    while i < lim:        
      if i < 2: 
        i += 1
        yield i - 1
      else:
        c = a + b
        a = b
        b = c
        i += 1
        yield c

  for i in fib(n):
    z = i
  return z
    
x = 1001
print (fibonacci_finder(x))
