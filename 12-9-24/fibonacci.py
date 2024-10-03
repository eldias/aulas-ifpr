nterms = int(input("How many terms? "))

# first two terms
p1, p2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please specify a positive integer")
# if there is only one term, return p1
elif nterms == 1:
   print("Fibonacci sequence upto", nterms, ":")
   print(p1)

else:
   print("Fibonacci sequence:")
   while count < nterms: # Enquanto a contagem não alcançar nterms(nº inserido por input): 
       print(p1) # imprima o penultimo
       nth = p1 + p2 # some o penultimo e ultimo em atual(nth)
       # update values
       p1 = p2 # penultimo recebe ultimo
       p2 = nth # ultimo recebe atual 
       count += 1 # incrementa contagem em 1