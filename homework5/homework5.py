sum = 0

while True:
    user_input = input("Введите число или 'stop'/'end' для завершения: ")
    
    if user_input.lower() in ['stop', 'end']:
        
        break
    sum = sum+int(user_input)    
print(f"Сумма введенных чисел: {sum}")
