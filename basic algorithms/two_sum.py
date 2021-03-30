# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

def twoSum(nums, target):
  answer = []

  for num in nums:
    if len(answer) > 0:
      return answer
    else:
      for index in range(len(nums)):
        cur_num_index = nums.index(num)
        if index == cur_num_index:
          continue
        else:
          if num + nums[index] == target:
            answer.append(nums.index(num))
            answer.append(index)
            break

  if len(answer) == 0:
    print('No operation equals the target: ' + str(target))

  return answer


print(twoSum([2, 7, 11, 15], 9))
