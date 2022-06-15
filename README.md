# Телеграм-бот для скачивания фотографий космоса и публикации их с помощью бота в Telegram


[space_image](https://klike.net/uploads/posts/2019-06/1560231201_2.jpg)


## Установка

1. Скачайте код
2. Для работы скрипта нужен Python версии не ниже 3.7
3. Установите зависимости, указанные в файле requirements.txt командой:

``pip install -r requirements.txt``

## Переменные окружения

1. Для работы скрипта с сайтом NASA необходимо получить token: [ссылка для получения токена](https://api.nasa.gov/)
2. Для работы Телеграм-бота необходимо создать бота и получить token: [ссылка для получения токена](https://telegram.me/BotFather). [Инструкция по созданию бота и получению tokena](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)
3. В корневой папке проекта необходимо создать файл **.env**, в который необходимо записать полученные токены по примеру:

```
NASA_TOKEN = полученный токен NASA
BOT_TOKEN = полученный токен бота
```

## Состав и запуск

### Весь код состоит из 4 независимых скриптов с API-интеграциями:
1. ```fetch_apod_nasa_images``` -  скачивает фотографии дня с сайта NASA. Запускается командой: ```python3 fetch_apod_nasa_images.py```
2. ```fetch_epic_nasa_images``` - скачивает фотографии  Земли и фиксирует уникальные перспективы некоторых астрономических событий с сайта NASA. Запускается командой: ```python3 fetch_epic_nasa_images.py```
3. ```fetch_spacex_images``` - скачивает фотографии последнего запуска SpaceX в случае если они были сделаны при последнем запуске. В случае отсутствия фотографий последнего запуска, скрипт выбирает из всех имеющих запусков с фотографиями рандомный. Запускается командой ```python3 fetch_spacex_images.py```. Опционально можно указать аргумент (ID конкретного запуска) командой: ```python3 fetch_spacex_images.py ID_запуска``` 
4. ```publish_image_to_telegram``` - публикует скачанные фотографии в чат Telegram c помощью бота. Запускается командой ```python3 publish_image_to_telegram.py```

### Скрипт ```main.py``` объединяет указанные выше скрипты:

При запуске командой ```python3 main.py``` скачиваются фотографии и публикуются в канал Telegram (время между публикациями можно установить в файле ```settigs.py``` переменная ```TIME_SLEEP```)

### ```helper.py``` Не требует отдельного запуска, содержит вспомогательные функции.
### ```settings.py``` Не требует отдельного запуска, содержит глобальные переменные настройки для работы скриптов, среди которых:

CHAT_ID - ID чата, в который публикуются фотографии

BOT_TOKEN - token бота

TIME_SLEEP - время между публикациями фотографий (сек)

IMAGES_FOLDER - наименование папки для скачивания фотографий

NASA_TOKEN - NASA token

ALL_LAUNCHES_URL - URL для получения информации о всех запусках SpaceX

LATEST_LAUNCH_URL - URL для получения информации о последнем запуске SpaceX

FILE_NAME_SPACEX - имя для сохраняемых фотографий запуска SpaceX

APOD_URL - URL для получения информации о фото дня NASA

FILE_NAME_APOD - имя для сохраняемых фото дня NASA

EPIC_URL - URL для получения информации о фото Земли и некоторых астрономических событий NASA

FILE_NAME_EPIC - имя для сохраняемых фото Земли и некоторых астрономических событий NASA