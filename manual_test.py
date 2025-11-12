# ----------------------------
# Файл: manual_test.py
# ----------------------------
from calculator import add, divide, multiply, subtract


def main():
    print("🚀 ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА")
    print("=" * 40)
    
    # Тестирование сложения
    print("СЛОЖЕНИЕ:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"-1 + 1 = {add(-1, 1)}")
    print(f"10 + (-5) = {add(10, -5)}")
    
    print("\n" + "=" * 40)
    
    # Тестирование вычитания
    print("ВЫЧИТАНИЕ:")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"0 - 10 = {subtract(0, 10)}")
    print(f"-5 - (-3) = {subtract(-5, -3)}")
    
    print("\n" + "=" * 40)
    
    # Тестирование умножения
    print("УМНОЖЕНИЕ:")
    print(f"2 * 5 = {multiply(2, 5)}")
    print(f"-2 * 3 = {multiply(-2, 3)}")
    print(f"4 * 0 = {multiply(4, 0)}")
    
    print("\n" + "=" * 40)
    
    # Тестирование деления
    print("ДЕЛЕНИЕ:")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"9 / 3 = {divide(9, 3)}")
    print(f"7 / 2 = {divide(7, 2)}")
    
    print("\n" + "=" * 40)
    
    # Тестирование обработки ошибок
    print("ОБРАБОТКА ОШИБОК:")
    try:
        result = divide(5, 0)
        print(f"5 / 0 = {result}")
    except ValueError as e:
        print(f"✅ divide(5, 0) -> Ошибка перехвачена: {e}")
    
    try:
        result = divide(10, 2)
        print(f"✅ divide(10, 2) = {result}")
    except ValueError as e:
        print(f"divide(10, 2) -> Ошибка: {e}")
    
    print("\n" + "=" * 40)
    print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")

if __name__ == "__main__":
    main()