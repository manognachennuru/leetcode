`first solution` - timeout , but own implementation
`second solution` - two strings are anagrams if their sorted strings are same , so we need to store all corresponding strings which have same sorted string
for that we use a dictionary (called opdict here) where keys are sorted strings and values are corresponding strs[i] 's
​
as sorted(strs) returns a list and keys in dictionary cannot be lists , we join the charectors as a single string using join method(in a variable named p)
​
​
`for third solution `- we can alsoconvert sorted str(which returns list) to tuple and store tuples as keys
​
​
when tuple not in op we insert a key named our tuple and add values , else we directly append new value to the old value(which is a list)