nums = []
print(len(nums))

while len(nums) <= 10 ** 9 or len(nums) < 2:
    q_num = input('Number (or q to quit) = ')
    if q_num == 'q':
        break
    elif int(q_num) >= 10 ** 9 or -10 ** 9 >= int(q_num):
        print(f"Value not correct, please pick between {-10 ** 9} - {10 ** 9}")
    else:
        nums.append(q_num)


print(nums)
# end while loop
# procures the target number
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


