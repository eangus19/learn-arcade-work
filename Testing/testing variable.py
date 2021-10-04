months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("enter a month number: "))
month = months[(n - 1) * 3:(n - 1) * 3 + 3]
print(month)

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=" ")