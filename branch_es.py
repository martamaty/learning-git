napis=("Co dziszaj kupuje?")
print(napis)
dicto={
    "warzywniaka":["marchew","pomarancza","banany"],
    "piekarnie":["bulki","chleb","rogal"]
}

for i in dicto:
    print("jezeli ide do",i,"kupuje",dicto[i])

count = 0
for key, value in dicto.items(): 
    if isinstance(value, list):
        count += len(value) 

print("w sumie to kupuje",count,"produktow")
print("branch-es")