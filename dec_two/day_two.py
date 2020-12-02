import csv

# part 1

with open('pass.csv') as data:
    reader = csv.reader(data, delimiter=' ')

    rentalCount = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]

        #get the range for the quota
        # 'a-b'
        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])

        count = 0
        for character in pw:
            if character == letter:
                count += 1

        if count >= lower and count <= upper:
            rentalCount += 1
   #Part 2

with open('pass.csv') as data:
    reader = csv.reader(data, delimiter=' ')

    validCount = 0
    for row in reader:
        quota, letter, pw = row[0], row[1][0], row[2]

        #get the range for the quota
        # 'a-b'
        i = quota.index('-')
        lower = int(quota[:i])
        upper = int(quota[i+1:])


        first = pw[lower-1] == letter
        last = pw[upper-1] == letter

        if (first and not last) or (last and not first):
            validCount += 1

print(rentalCount)
print(validCount)
