# URLSHORTENER

## Содержание

- [Описание](#about)
- [Деплой](#deployment)
- [Использование](#usage)

## Описание <a name = "about"></a>

Тестовый проект для сокращения ссылок, можно было сделать на flask и не тянуть тяжелую джангу для такой простой задачи, но когда уже понял - было поздно. По факту за 15 минут сделано для галочки

## Деплой <a name = "deployment"></a>

### Подготовка

Нам нужен python3 и python3-pip

```
sudo apt install python3
sudo apt install python3-pip
```

### Разворачиваем

```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## Использование <a name = "usage"></a>

Создаем короткую ссылку:
```
http://127.0.0.1:8000/sh/generate/YOUR_LINK
```

В ответ получаем json в ключе data лежит наша короткая ссылка, просто копируем и вставляем в браузер и вас перенаправит на источник
