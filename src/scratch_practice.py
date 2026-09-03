num_data=[10,20,10,30,20,10,40]
count_dict={}
for n in num_data:
    if n in count_dict:
        count_dict[n]+=1
    else:
        count_dict[n]=1
print(count_dict)