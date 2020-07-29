# using python3

def MaxSalary(digits):
    answer = []
    while len(digits) > 0:
        maximum = 0
        for i in digits:
            if i >= maximum:
                maximum = i
        answer.append(maximum)
        digits.remove(maximum)
    return answer


n = int(input())
digits = list(map(int, input().split()))
result = MaxSalary(digits)
print(result)
