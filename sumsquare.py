


# factorial sum

# fac=1
# sum=0
# for i in range(1,num+1):
#     fac=fac*i
# a=(fac)
# while a:
#     b= a%10
#     sum+=b
#     a//=10
# print(sum)


# insertion  
# a=[3,5,9,1,2,4]
# n=len(a)
# for i in range(n-1):
#     min=i
#     j=i-1
#     while j>=0 and key>a[j]:
#         a[j+1]=a[j]
#         j-=1
#     a[j+1]=key
# print(a)

# for i in range(n-1):
#     min =i
#     for j in range(j+1,n):
#         if a[j]<


# a=[2,3,7,8,12,13,15]
# n=len(a)
# key=int(input())
# low=0
# high = n-1
# while low<=high:
#     mid=low+(high-low)//2
#     if a[mid]==key:
#         print("exist")
#         break
#     elif (a[mid]<key):
#         low=mid+1
#     elif a[mid]>key:
#         high=mid-1

#     else:
#         print("not")


# def binsearch(a,low,high,key) 


# a=int(input())
# c=0
# max=0
# for i in a:
#     if i%2==0:
#   

# n=int(input())
# d=list(map(int,input().split()))
# r=list(map(int,input().split()))
# min=float("inf")
# min_index=0
# i=0
# while i<n:
#     if d[i]<min:
#         min=d[i]
#         min_index=i
#     i+=1
# print(k*min+r(min_index))

# n=list(map(int,input().split()))
# n=[2,3,4,5,6,7]
# a=[]
# c=1
# if n==1 or n==2:
#     print("YES")
# elif a[0]<=a[1]:
#     for i in range(n-1):
#         if a[i]<a[i+1]:
#             c+=1
#         else:
#             break
# else:
#     for i in range(n-1):
#         if a[i]>a[i+1]:
#             c+=1
#         else:
#             break
# if c==n:
#     print("YES")
# else:
#     print("no")