with open('nums.txt') as f:
    lines = f.readlines()

nums = [ int(line.strip()) for line in lines]

#Part 1
def expense_report_one(nums, target):
    greatest_exp = -1
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            num1 = nums[i]
            num2 = nums[j]

            if num1+num2 == target:
                expense = num1 * num2

                if expense > greatest_exp:
                    greatest_exp = expense

    print(greatest_exp)

#Part 2
def expense_report_two(nums, target):
    greatest_exp  = 1
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                num1, num2, num3 = nums[i], nums[j], nums[k]

                if num1+num2+num3 == target:
                    expense = num1 * num2 * num3

                    if expense > greatest_exp:
                        greatest_exp = expense

    print(greatest_exp)

expense_report_one(nums, 2020)
expense_report_two(nums, 2020)
