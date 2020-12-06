
from time import time
from random import randrange
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# d is the number of characters in the input alphabet
d = 256

#code for rabin karp algorithm
def search(pat, txt, q): 
	M = len(pat) 
	N = len(txt) 
	i = 0
	j = 0
	p = 0 # hash value for pattern 
	t = 0 # hash value for txt 
	h = 1

	# The value of h would be "pow(d, M-1)% q" 
	for i in range(M-1): 
		h = (h * d)% q 

	# Calculate the hash value of pattern and first window 
	# of text 
	for i in range(M): 
		p = (d * p + ord(pat[i]))% q 
		t = (d * t + ord(txt[i]))% q 

	# Slide the pattern over text one by one 
	for i in range(N-M + 1): 
		# Check the hash values of current window of text and 
		# pattern if the hash values match then only check 
		# for characters on by one 
		if p == t: 
			# Check for characters one by one 
			for j in range(M): 
				if txt[i + j] != pat[j]: 
					break

			j+= 1
			# if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1] 
			#if j == M: 
			#	print ("Pattern found at index " + str(i))

		# Calculate hash value for next window of text: Remove 
		# leading digit, add trailing digit 
		if i < N-M: 
			t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q 

			# We might get negative values of t, converting it to 
			# positive 
			if t < 0: 
				t = t + q 


# Python program for KMP Algorithm
from time import time
def KMPSearch(pat, txt): 
	M = len(pat) 
	N = len(txt) 

	# create lps[] that will hold the longest prefix suffix 
	# values for pattern 
	lps = [0]*M 
	j = 0 # index for pat[] 

	# Preprocess the pattern (calculate lps[] array) 
	computeLPSArray(pat, M, lps) 

	i = 0 # index for txt[] 
	while i < N: 
		if pat[j] == txt[i]: 
			i += 1
			j += 1

		if j == M: 
			
			j = lps[j-1] 

		# mismatch after j matches 
		elif i < N and pat[j] != txt[i]: 
			# Do not match lps[0..lps[j-1]] characters, 
			# they will match anyway 
			if j != 0: 
				j = lps[j-1] 
			else: 
				i += 1

def computeLPSArray(pat, M, lps): 
	len = 0 # length of the previous longest prefix suffix 

	lps[0] # lps[0] is always 0 
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1 
	while i < M: 
		if pat[i]== pat[len]: 
			len += 1
			lps[i] = len
			i += 1
		else: 
			# This is tricky. Consider the example. 
			# AAACAAAA and i = 7. The idea is similar 
			# to search step. 
			if len != 0: 
				len = lps[len-1] 

				# Also, note that we do not increment i here 
			else: 
				lps[i] = 0
				i += 1



## EMPIRICAL ANALYSIS
				
sum_kmp=0
sum_rabin_karp=0

## reads file 
with open('algo sample.txt', 'r') as file:
    data = file.read()


## lst containing all the words in file as string
lst = data.split(" ")
print(lst)
n = len(lst)
x=''
b = True
t = 0 # total patterns to be matched
k=[] # array of time taken by kmp at each interval
r=[] # array of time taken by Rabin karp at each interval
while t!=100:
        if (x=='done'):
                b=False
        else:
                index = randrange(n)
                x= lst[index]
                t=t+1
                ## kmp
                before1 = time()
                KMPSearch(x, data)
                after1 = time()
                total_time_kmp = after1 - before1
                sum_kmp += total_time_kmp
                
                ## rabin karp
                before2 = time()
                q = 101 # A prime number 
                search(x, data, q)
                after2 = time()
                total_time_rabin_karp = after2 - before2
                sum_rabin_karp += total_time_rabin_karp
                k.append(total_time_kmp)
                r.append(total_time_rabin_karp)



print("average time taken by kmp to match: ", sum_kmp/t)
print("average time taken by rabin_karp to match: ", sum_rabin_karp/t)
plt.plot(k, 'r--', r, 'g--')
red_patch = mpatches.Patch(color='red', label='KMP')
green_patch = mpatches.Patch(color='green', label='Rabin Karp')
plt.legend(handles=[red_patch, green_patch])
plt.xlabel('Iterations')
plt.ylabel('time taken (t)')

plt.show()                


