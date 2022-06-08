import random
import time


def intro():
    print("Привет, мой милый друг! И добро пожаловать на новую \
и продвинутую игру 'Кто хочет стать миллионером?'. Я - новый ведущий \
этой замечательной программы. Моё имя Владимир Владимирович, но для \
вас я Господин На Века.", "\n\t", "У вас всегда есть возможность взять \
подсказку или сдаться и забрать деньги. Приступим?")
    name = input("Введите ваше имя: ")
    print("Добро пожаловать в игру, " + name + '!')
    answer = input('Хотите прочитать правила игры до ее начала? ')
    if answer.lower() == 'да':
        print('\n','Привет!','\n', 'Предлагаем тебе сыграть в игру «Кто хочет стать миллионером?». \
Тебе будут задаваться вопросы, а за каждый правильный ответ на твой счёт будет начисляться по 100 000 рублей.','\n',\
'На каждый вопрос даётся 4 возможных варианта ответа, но правильный только один.','\n',\
'Чтобы ответить на вопрос, напиши букву, под которой написан твой ответ. \
Если ты отвечаешь неверно, твой выигрыш обнуляется и ты покидаешь игру. \
Во время игры ты можешь воспользоваться 3 подсказками: «50/50», «право на ошибку» и «звонок другу». \
Каждой подсказкой можно воспользоваться только один раз.','\n',\
'Подсказка «50/50»: из 4 ответов остаётся только 2, один из которых правильный. \
Тебе нужно выбрать один из оставшихся ответов.','\n',\
'Подсказка «право на ошибку»: если ты отвечаешь на вопрос неправильно, у тебя есть ещё \
одна попытка ответить.','\n',\
'Подсказка «звонок другу»: ты можешь обратиться за помощью к другу (к нашему чат-боту), \
который поможет ответить тебе на вопрос правильно.','\n',\
'В случае, если ты ответил правильно на 5 вопросов, тебе будет предложено сыграть \
в суперигру, где ты сможешь утроить свой выигрыш и забрать 1 500 000 рублей.', '\n',\
'В суперигре задаются вопросы без вариантов ответов. Тебе нужно будет самому написать \
правильный ответ. В случае ошибки твой выигрыш обнуляется и ты покидаешь игру.','\n',\
'Если ты не хочешь принимать участие в суперигре, можно продолжить играть на уровне \
с вариантами ответа и выиграть 1 000 000 рублей.','\n',\
'Удачи!')
    time.sleep(3)
    return name

def open_file():
    with open('вопросы.txt', encoding="utf-8") as file:
        lines = file.readlines()
        random_lines = []
        for i in range(1, 11):
            rand_ques = random.choice(lines)
            random_lines.append(rand_ques)
            i += 1
        questions = {}
        for line in random_lines:
            ques, ans = line.split("|")
            ans = ans.replace("\n", "")
            questions[ques] = ans
        return questions

def open_right():
    with open("прав ответ.txt", encoding="utf-8") as file_right:
        lines = file_right.readlines()
        right_answers = {}
        for line in lines:
            ques, ans = line.split("|")
            ans = ans.replace("\n", "")
            right_answers[ques] = ans
        return right_answers

def open_help():
    with open("помощь друга.txt", encoding="utf-8") as file_help:
        lines = file_help.readlines()
        friend_answer = {}
        for line in lines:
            ques, ans = line.split("|")
            ans = ans.replace("\n", "")
            friend_answer[ques] = ans
        return friend_answer

def answers(key, value):
    print("\n", key)
    values = value.split(", ")
    print('{}\t\t\t{}'.format(values[0], values[1]))
    print('{}\t\t\t{}'.format(values[2], values[3]))

    
def right_answer(key, right_answers):
    for akey, avalue in right_answers.items():
        if key == akey:
            right_word = avalue
            return right_word


def fifty(right_word, value):
    values = value.split(", ")
    fifty = []
    for i in values:
        if i.startswith(right_word):
            first = i
        else:
            fifty.append(i)
    two = [random.choice(fifty), first]
    two.sort()
    if two[0].startswith('А') and two[1].startswith('Б'):
        print(two[0] + '\t\t\t' + two[1])
    elif two[0].startswith('В') and two[1].startswith('Г'):
        print('\n' + two[0] + '\t\t\t' + two[1])
    else:
        for each in two:
            if each.startswith('А'):
                print(each)
            elif each.startswith('Б'):
                print('\t\t\t', each)
            elif each.startswith('В'):
                print(each)
            elif each.startswith('Г'):
                print('\t\t\t', each)


def question_friend(name):
    print('\n', 'Calling...', '\n')
    time.sleep(5)
    print('Иосиф: Привет!')
    time.sleep(2)
    input(name + ': ')
    time.sleep(3)
    print('Иосиф: Я знаю, что ты на игре "Кто хочет стать миллионером?". Я очень \
рад, что ты позвонил именно мне. Чем я могу тебе помочь?')
    question = ''
    while question == '':
        time.sleep(2)
        question = input(name + ' (задайте ваш вопрос): ')
        if question == '':
            print('Ты не задал вопрос :(')
    return question


def answer_friend(question, friend_answer):
    for key, value in friend_answer.items():
        if question == key:
            time.sleep(3)
            print('Иосиф: ', value)


def help_me(fifty, right_word, value, name, hint, hints):
    
    answer = input("Хотите подсказку? ")
    if answer.lower() == "да":
        choice = input(hint)
        if choice.lower() == "50/50":
            fifty(right_word, value)
            hints.append('fifty')
            return "50/50"
        if choice.lower() == "право на ошибку":
            hints.append('mistake')
            return "mistake"
        if choice.lower() == "звонок другу":
            hints.append('call')
            q_f = question_friend(name)
            f_a = open_help()
            answer_friend(q_f, f_a)
            return "call"
            
            
def player_answer(right_word, help_me):
    answer = input("Введите ваш ответ: ")
    time.sleep(5)
    if answer == right_word:
        print('\n' + "Правильно!")
        return "+"
    if not answer == right_word:
        print('\n', "К сожалению, вы проиграли.")
        return "-"


def take_money():
    desition = input("Хотите закончить игру и забрать деньги? ")
    if desition.lower() == "да":
        return "-"
    else:
        pass


def super_game():
    with open("суперигра.txt", encoding="utf-8") as file_super:
        lines = file_super.readlines()
        super_game = {}
        for line in lines:
            ques, ans = line.split("|")
            ans = ans.replace("\n", "")
            super_game[ques] = ans
    
    for k, v in super_game.items():
        print("\n", k)
        answer = input("Ваш ответ: ")
        if answer == v:
            print("Правильно!")
            pass
        else:
            print("Неправильный ответ!")
            return "-"
            break
                    

def main():
    name = intro()
    money = 0
    hints = []
    
    questions = open_file()
    right_answers = open_right()
    friend_answer = open_help()
    hint = 'Какую подсказку: 50/50, звонок другу, право на ошибку? '

    for key, value in questions.items():
        answers(key, value)
        right_word = right_answer(key, right_answers)
        h_m = help_me(fifty, right_word, value, name, hint, hints)
        if 'fifty' in hints:
            hint = 'Какую подсказку: звонок другу, право на ошибку? '
        if 'call' in hints:
            hint = 'Какую подсказку: 50/50, право на ошибку? '
        if 'mistake' in hints:
            hint = 'Какую подсказку: 50/50, звонок другу? '
        if 'fifty' in hints and 'call' in hints:
            hint = 'Какую подсказку: право на ошибку? '
        if 'fifty' in hints and 'mistake' in hints:
            hint = 'Какую подсказку: звонок другу? '
        if 'call' in hints and 'mistake' in hints:
            hint = 'Какую подсказку: 50/50? '
        if 'fifty' in hints and 'mistake' in hints and 'call' in hints:
            hint = 'Вы больше не можете пользоваться подсказками! '
        p_a = player_answer(right_word, help_me)

        if h_m == "mistake" and p_a == "-":
            print("Попробуйте еще раз!")
            p_a = player_answer(right_word, help_me)

        if p_a == "+":
            money += 100000
            print("Ваши деньги:", money, "рублей.", "\n")
            if money == 500000:
                des = input("Хотите сыграть в суперигру? Поставить свои 500.000 \
рублей и утроить сумму в случае победы? ")
                if des.lower() == "да":
                    s_g = super_game()
                    if s_g == "-":
                        print("О нет! Вы проиграли! Не растраивайтесь, может в \
следующий раз вам повезет!")
                        break
                    else:
                        print("Поздравляю! Вы выиграли 1,5 миллиона рублей!")
                        break
                else:
                    pass
            if money < 1000000:
                t_m = take_money()
                if t_m:
                    print("Поздравляю, ваш выигрыш: ", money, "рублей. До свидания!")
                    break
            if money == 1000000:
                print("Невероятно! Вы только что выиграли в игру 'Кто хочет стать миллионером?' \
не 200 тысяч, не 500 тысяч, а целый 1 миллион рублей! Вы стали сильнее, мудрее и определенно \
богаче! Был очень рад с вами познакомиться, до свиданья!")
                break
        else:
            print('\n', 'Правильный ответ был:')
            value = value.split(", ")
            for i in value:
                if i.startswith(right_word):
                    right_word = i
            if right_word.startswith('А'):
                print(right_word, '\n')
            if right_word.startswith('Б'):
                print('\t\t', right_word, '\n')
            if right_word.startswith('В'):
                print('\n', right_word)
            if right_word.startswith('Г'):
                print('\n\t\t', right_word)
            break
        


if __name__ == "__main__":
    main()
