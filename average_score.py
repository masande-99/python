score_1 = int(input("Please enter the first score : "))
score_2 = int(input("Please enter the second score : "))
score_3 = int(input("Please enter the third score : "))

sum = score_1 + score_2 + score_3
print(sum)
average = sum / 3

message = "The average of " + str(sum) + " is "

print(message + str(average))
