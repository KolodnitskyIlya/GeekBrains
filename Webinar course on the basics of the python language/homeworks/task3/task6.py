''' 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func(). '''

def int_func(word):
    return word.title()

def int_func1(word):
    int_list = word.split()
    text = ""
    for item in int_list:
        slem = ''
        for i in range(len(item)):
            if i == 0:
                slem += item[i].upper()
            else:
                slem += item[i]
        text += slem + " "
    return text[0:-1]

print(int_func('text is my favorite'))
print(int_func1('text is my favorite'))

