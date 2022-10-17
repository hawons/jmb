## code 17.1
# 주어진 list의 부분합 계산
def partialSum(a: list):
    ret = list(a.size())
    ret[0] = a[0]
    for i in range(0, a.size()):
        ret[i] = ret[i-1] + a[i]
    return ret

# 어떤 list의 부분합이 주어졌을 때, 원래 list의 a~b까지 합 계산
def rangeSum(psum: list, a: int, b: int):
    if a == 0:
        return psum[b]
    return psum[b] - psum[a-1]


## code 17.2
# list의 부분합과 제곱의 부분합을 입력으로 특정 구간의 분산 계산 함수
def variance(sqpsum: list, psum: list, a: int, b: int):
    mean = rangeSum(psum, a, b) / (b - a + 1)
    ret = rangeSum(sqpsum, a, b) - 2 * mean * rangeSum(psum, a, b) + (b - a + 1) * mean * mean
    return ret / (b - a + 1)


## code 17.3
# 부분합 이용 2차원 list 구간합 계산 함수
def gridSum(psum: list, y1: int, x1: int, y2: int, x2: int):
    ret = psum[y2][x2]
    if y1 > 0: 
        ret -= psum[y1-1][x2]
    elif x1 > 0:
        ret -= psum[y2][x1-1]
    elif y1 > 0 and x1 > 0:
        ret += psum[y1-1][x1-1]
    return ret

