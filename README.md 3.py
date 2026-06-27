def find_coins_greedy(amount):
    """
    Жадібний алгоритм пошуку мінімальної кількості монет.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result


def find_min_coins(amount):
    """
    Алгоритм динамічного програмування.
    """
    coins = [1, 2, 5, 10, 25, 50]

    # Мінімальна кількість монет для кожної суми
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    # Для відновлення відповіді
    used_coin = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coin[i] = coin

    result = {}
    while amount > 0:
        coin = used_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


if __name__ == "__main__":
    amount = 113

    print("Greedy:")
    print(find_coins_greedy(amount))

    print("\nDynamic programming:")
    print(find_min_coins(amount))
