all_words = set()
all_words = {'фигура', 'афроамереканцы', 'геометрия', 'информатика', 'высота','иллюминация', 'собака', 'череп', 'дрозд', 'солнце'} # Все слова
win = False #Флаг победы
lose = True
count = 0 #Кол-во ходов
word = list(all_words.pop()) # Выбор рандомного слова
lword = list("*" * len(word)) #Создание шаблона для финального слова
used = [] #Список для использованых
unused = set() #Список для не использованных

for i in range(1, 32 + 1): #Добавление всех букв в set 
    unused.add(chr(ord("а") + i))
unused.add("ё")
unused.add("а")
letters = unused

print("Добрый день! Вы играете в ПОЛЕ ЧУДЕС!" "\n" "Удачи!" "\n" "В загаданных словах все буквы маленькие!" "\n" "если вам нужна помошь пишите 'Помощь'")
print("Если вы хотите написать всё слово введите 'Знаю'" "\n")
print("Ваше слово:", "".join(lword), "\n") # Отображение слова

while not win: #Бесконечный цикл
    a = input().lower()
    if a == "помощь": #Вызов команд помощи
        print("Вы вызвали помощь:" "\n" "!1 - показать не использованые буквы")
        print("!2 - показать использованные буквы\n" "!3 - Сдаться\n" "!4 - выход\n")     
        a = input().lower()
    elif a == "знаю": #Проверка на все слово
        print("Вы хотите дать ответ? (Да/Нет)" "\n")
        a = input().lower()
        if a == "да":
            print("Вводите: \n" )
            a = list(input().lower())
            if a == word:
                win = True
                lose = False
                break
            else:
                win = False
                lose = True
                break
        elif a == "нет": #Возвращение в основной цикл
            print("Введите букву: \n")
    elif a == "!1":
        if unused == []:
            print("Вы использовали все буквы")
        else:
            print("Вот ваши не использованые буквы:\n", " ".join(unused))
    elif a == "!2":
        if used == []:
            print("Вы еще не ввели ни одной буквы")
        else:
            print("Вот ваши использованные буквы:\n" " ".join(used))
    elif a == "!3":
        win = False
        lose = True
    elif a == "!4":
        print("Введите букву:\n")
        count += 1
    elif a in used: #Если есть в использованых
        count += 1
        print("Вы уже вводили эту букву!")
    
    elif len(a) != 1 or a not in letters: #Если буква не коректна
        count += 1
        print("Вы не правильно ввели букву!" "\n" "Введите еще раз." "\n")
    
    elif len(a) == 1 and a in letters: #Если буква коректна
        count += 1
        used.append(a) #Добавляем в использованые
        if a in unused: #НА всякий проверяем есть ли он в неиспользованых
            unused.remove(a) #Убираем по значению
        if a in word: # Если буква в слове
            print("Вы угадали букву!")
            for i in range(len(word)): #Проходим по строке, находим, заменяем * на нужное
                if word[i] == a: 
                    lword[i] = word[i]
            print("".join(lword), "\n")
        else:
            print("Такой буквы нет в слове. Попробуй ещё раз!")
    
    if "*" not in lword: #Проверка на победу.
        win = True
        lose = False
    

if win and not lose:
    print("Позравляю! Вы выйграли!", "\n", "Ходов было затрачено:", count, "\n")
else:
    print(a)
    print("Увы, но вы проиграли." "\n" "Спасибо за игру!")