
number = int(input("Введіть трицифрове число: ")) # Отримуємо трицифрове число від користувача
first_digit = number // 100 # Знаходимо першу цифру (ділення націло на 100)
last_digit = number % 10 # Знаходимо останню цифру (остача від ділення на 10)
if first_digit == last_digit:       # Перевіряємо, чи рівні ці цифри
    print("Число є паліндромом")
else:
    print("Число не є паліндромом")
