def main():
    pounds = pounds_to_float(input("How much was the meal? "))

    percent = percent_to_float(input("What percentage would you like to charge? "))
        
    
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")

def pounds_to_float(d):
    pounds = (d.replace("£","")) #TODO
    return float(pounds)

def percent_to_float(p):
    n = (p.replace("%",""))    #TODO
    n = float(n)
    percent = n/100
    return percent
main()
