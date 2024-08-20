def finbonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = finbonacci(n-1,memo) + finbonacci(n-2, memo)
    return memo[n]

# test the function
print(finbonacci(10)) # output: 55