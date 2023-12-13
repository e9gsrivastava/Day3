# def home():
#     x={'car':'tesla'}

# def bone():
#     p=x[car]+'s'
#     print(p)
# print(bone)


#Q1 list comprehension

# x=[i**2 for i in range(1,21) if i%2==0]
# print(x)


#Q2  zip

# a=[1,2,3]
# b=[4,5,6]
# r=[i for i in zip(a,b)]
# print(r)

#Q3 multiples

# x=int(input("enter any int"))
# result=[]
# result=[i*x for i in range(1,11)]


# print(result)



# Q4 divisors

# result=[]
# x=1000
# for i in range(1,x):
#     if x%i==0:
#         result.append(i)
#         if len(result)==10:
#             break


# result=[i*x for i in range(1,11)  if x%i==0]

# print(result)


# Q5 if in list comprehension




# a=[-2,13,-5,0,1,2]
# result=[i for i in a if i>=0]
# print(result)


#Q6 if else

# a=[-2,13,-5,0,1,2]
# result=[ i if i>=0 else i*-1 for i in a]     
# print(result)


# Q7 multiple loops
# a=[1,2,3]
# result=[ x  for i in a for x in range(i)]     
# print(result)

# Q8 



# a=[[1,2],[3,16],[8,9]]
# # result=[1,2,3,16,8,9]

# result=[ x  for i in a for x in i]     
# print(result)




##############dict comprehensins***********************************

# Q1

# a=['fruits', 'Car','Board']
# di={i:len(i) for i in a}
# print(di)


# Q2 if 

# a=['fruits', 'Car','Board']
# di={i:len(i) for i in a if len(i)>4}
# print(di)


# Q3 imp

a=16
print(9**(1/2))
di={ i:True if i**(0.5)== int(i**(.5)) else False for i in range(a+1) } 
print(di)

