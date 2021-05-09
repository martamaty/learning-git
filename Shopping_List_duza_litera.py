napis=("Co dziszaj kupuje?")
print(napis)
dicto={
    "warzywniaka":["marchew","pomarancza","banany"],
    "piekarni":["bulki","chleb","rogala"]
}

for i in dicto:
    print("jezeli ide do",i.title(),"kupuje",str(dicto[i]).title())

count = 0
for key, value in dicto.items(): 
    if isinstance(value, list):
        count += len(value) 

print("w sumie to kupuje",count,"produktow")







