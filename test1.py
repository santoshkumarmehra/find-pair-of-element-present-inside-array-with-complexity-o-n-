def findPair(arr,n):
	flag=0
	s=set()
	for ele in arr:
		if ele<0:
			s.add(ele)
	for ele in arr:
		if ele>0:
			if -ele in s:
				flag=1
				print(ele,-ele)
	if flag==0:
		print("no pair exist")

arr=[5,4,-3,2,-5,3]
n=len(arr)
findPair(arr,n)