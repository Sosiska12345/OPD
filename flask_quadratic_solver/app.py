from flask import Flask, render_template, request
import math

app = Flask(__name__)
#Создаёт экземпляр Flask-приложения. __name__ указывает Flask, где искать другие файлы, например, шаблоны.

@app.route('/') #Указывает, что функция ниже будет выполняться, когда пользователь откроет главную страницу сайта (/).
def index():
    return render_template('index.html', result=None)
#Возвращает HTML-страницу index.html и передаёт в неё значение result=None.

@app.route('/solve', methods=['POST'])
#Указывает, что следующая функция будет обрабатывать POST-запрос (отправку формы) по адресу /solve.

def contacts ():
    return render_template('c.html', result=None)

def solve():
    try:
#Начинаем блок try, чтобы ловить возможные ошибки при вводе
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
#Используется request.form.get() для безопасного доступа.
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            result = f"Два корня: x₁ = {root1:.2f}, x₂ = {root2:.2f}"
        elif discriminant == 0:
            root = -b / (2*a)
            result = f"Один корень: x = {root:.2f}"
        else:
            result = "Нет действительных корней"
    except Exception as e:
        result = f"Ошибка: {e}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
