# Вышел за кофе

Визуальная новелла для Рекламатона Мини. Шесть решений на прохождение, два финала и примерно 5–8 минут чтения. Иллюстрации и все сцены уже встроены в `novella.html`.

## Публикация через Streamlit Community Cloud

1. Распакуйте архив и загрузите его содержимое в корень репозитория GitHub. Убедитесь, что `streamlit_app.py`, `requirements.txt` и `novella.html` лежат рядом. Папка `.streamlit` задаёт цветовую тему.
2. Откройте [Streamlit Community Cloud](https://share.streamlit.io/), выберите **Create app** и укажите свой репозиторий и ветку.
3. В **Main file path** укажите `streamlit_app.py`. В **Advanced settings** можно выбрать Python 3.11 — на нём проверен этот пакет. Нажмите **Deploy**.

После запуска вы получите ссылку на игру. API-ключи и секреты не требуются. Для интерфейса Streamlit нужен браузер с включённым JavaScript.

## Локальный запуск

```bash
python -m pip install -r requirements.txt
python -m streamlit run streamlit_app.py
```

Для автономной игры можно открыть `novella.html` отдельно в браузере.
