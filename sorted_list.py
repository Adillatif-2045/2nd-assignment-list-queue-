#take input from user to know the length of the list

print("How many numbers you want to enter in list")
x = input()

#check enterd no is digit or not

if not x.isdigit():
    print("You entered an invalid value.")
else:

#make list

    enterd_list=[]
    for i in range(int(x)):
        u_list = int(input("Enter first no #{}: ".format(i+1)))

#append the enterd list

        enterd_list.append(u_list)

#print enterd list

    print("your enterd list is:" ,enterd_list)

#print sorted list

    enterd_list.sort()
    print("sorted list is: ", enterd_list)

#enter any num you want to append

    print("enter any no you want to append")
    appended_no = input()
    if not appended_no.isdigit():
        print("You entered an invalid value.")
    else:
        enterd_list.append(int(appended_no))
        print("list after appending with new no: ",enterd_list)
        enterd_list.sort()
        print("list after appending and sorted with new no: ", enterd_list)

#end of the code

