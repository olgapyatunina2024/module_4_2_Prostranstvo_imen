def test_function ():

    def inner_function():
        print ('Я нахожусь в области видимости функции test_function')

        inner_function()  # ничего не возвращает

    # внутренняя функция не работает
    # Вызов функции inner_function() вне функции test_function приводит к ошибке
    # имя inner_function не определено из-за разницы в пространстве имён, нельзя получить значения внутри функции извне

    test_function()  # работает

  