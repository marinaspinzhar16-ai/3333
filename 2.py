import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Функція
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# ----------------------------
# Побудова графіка
# ----------------------------
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color='red', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)

ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([-0.5, 2.5])
ax.set_ylim([0, max(y) + 0.5])

ax.axvline(a, color='gray', linestyle='--')
ax.axvline(b, color='gray', linestyle='--')

ax.set_title("Інтегрування функції f(x)=x²")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.grid()
plt.show()

# ----------------------------
# Метод Монте-Карло
# ----------------------------
N = 100000

x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

inside = y_rand <= f(x_rand)

rectangle_area = (b - a) * f(b)

mc_integral = rectangle_area * np.sum(inside) / N

print(f"Інтеграл методом Монте-Карло: {mc_integral}")

# ----------------------------
# Перевірка через scipy.integrate.quad
# ----------------------------
quad_result, error = spi.quad(f, a, b)

print(f"Інтеграл (quad): {quad_result}")
print(f"Оцінка похибки: {error}")

print(f"Абсолютна похибка: {abs(mc_integral - quad_result)}")
