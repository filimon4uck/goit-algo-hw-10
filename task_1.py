import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Produce", pulp.LpMaximize)

# Визначення змінних
Limonade = pulp.LpVariable("Limonade", lowBound=0, cat="Integer")
Fruit_juice = pulp.LpVariable("Fruit_juice", lowBound=0, cat="Integer")

# Функція цілі (Максимізація виробництва)
model += Limonade + Fruit_juice, "Produce"

# Додавання обмежень
model += 1 * Fruit_juice + 2 * Limonade <= 100
model += 1 * Limonade <= 50
model += 1 * Limonade <= 30
model += 2 * Fruit_juice <= 40
# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти лимонад:", Limonade.varValue)
print("Виробляти фруктовий сік:", Fruit_juice.varValue)
print("Загальне виробництво:", Limonade.varValue + Fruit_juice.varValue)
