import random
print('Добро пожаловать в числовую угадайку')

def is_valid(upper_limit):

    while True:
        guess = input(f'Введите число от 1 до {upper_limit}: ')
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= upper_limit:
                return guess
            else:
                print(f'Число должно быть в диапазоне от 1 до {upper_limit}.')
        else:
            print('Пожалуйста, введите корректное число.')

def main():

    upper_limit = int(input('Введите верхнюю границу диапазона (число больше 1): '))
    counter = 0
    num = random.randint(1, upper_limit)

    while True:
        guess = is_valid(upper_limit)
        counter += 1
        if guess < num:
            print('Ваше число меньше загаданного, попробуйте еще раз.')
        elif guess > num:
            print('Ваше число больше загаданного, попробуйте еще раз.')
        else:
            print(f'Поздравляем! Вы угадали число {num} за {counter} попыток.')
            break

main()

while True:
    play_again = input('Хотите сыграть еще раз? (да/нет): ').strip().lower()
    if play_again == 'да':
        main()
    elif play_again == 'нет':
        break
    else:
        print('Пожалуйста, введите "да" или "нет".')


print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


