i=1
sum =0
while True:
    multi=3*i
    if sum+multi<=500:
        sum+=multi
        i=i+1
    else:
        break
print(sum)
