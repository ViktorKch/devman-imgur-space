# Космический Imgur

Данный проект создан для загрузки фотографий, связанных с космосом, и публикации их на сайте [Imgur](https://imgur.com/)

Фотографии загружаются из открытых источников, при помощи API этих источников. В данном проекте используются два источника:
[SpaceX REST API](https://github.com/r-spacex/SpaceX-API) (фотографии последнего запуска). А также [Hubble API](http://hubblesite.org/api/documentation). В Hubble API есть подборки фотографий по коллекциям, в данном случае загружаются фотографии из коллекции [stsci_gallery](http://hubblesite.org/api/v3/images?page=all&collection_name=stsci_gallery). 

Публикация фотографий на сервисе [Imgur](https://imgur.com/) при помощи их API.


### Как установить

API SpaceX и Hubble являются публичными и не требуют ключа. 

Для использования API Imgur нужно создать приложение и получить свой `client-id` и `client-secret`.

[Создать приложение](https://api.imgur.com/oauth2/addclient)
    - В поле `Authorization callback URL` напишите `http://localhost`
  
Далее в папке проекта необходимо создать файл `.env` и в нем сохранить `client-id` и `client-secret` в переменных `CLIENT_ID`
и `CLIENT_SECRET` соответственно.  

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).