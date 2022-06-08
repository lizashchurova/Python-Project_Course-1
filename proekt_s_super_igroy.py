import random

questions = ("Где в Древней Греции можно было увидеть надпись: 'Здесь \
живут мертвые, и говорят немые'?", "Что означает аббревиатура «имхо», \
которая часто встречается в интернет-общении?", "Сколько морей омывают \
Балканский полуостров?", "Каким символом в таблице Менделеева обозначается \
мышьяк?", "Какое событие произошло 14 июля 1789 года?", "Кто совершил первое \
кругосветное путешествие?", "Кого или что изучает герпетолог?", \
"Кто написал “Сотворение Адама”?")

keys = {"Где в Древней Греции можно было увидеть надпись: 'Здесь \
живут мертвые, и говорят немые'?": "На кладбище/В библиотеках/В тюрьмах/В больницах",\
"Что означает аббревиатура «ИМХО», которая часто встречается в интернет-общении?": \
"Несмотря на авторитеты/Уточняя подробности/По моему мнению/Вопреки вышеизложенному", \
"Сколько морей омывают Балканский полуостров?": "3/4/5/6", "Каким символом в таблице \
Менделеева обозначается мышьяк?": "Ms/As/HI/Mt", "Какое событие произошло 14 июля \
1789 года?": "Великая английская революция/Захват Цейлона англичанами/Термидорианский\
 переворот/Великая французская революция", "Кто совершил первое кругосветное путешествие?":\
"Фернан Магеллан/Васко да Гама/Джеймс Кук/Христофор Колумб", "Кого или что изучает герпетолог?":\
"Бабочек/Черепах/Лекарственные травы/Герпес", "Кто написал 'Сотворение Адама'?":\
"Микеланджело/Боттичелли/Тициан/Рафаэль"}


def intro():
    print("\t", "Привет, мой милый друг! И добро пожаловать на новую \
и продвинутую игру 'Кто хочет стать миллионером?'. Я - новый ведущий \
этой замечательной программы. Моё имя Владимир Владимирович, но для \
вас я Господин На Века.", "\n\t", "У вас всегда есть возможность взять \
подсказку или сдаться и забрать деньги. Приступим?")
    name = input("Введите ваше имя: ")
    print("Добро пожаловать в игру, ", name)


def answers(key, value):
    print("\n", key)
    v = value.split("/")
    n = 1
    for i in v:
        if n == 1:
            print("А)", i, end="\t\t")
            n += 1
        elif n == 2:
            print("Б)", i, end="\n")
            n += 1
        elif n == 3:
            print("В)", i, end="\t\t")
            n += 1
        elif n == 4:
            print("Г)", i, end="\n")

    
def right_answer(key, value):
    right = {"Где в Древней Греции можно было увидеть надпись: \
'Здесь живут мертвые, и говорят немые'?": "В библиотеках", \
"Что означает аббревиатура «ИМХО», которая часто встречается \
в интернет-общении?": "По моему мнению", "Сколько морей омывают \
Балканский полуостров?": "6", "Каким символом в таблице Менделеева \
обозначается мышьяк?": "As", "Какое событие произошло 14 июля 1789 года?": \
"Великая французская революция", "Кто совершил первое кругосветное путешествие?":\
"Фернан Магеллан", "Кого или что изучает герпетолог?": "Черепах", \
"Кто написал 'Сотворение Адама'?": "Микеланджело"}
    v = value.split("/")
    for i in v:
        if i == right[key]:
            right_word = i
            return right_word

def fifty(right_word, value):
    v = value.split("/")
    fifty = []
    second = random.choice(v)
    if second == right_word:
        second = random.choice(v)
    fifty.append(second)
    print(random.choice(fifty), "\n\t\t", right_word)


def mistake(right_word, help_me):
    answer = input("Введите ваш крутой ответ: ")
    if answer == right_word:
        print("Правильный ответ!")
        return "+"
    if not answer == right_word:
        print("Вы проиграли! Удачи!")

        

def help_me(fifty, mistake, right_word, value):
    answer = input("Хотите подсказку? ")
    if answer.lower() == "да":
        choice = input("Какую подсказку: 50/50, звонок другу, право на ошибку? ")
        choice.lower()
        if choice == "50/50":
            return "50/50"
        if choice == "право на ошибку":
            return "mistake"
        if choice == "звонок другу":
            return "call"
            
            
def player_answer(right_word, help_me):
    answer = input("Введите ваш ответ: ")
    if answer == right_word:
        print("Правильно!")
        return "+"
    if not answer == right_word:
        print("Вы проиграли.")
        return "-"

def take_money():
    desition = input("Хотите закончить игру и забрать деньги? ")
    desition.lower()
    if desition == "да":
        return "-"
    else:
        pass

def super_game():
    questions_sg = ("Как дела?", "Ты норм?")
    right_sg = {"Как дела?": "Отлично", "Ты норм?": "Да"}
    for k, v in right_sg.items():
        print(k)
        answer = input("Ваш ответ: ")
        if answer == v:
            print("Правильно!")
            pass
        else:
            print("Вы проиграли!")
            break
                    

def main():
    intro()
    money = 0
    n = 0
    m = 0
    for key, value in keys.items():
        
        answers(key, value)
        right_word = right_answer(key, value)
        h_m = help_me(fifty, mistake, right_word, value)
        if h_m == "50/50" and m == 1:
            print("Вы уже использовали эту подсказку!")
            h_m = help_me(fifty, mistake, right_word, value)
        if h_m == "50/50" and m == 0:
            fifty(right_word, value)
            m = 1


        p_a = player_answer(right_word, help_me)

        if h_m == "mistake" and n == 1:
            print("Вы уже использовали эту подсказку!")
            help_me(fifty, mistake, right_word, value)
        if h_m == "mistake" and n == 0 and p_a == "-":
            mis = mistake(right_word, help_me)
            n = 1
        
       
        if p_a == "+" or mis == "+":
            money += 100000
            print("Ваши деньги:", money, "рублей.", "\n")
            if money == 500000:
                des = input("Хотите сыграть в супер игру? Поставить свои 500.000 \
рублей и удвоить сумму в случае победы? ")
                des.lower()
                if des == "да":
                    super_game()
                    break
                else:
                    pass
            pass
        else:
            break
        t_m = take_money()
        if t_m:
            print("Поздравляю, ваш выигрыш: ", money, "рублей. До свидания!")
            break


if __name__ == "__main__":
    main()

