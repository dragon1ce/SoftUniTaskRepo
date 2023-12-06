def negative_vs_positive(strng):
    nums = [int(x) for x in strng.split()]
    pos = []
    neg = []
    for num in nums:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
    neg_sum = sum(neg)
    pos_sum = sum(pos)
    print(neg_sum)
    print(pos_sum)
    if abs(neg_sum) > pos_sum:
        print("The negatives are stronger than the positives")
    elif abs(neg_sum) < pos_sum:
        print("The positives are stronger than the negatives")


a = input()
negative_vs_positive(a)
