s = ( 1, 2, 3, 4 )
s1 = ( 1, 2)
s2 = (3, 4)

i = 2
j = 4
x = 2
n = 3
step = 2
start = 1
stop = 5
print(x in s)                # True if an item of s is equal to x, else False
print(x not in s)            # False if an item of s is equal to x, else True
print(s1 + s2)               # the concatenation of s1and s2
print(s * n, n*s)              # n copies of s concatenated
print(s[i])                    # i'th item of s, origin 0  (1)
print(s[i:j])                  # Slice of s from i(included) to j(excluded). Optional stepvalue, possibly negative(default: 1).
print(s[i:j:step])
print(s.count(x))              # returns number of i's for which s[i] == x
#print s.index(x[, start[, stop]])     # returns smallest i such that s[i]==x. start and stop limit search to only part of the sequence.
print(len(s))                  # Length of s
print(min(s))                  # Smallest item of s
print(max(s))                  # Largest item of s
print(reversed(s))             # [2.4] Returns an iteratoron sin reverse order. smust be a sequence, not an iterator (use reversed(list(s)) in this case. [PEP 322]

