# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gRtgQ7mD4fVKEKhZGMEu_rVeWKGKmkfr
"""

A = [[1,2,3],[4,5,6],[7,8,9]]
r = list(zip(*A[::-1]))
print(r)

166//2

a = 100


count = 0
while(a):
  count += a&1
  a >>= 1
  
print(count)

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
 
 
i = 100
print(countSetBits(i))



s = "192.164.01.1"
l =[int(e) for e in s.split(".")]

for e in l:
  if e not in range(0,256): print( "Invalid Ip")
  elif: e not

#print(l)

matrix = []
for i in range(n_rows):          # A for loop for row entries
    a =[ ]
    a.append(int(input()))
    matrix.append(a)

nums1 = [1,234,67,3645,24]
nums2 = [324,5436,89,3,674]

merged = nums1 +nums2

merged.sort(reverse = True)
print(merged)

print(int(2.7))

nums1 = [1,2]
nums2 = [3,4]
m = len(nums1)
n = len(nums2)

merged = nums1 + nums2
m_len = len(merged)
merged.sort()

if len(merged) %2 !=0:
    median = merged[int(m_len/2)]
    print( median)
else:
    median = (merged[int(m_len/2)] + merged[int((m_len/2))-1] )/2
    print( median

nums = [12,17,15,13,10,11,12]
msum = 0
msumfinal = 0

for e in nums:
    if msum < (msum+e):

      msum = max(msum,msum+e)
      print(msum)
    else:
      msumfinal = max(msumfinal,msum)
      #print(msumfinal)
      msum = 0
        
print(msumfinal ) #max(msumfinal,msum))

1110010&1