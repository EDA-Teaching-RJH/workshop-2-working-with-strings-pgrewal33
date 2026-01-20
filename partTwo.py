import math  

def main():
    x = int(input("what is a?"))
    y = int(input("what is b?")) #TO DO  
    pythag(x,y)

def pythag(h,g):
    A = (h ** 2)
    B = (g ** 2)
    answer = (A + B)  #TO DO
    final_answer = math.sqrt(answer)
    print (final_answer)
main()
