# Selection sort
# every iteration -> one element compared with every other to find smallest -> place in first positions, then in second position, repeat
# rearrange in-place to save on space
# O(n^2)
# not a stable sort, equal elements might be re-arranged


# compare 15 with all other elements, pcick the smallest one
# place at front of array, swop the 15 with 11
# shift search area plus one, so start at 32 -> to end 

nums = [15,32,26,11,36,19,42,44,14]
testsortednums = [11,14,15,19,26,32,36,42,44]

def selectionsort(nums):
  for i in range(len(nums) - 1):
    minIdx = i
    for j in range(i + 1,len(nums)):
      if nums[j] < nums[minIdx]:
        minIdx = j
    nums[i], nums[minIdx] = nums[minIdx], nums[i]
  return nums
  
  

assert(selectionsort(nums) == testsortednums)
  
# Bubble sort
#===================================================
nums = [15,32,26,11,36,19,42,44,14]

# Iterate through list
# compare first two elements, which is larger, move it to the right
# move one, compare next two elements, move or swop positions to get biggest element to the right
# Keep bubbling up the biggest element.
# once biggest element to the right, repeat, the process, untill all elements are sorted
# O(n^2) but its a stable sort, same values will not be swapped., O(1) space

nums = [15,32,26,11,36,19,42,44,14]
testsortednums = [11,14,15,19,26,32,36,42,44]

def bubblesort(nums):

  for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
  return nums    
    
print(bubblesort(nums))
assert(bubblesort(nums) == testsortednums)






