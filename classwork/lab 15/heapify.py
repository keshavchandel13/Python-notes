import heapq
lst = [100,19,36,17,3,25,1,2,7,2]

print(f"List before heapify: {lst}")
heapq.heapify(lst)
print(f"Heapified list: {lst}")
heapq.heappush(lst,69)
print("The heap after the addition of new element: ",lst)


