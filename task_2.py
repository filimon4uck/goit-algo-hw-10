import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення нової функції
def f(x):
    return np.exp(-(x**2))


# Межі інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, "r", linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color="gray", alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color="gray", linestyle="--")
ax.axvline(x=b, color="gray", linestyle="--")
ax.set_title(f"Графік інтегрування f(x) = e^(-x^2) від {a} до {b}")
plt.grid()
plt.show()

# Обчислення інтеграла за допомогою функції quad (аналітичний результат)
result_quad, error_quad = spi.quad(f, a, b)
print(f"Інтеграл (метод quad): {result_quad}, похибка: {error_quad}")


# Метод Монте-Карло для обчислення визначеного інтеграла
def monte_carlo_integration(f, a, b, n):
    # Генерація випадкових точок
    x_random = np.random.uniform(a, b, n)
    y_random = f(x_random)

    # Обчислення середнього значення функції
    integral = (b - a) * np.mean(y_random)
    return integral


# Виконання обчислення інтегралу методом Монте-Карло з n = 10000 точок
n = 10000
result_monte_carlo = monte_carlo_integration(f, a, b, n)
print(f"Інтеграл (метод Монте-Карло): {result_monte_carlo}")

# Порівняння результатів
error_monte_carlo = abs(result_quad - result_monte_carlo)
print(f"Похибка Монте-Карло: {error_monte_carlo}")
