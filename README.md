
## Інтеграл обчислюється на проміжку \([0, 2]\).  

## Алгоритм

1. **Метод Монте-Карло**:
   - Генеруються випадкові точки в межах \([a, b]\).
   - Обчислюється середнє значення функції в цих точках.
   - Інтеграл знаходиться як добуток середнього значення функції на довжину відрізка.  

2. **Метод `quad` з SciPy**:
   - Використовується вбудована функція `quad`, що забезпечує високу точність обчислення інтегралів.

## Результати

### Інтеграл за допомогою `quad`:
- Результат: **0.8820813907624215**
- Похибка: **9.793070696178202e-15**

### Інтеграл за допомогою методу Монте-Карло:
- Результат: **0.8898048023962835**

### Похибка Монте-Карло:
- Похибка: **0.007723411633861921**

## Висновки

1. **Точність методів**:
   - Метод `quad` демонструє вкрай високу точність, з похибкою близько \( 10^{-15} \), що підтверджує його надійність для точного обчислення визначених інтегралів.
   - Метод Монте-Карло має більшу похибку \( \approx 0.0077 \), що обумовлено випадковим характером цього методу.  

2. **Метод Монте-Карло**:
   - Метод підходить для обчислення інтегралів функцій, де неможливо застосувати аналітичний підхід.
   - Точність Монте-Карло залежить від кількості випадкових точок: більше точок дає меншу похибку.  

3. **Порівняння результатів**:
   - Хоча метод Монте-Карло показує результат, близький до аналітичного, похибка у нього більша.
   - Використання Монте-Карло доцільне для складних інтегралів, де метод `quad` не підходить.  