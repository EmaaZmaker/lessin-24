dict1={"EA":9,"RC":9,"BE":9,"NF":5}
k=9
result=0
for key in dict1:
    if dict1[key]==k:
        result=result+1
print(f"the frequency of k is {result}")