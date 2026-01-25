def main():

    age = float(input("what is your age? "))

    if age <=18:
        return "you are a child"
    
    else:
        return "you are an adult"
    

result = main()
print(result)