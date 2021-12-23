'''l=[4,3,2,1]
output:[4,3,2,2]'''
i=0
s=0
while(i<len(digits)):
      g=digits[i]
      s=s*10+g
      i+=1
s+=1 
k=[int(x) for x in str(s)]
return k


'''l=[2,7,11,15] target=9
output:[0,1]'''
Because nums[0] + nums[1] == 9, we return [0, 1].
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            return([i,j])

'''palindrome'''
s=str(x)
d=list(s)
d.reverse()
print(d)
r=''
for i in range(len(d)):
    n=d.pop(0)
    r=r+n
if(s==r):
    return True
else:
    return False


nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
'''Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores)'''
while(nums.count(val)):
    nums.remove(val)
print(nums)


'''haystack = "hello", needle = "ll"
Output: 2'''
if needle in haystack:
    return(haystack.index(needle))
else:
    return(-1)


'''nums = [1,3,5,6], target = 5
Output: 2'''
if target in nums:
    return(nums.index(target))
else:
    nums.append(target)
    d=sorted(nums)
    return(d.index(target))

'''EXPLANATION:return string with uppercase if more no of uppercase letters are there in a string else return with lowercase'''
def isupper(c):
    if (c.isupper()):
        return True
    
s='hoUsEST'
d=len(s)
j=(1+len(s))//2
c=0
if(d%2!=0):
    for i in s:
        if(isupper(i)):
            c+=1
    if(c>=j):
        print(s.upper())
    else:
        print(s.lower())
else:
    for i in s:
        if(isupper(i)):
            c+=1
    if(c>j):
        print(s.upper())
    else:
        print(s.lower())


'''EXPLANATION:if the last digit of the number is non-zero, she decreases the number by one;
if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).(Until k times)'''
n,k=map(int,input().split())
for i in range(k):
      if(n%10==0):
            n=n//10
      else:
            n-=1
print(n)


'''EXPLANATION:Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.
Bob wants to become largest of bears.The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10)
— the weight of Limak and the weight of Bob respectively.
Print one integer, denoting the integer number of years after which Limak will become strictly larger than Bob.'''
m,n=map(int,input().split())
c=0
while(m<=n):
    m*=3
    n*=2
    c+=1
print(c)


'''EXPLANATION:An Elephant reaches to his Friend's house only in 1,2,3,4,5 steps at a time,so based on the distance,print howmany steps are needed
to reach the Destination
Example:5
OUTPUT:1(need 1 steps to reach Destination)
Example:12
OUTPUT:3(need 3 steps to reach a Distance of 12 mts)'''
n=int(input())
k=0
c=0
if(n<=5):
    print("1")
else:
    while(k!=n):
        k+=5
        p=n-k
        c+=1
        if(k>=n):
            break
    print(c)


'''EXPLANATION:For example if n = 1, then HULK(Dr.Bruce Banner) feeling is "I hate it" or if n = 2 it's "I hate that I love it",
and if n = 3 it's "I hate that I love that I hate it" and so on.'''
n=int(input())
m=n
for i in range(1,n):
    if(i%2==0):
        print("I love that",end=' ')
    else:
        print("I hate that",end=' ')
if(m%2==0):
    print("I love it",end=' ')
else:
    print("I hate it",end=' ')
