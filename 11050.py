# 문제
# 자연수 N 과 정수 K가 주어졌을 때 이항계수 (N K)를 구하는 프로그램을 작성하시오


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def binomial_coefficient(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def main():
    [n, k] = [int(item) for item in input("input N, K : ").split()]

    print(binomial_coefficient(n, k))

main()