nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numL = len(nums)

b = int(input('Target value = '))
if -10 ** 9 <= int(b) <= 10 ** 9:
    target = b
# Calculation:runs through the list to see what two numbers add up to the target
    a = 1
while a < 10:
    for a in nums:
        if nums[a-1] + nums[a] == target:
            nums = [a-1,a]
            print(nums)
            break
        elif nums[a-1] + nums[a] != target:
            a += 1
            continue
        else:
            print("There are no numbers that equal your number ", target)
            break
    break

