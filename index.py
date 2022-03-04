
def tal_medel(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("Medoll tälet är =", tal_medel([7,1,4]))


# Uppgift 1
# höjd=int(input("Skriv höjden av din tringaglegl")) 

# längd=int(input("Skriv längden av din triangel"))

# print(höjd*längd/2) 