
# --------->string python assiment:-

# mystr="world largst population country name is india"

# print(mystr.count("o"))
# print(mystr.count("i"))
# print(mystr.count("n"))
# print(mystr.count("w"))



# mystr="sunset"

# print(mystr.replace("s","%"))


# mystr="tops technology in cg road  ahmedabad@"

# print(len(mystr))


# mystr="tops technology in varacha in surat"

# print(mystr.count("in"))
      

# mystr=("a,e,i,o,u")

# if "a,e,i,o,u" in mystr:
#     print("yes...")

# else:
#     print("no...")    
  

mystr="tops"
if len(mystr)<4:
    print(mystr.upper())

else:
    print(mystr)



# ------------------> list python assiment:-(collection)----------------------------------------------------------<

# 1) write a python program to check a list is empty or not

'''list=["india"]

if list:
    print("list is not empty")

else:
    print("list is empty")  '''  


# 2) write a python program to remove duplicates from a list

'''list=["india","japan","dubai","london","rassia","usa"]

list.remove("dubai")
print(list)'''

# 3) write a python function that takes two lists and returns the number of common members

'''country={"india","japan","canada","dubai","ahmedabad"}
city={"ahmedabad","surat","japan","p    atna","delhi"}

print(country.intersection(city))'''




# 4)write a python program to get the difference between the two lists


# l1=[1,2,3,4,5,6]
# l2=[1,2,3,4]

# s1=set(l1)
# s2=set(l2)

# l3=list(s1-s2)
# print(l3)


# 5)write a python program to find the second smallest number in a list



# 6)write a python program to find the second largest number in a list

# list=[10,25,58,8,56,98,99]
# list.sort()
# element=list[-2]            #bottem largest number reverse 
# print("second largest number is:",element)


# 7)write a python program to get the frequency of elements in a list


# list=["india","japan","dubai","london","rassia","usa"]

# print(list.count("japan"))



# 8)write a python program to convert a list of multiple integers into a single integer

# list=[11,25,33]

# for i in  list:
#     print(i,end="")

# 9)write a python program to compute the similarity between two lists
 
'''color1={'orange',"red","green","white","pink"}
color2={"red","maroon","pink","blue","green","pink"}

print(color1.intersection(color2))'''

# 10)write a python program to check if all dictionaries in a list is empty or not

'''dictlist=["india",'london','dubai']

if dictlist:
    print("the dictionary list is not empty")

else:
    print("the dictionry list is empty")    
'''

# --------------------->tuple aassiment:------------------------------------------------------------------<

# 1)write a python program to create a tuple with different data types

# mytup=("mango",'apple','orange','banana','stawberry','berry','watermelon')
# print(mytup)

# 2)write a python program to add in an item in tuple

# mytup=(["mango",'apple','orange','banana','stawberry','berry','watermelon'])

# mytup.append("coconut")
# print(mytup)

# 3)write a python program to convert a tuple to a string

mystr=('name',"raj","ran")

str=" ".join(mystr)
print(str)


# 4)write a python program to find the repeted item of tuple

# 5)write a python program to find the lenth of tuple

# mytup=("mango",'apple','orange','banana','stawberry','berry','watermelon')

# print(mytup.__len__())

# 6)write a python program to convert a tuple to a dictionary

# 7)write a python to replace last value of tuple in list
# mytup=[('10,20,30'),('40,50,30'),('70,80,30')]

# 9)wite a pyhton program to sort a tuple by its flot elements



# 10)write a python program to count the elements in a list until an elements is tuple

# mytup=(["mango",'apple','orange','banana','stawberry','berry','watermelon','mango','banana'])


# print(mytup.count('mango'))



#-----------------------------------sets-----------------------------------------------

# 1) write a python program to iteration over sets:-

# num_set=([1,2,3,4,5])

# for i in num_set:
#     print(i)


# 2) wirte a python program in add member in set  

# product={'besan','sugar','salt','tuemeric','lemon'}

# product.add('tea')
# print(product)

# 3) write a pyhon pogram to remove item in set

# myset={'orange','red','purple','white','black'}

    # myset.remove("red")
# print(myset)

# 4)write a python program to remove am item from if is present in set

# productset={"meet",'manav',"raj",'shyam','rahul'}

# productset.clear()
# print(productset)

# 5)write a python program create intersection in sets

# productset={"meet",'manav',"raj",'shyam','rahul'}

# myset={'orange','red','purple','white','black',"meet",'rahul'}

# print(productset.intersection(myset))

# 6)write a python program create a symmertric of sets.


# productset={"meet",'manav',"raj",'shyam','rahul'}

# myset={'orange','red','purple','white','black',"meet","manav","rahul"}

# print(productset.symmetric_difference(myset))

# 7)write a python program to find maximum and minimum value in the sets

# # 8)write a python program of lenth of a sets
# productset=len({"meet",'manav',"raj",'shyam','rahul'}) 
# print(productset)

# for i in "tops technology":
#     print(i)