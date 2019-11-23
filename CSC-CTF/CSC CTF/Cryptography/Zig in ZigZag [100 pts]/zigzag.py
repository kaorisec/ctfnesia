#!/usr/bin/python2.7

# CCC{flag}
flag = "REDACTED"

key = 16
arr = [["0" for i in range(len(flag)/key)] for j in range(key)]
row = 0
col = 0
count = 0
for i in range(len(flag)):
	arr[row][col] = flag[i]
	row = (row+1)%key
	col = (col+1)%(len(flag)/key)
	
enc = ""
for i in arr:
	for j in i:
		enc += str(j)
print enc
