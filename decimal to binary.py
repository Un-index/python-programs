

# include base specification feature to serve to illustrate how this would work with other bases

n, base = eval(input("enter number and base here, separated by a comma(,): "));
basestr = str(base)+"|"
print(f"{basestr} {n} | r")
print("_________")
maxdgts = len(str(n))+1;
remchain = ""

while(n>0):
    rem = n%base
    remchain += str(int(rem))
    n = (n-rem)/base
    currdgts = len(str(n))
    print(basestr+f" {int(n)}{(maxdgts-currdgts + 2)*' '}| {int(rem)}")

print("(reversed remainders) binary:", remchain[::-1])
