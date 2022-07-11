E = {1,2,3,4,5}
N = {4,8,0,6,2}

# union of two set
union = E.union(N)
print(union)

#intersection of two set
intersection = E.intersection(N)
print(intersection)

#difference of two set
difference = N.difference(E)
print(difference)

#symmetric difference of two set
difference1 = N.symmetric_difference(E)
print(difference1)