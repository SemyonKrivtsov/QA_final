# QA final project

Проект представляет собой тестирование интернет-магазина store77 с помощью Selenium.
В проекте проверяются три сценария:
- Покупка самого популярного телефона Samsung от выбора до заказа
- Покупка самого популярного телефона Google от выбора до заказа
- Покупка двух упомянутых выше телфеонов

В проекте пользователь авторизируется, по этому необходимо заранее зарагистироваться и ввести свой login и password в `secret.py`.

Для прохождения всех тестов необходимо выполнить команду из корня проекта:
```
python -m pytest -s -v tests\test_buy_product.py
```
