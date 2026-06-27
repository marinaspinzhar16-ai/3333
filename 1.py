import time

COINS = [50, 25, 10, 5, 2, 1]


# Жадібний алгоритм
def find_coins_greedy(amount):
    result = {}

    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result


# Динамічне програмування
def find_min_coins(amount):
    # Мінімальна кількість монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Запам'ятовуємо останню використану монету
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлення відповіді
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return dict(sorted(result.items()))


# Приклад роботи
amount = 113

print("Жадібний алгоритм:")
print(find_coins_greedy(amount))

print("\nДинамічне програмування:")
print(find_min_coins(amount))


# Порівняння часу
amount = 100000

start = time.perf_counter()
find_coins_greedy(amount)
greedy_time = time.perf_counter() - start

start = time.perf_counter()
find_min_coins(amount)
dp_time = time.perf_counter() - start

print(f"\nGreedy: {greedy_time:.6f} сек.")
print(f"Dynamic Programming: {dp_time:.6f} сек.")
