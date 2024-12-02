f = open("2023/1/input1.txt")

allnums = []

for l in f.readlines():
  i = 0
  ol = l
  nums = []
  while i < len(l):
    if l[i].isdigit():
      nums.append(int(l[i]))
    if l[i:i+len("one")] == "one":
      nums.append(1)
    if l[i:i+len("two")] == "two":
      nums.append(2)
    if l[i:i+len("three")] == "three":
      nums.append(3)
    if l[i:i+len("four")] == "four":
      nums.append(4)
    if l[i:i+len("five")] == "five":
      nums.append(5)
    if l[i:i+len("six")] == "six":
      nums.append(6)
    if l[i:i+len("seven")] == "seven":
      nums.append(7)
    if l[i:i+len("eight")] == "eight":
      nums.append(8)
    if l[i:i+len("nine")] == "nine":
      nums.append(9)

    i += 1

  
  print(ol.strip(),end=" = ")
  print(nums[0]*10 + nums[-1])
  allnums.append(nums[0]*10 + nums[-1])

print(sum(allnums))