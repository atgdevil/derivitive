poly = input("Enter the polynomial")
poly = poly.replace(" ","")
poly = poly.replace("-","+-")
poly = poly.replace("X","x")
pol_list = poly.split("+")
print(pol_list)

def derivitive() :
    for i in range(len(pol_list)):
        term = pol_list[i]
        if 'x^' not in term:
            if 'x' not in term:
                print("+ 0")
                continue
            else:
                term = term.replace("x","x^")
                coeff = term.split("x^")
                print("+",coeff[0],end="")
                continue
        else:
            coeff = term.split("x^")

            coeff[1] = int(coeff[1]) - 1
            coeff[0] = int(coeff[0]) * int(coeff[1])
            print("+",coeff[0],end="")
            print("x^",end="")
            print(coeff[1],end="")


derivitive()




