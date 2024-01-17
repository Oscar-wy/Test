numbers = [1,2,3,4,7,8,9,44,3,11,545]
found = False
user = int(input("Enter A Number: "))
for i in range(len(numbers)-1):
    if user == numbers[i]:
        print(f"{numbers[i]} Found")
        found = True
if found == False:
    print(f"Not Found {user}!")