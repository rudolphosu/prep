def solution(amount,coins,memo):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0

    if memo[amount] > 0:
        return memo[amount]

    sum = 0
    for coin in coins:
        sum += solution(amount - coin,coins,memo)
    memo[amount] = sum
    return memo[amount]



def main():
    amount = 10
    coins = [1,5,10,25]
    memo = [0 for i in range(amount+1)]
    print solution(amount,coins,memo)

if __name__ == '__main__':
    main()
