import sys
from collections import defaultdict

input = sys.stdin.readline

n, q = map(int,input().split())
index = set()

update = []
for i in range(n):
	l, r, v = map(int,input().split())
	index.add(l)
	index.add(r)
	update.append([l, r, v])

query = []
for i in range(q):
	l, r= map(int,input().split())
	index.add(l)
	index.add(r)
	query.append([l, r])

#sorting to remove the gaps between two indexes
index = sorted(list(index))

#combining indexes to their new index
sortedIndex = defaultdict(int)
for i in range(len(index)):
	sortedIndex[index[i]] = i

#adding values in lower and upper bound of a range
populatedArray = [0]*(len(index))
for i in range(n):
	l, r, v = update[i]
	populatedArray[sortedIndex[l]]+=v
	populatedArray[sortedIndex[r]]-=v

#populating the array
for i in range(1,len(populatedArray)):
	populatedArray[i] += (populatedArray[i-1])

#as the array is compressed, indexes that were removed, those index's values must be included
compressedPopulatedArray = populatedArray[::]
for i in range(1,len(populatedArray)):
	#adding previous index's value multiplied by number of removed indexes in the gap, to right-index
	compressedPopulatedArray[i] += (populatedArray[i-1])*(index[i]-index[i-1]-1)

#simple prefix sum
prefixSum = [0]
for i in range(len(index)):
	prefixSum.append(prefixSum[i]+compressedPopulatedArray[i])

result = []
#final query
for i in range(q):
	l, r = query[i]
	#prefixSum array has a '0' in the beginning, that's why +1 for the correct index

	result.append(str(prefixSum[sortedIndex[r]+1]-prefixSum[sortedIndex[l]+1]-populatedArray[sortedIndex[r]]+populatedArray[sortedIndex[l]]))
	#As the compressed values are added to r-index, so the r-index is included in the prefixSum . 
	# But query wanted (l<=i<r), so the exact value of the r-index from the
	#original array(populatedArray) is subtracted.
	
	#Again, as the compressed values are added to r-index, when in query it becomes the l-index, using 
	# normal way of prefixSum range query will result the extra compressed values added in the result.
	# that's why instead of taking the previous index of l-index, the l-index itself was taken here.
	# but that raises another problem, that the exact value of l-index gets subtracted which should be in the result
	# that is why the exact value of l-index from the original array(populatedArray) is added#

print("\n".join(result))