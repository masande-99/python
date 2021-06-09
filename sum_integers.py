score_1 = int(input("Please enter the first score : "))
score_2 = int(input("Please enter the second score : "))
score_3 = int(input("Please enter the third score : "))


def sum_numbers():
    sum = score_1 + score_2 + score_3

    if score_1 == score_2 or score_2 == score_3 or score_3 == score_1:
        print(0)
    else:
        print(sum)


sum_numbers()
