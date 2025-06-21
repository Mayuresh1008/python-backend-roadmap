## Loop Control Statements

## break - Stop the loop immediately

for i in range(1, 10):
    if i == 5:
        print("Stopping at 5")
        break
    print(i)

## continue - skip the current round and go to next
print("")
for i in range(1, 6):
    if i == 3:
        continue 
    print(i)

