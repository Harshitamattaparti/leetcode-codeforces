'''EXPLANATION:Given an array nums of size n, return the majority element.The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.'''
n=len(nums)
d=list(set(nums))
if(n%2==0):
      for i in d:
            if(nums.count(i)>(n//2)):
                  return i
for i in d:
      if(nums.count(i)>=(n//2)+1):
            return i

'''EXPLANATION:Return Maximum number of words in a sentence from the list'''
a=["alice and bob love leetcode","i think so too","this is great thanks very much"]
d=0
for i in range(len(a)):
    b=a[i]
    x=b.split(' ')
    print(x)
    k=len(x)
    if(k>d):
        d=k
print(d)

'''EXPLANATION:reverse a list of Characters'''
s=['h','e','l','l','o']
d=len(s)
if(d%2!=0):
      for i in range(0,(d//2)+1):
      s[i],s[-(i+1)]=s[-(i+1)],s[i]
else:
      for i in range(0,(d//2)):
      s[i],s[-(i+1)]=s[-(i+1)],s[i]

'''EXPLANATION:return maximum length of Consecutive ones'''
c=0
d=0
l=[]
for i in nums:
      if(i==1):
            c+=1
      else:
            c=0
      if(c>d):
            d=c
return d

'''EXPLANATION:return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.'''
nums.sort()
d=list(set(nums))
if(len(d)==1):
      return d[0]
d.remove(max(d))
d.remove(max(d))
if(len(d)!=0):
      return max(d)
else: 
      return max(nums)


'''EXPLANATION:The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
return max of the total sum'''
s='011101'
d=s
a=[]
for i in range(1,len(d)):
    d=s
    l=d[0:i]
    m=d[i:]
    k=[int(x) for x in str(l)]
    n=[int(x) for x in str(m)]
    a.append(k.count(0)+n.count(1))
print(max(a))


'''EXPLANATION: To see whether the s can turn into goal after certain rotations'''
s='abcde'
goal='abced'
c=''
d=0
for i in range(1,len(s)):
        b=s[i:]
        a=s[0:i]
        c=b+a
        if(c==goal):
            d+=1
            break
if(d==1):
    print("True")
else:
    print("False")


'''EXPLANATION: if number '3322251' is given there are two 3's,three 2's,one 5 and one 1 is there,
so we have to print the number like '23321511''''
a='17774663889222'
d=list(a)
for i in d:
        if(d.count(i)>1):
                d.remove(i)
s=list(a)
f=[]
for i in d:
        m=s.count(i)
        f.append(m)
u=''
p=''
w=[]
for i in range(len(f)):
        r=f[i]*10+int(d[i])
        w.append(r)
        p=p+str(w[i])
print(p)


'''EXPLANATION:To count the no of even numbers in every loop.For example if an array 1 2 4.Therefore
[1] requires 0 operations.
[1,2] requires 1 operation.
[1,2,4] requires 2 operations.
[2] requires 1 operation.
[2,4] requires 2 operations.
[4] requires 1 operation.
Total 7 operations are required to convert Even to Odd Numbers'''
n=int(input())
for i in range(n):
    r=int(input())
    l=list(map(int,input().split()))
    c=0
    i=0
    e=0
    while(i<len(l)):
        j=0
        while(j<=i):
            if(l[j]%2==0):
                c+=1
            j+=1
        i+=1
        if(i==len(l)):
            l.remove(l[e])
            i=0
            if(len(l)==0):
                break
    print(c)

'''EXPLANATION:Given a positive integer
num consisting only of digits 6 and 9.Return the maximum number you can get
by changing at most one digit (6 becomes 9, and 9 becomes 6).Written in CPP'''
#include <iostream>
using namespace std;
int main()
{
    float n,r;
    cin>>n;
    float d=n;
    int i=1000,p,c;
    while(i>=1)
    {
        if(n==9999)
        {
            cout<<9999;
            break;
        }
        p=n/i;
        r=n/i;
        if(p==6)
        {
            c=i;
            break;
        }
        else
        {
            n=((r*i)-(p*i));
            i=i/10;
        }
    }
    if(c==1000)
    {
        cout<<d+3000;
    }
    else if(c==100)
    {
        cout<<d+300;
    }
    else if(c==10)
    {
        cout<<d+30;
    }
    else if(c==1)
    {
        cout<<(d+3);
    }
    else cout<<"";
}

'''EXPLANATION:Given an integer array nums and an integer k,
return the kth largest element in the array.
nums = [3,2,1,5,6,4], k = 2'''
nums.sort()
return nums[-k]

'''EXPLANATION:Given a signed 32-bit integer x, return x with its
digits reversed. If reversing x causes the value to go outside the signed
32-bit integer range [-231, 231 - 1], then return 0.
x=123
OUTPUT:321
x=-123
OUTPUT:-321'''
if(x>0):
      d=int(str(x)[::-1])
      if(d>-(2**31) and d<((2**31)-1)):
            return d
      else:
            return 0
else:
      x=(x+2*(-x))
      d=-int(str(x)[::-1])
      if(d>-(2**31) and d<((2**31)-1)):
            return d
      else:
            return 0

'''EXPLANATION:word = "abcdefd", ch = "d" Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".'''
if ch in word:
      l=list(word)
      w=''.join(l[0:(l.index(ch))+1])
      return w[::-1]+''.join(l[l.index(ch)+1:])
return word

'''EXPLANATION:
Input: moves = "RRUDLULUDD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude,
so it ended up at the origin where it started. Therefore, we return true.'''
d=moves.count('U')
f=moves.count('D')
j=moves.count('L')
k=moves.count('R')
if((d==0 and j==k) or (j==0 and d==f)):
      return True
elif(j==k and d==f):
      return True
return False
