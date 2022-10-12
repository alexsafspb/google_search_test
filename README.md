# selenium + pytest test task
## Условия задания
  На стеке python/pytest/selenium сделать проект
## Написать тест  
 1) открыть страницу google.com
 2) отправить запрос на поиск сайта Think24.ru
 3) в результатах запроса на странице ответа Google найти сайт
 4) перейти на сайт (открыть его) нажав на ссылку в результатах поиска.

### Установка
Для работы необходимы Chrome и chromedriver.  

Установка зависимостей
```
pip install -r requirements.txt 
```
затем установка selenium-chromedriver
```
python3 -m selenium-chromedriver
```
NB! автоматически установленный chromedriver 
    может не соответствовать версии Chrome.  
    В этом случае необходима ручная установка.  
Версия Chome определяется как 
```
google-chrome --version
```
Последнее число в версии может не совпадать с версией chromedriver на сайте
https://sites.google.com/chromium.org/driver/downloads  

После определения нужной версии selenium-chromedriver по версии Chrome его нужно скачать, 
разархивировать и скопировать в /usr/bin

### Установка remote selenium chrome webdriver (docker-compose)
```
docker-compose up
после успешного запуска прервать процесс
docker-compose start
```


## Запуск тестов
1) Локальный Chrome и webdriver
``` 
pytest -v  test.py
```
2) Remote Chrome webdriver (используя docker-compose )

``` 
pytest -v  test.py --remote
```

3) Запуск тестов с отчетом в html
```
pytest --html=report.html --self-contained-html -v test.py --remote
```
