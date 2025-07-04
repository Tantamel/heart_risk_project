A network error occurred. Please check your connection and try again. If this issue persists please contact us through our help center at help.openai.com.


# Heart Attack Risk Prediction API

## Описание проекта
Это REST‑API на FastAPI для предсказания риска сердечного приступа на основе медицинских и поведенческих данных пациента.  
Модель обучена с помощью CatBoost, а препроцессинг данных упакован в класс `DataPreprocessor`.

## Структура проекта
heart_risk_project/
├── app/
│ ├── init.py
│ ├── data_preprocessing.py # класс DataPreprocessor
│ ├── model.py # класс HeartRiskModel
│ └── main.py # FastAPI-приложение
├── notebooks/
│ └── EDA_heart_project.ipynb # анализ и обучение модели
├── saved_model/
│ └── catboost_heart_model.cbm # сохранённая модель CatBoost
├── test_client.py # скрипт для отправки запроса к API и сохранения submission.csv
├── requirements.txt # список зависимостей
└── README.md # этот файл


## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Tantamel/heart_risk_project.git
   cd heart_risk_project
(Для изоляции зависимостей можно создать виртуальное окружение):

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Установите зависимости:

pip install -r requirements.txt
Запуск API‑сервера
В корне проекта выполните:

uvicorn app.main:app --reload
После старта сервер будет доступен по адресу
http://127.0.0.1:8000

Документация Swagger
Автоматически доступна по адресу
http://127.0.0.1:8000/docs

Использование:
Запустите сервер (см. выше).

Подготовьте CSV-файл test.csv (в корне проекта) с теми же колонками, что были в исходном тестовом датасете, включая столбец id, но без столбца prediction.

Запустите скрипт:

python test_client.py
В результате появится файл submission.csv с двумя колонками:

id

prediction

Пример ответа API
Если отправить запрос через Swagger или test_client.py, в ответ придёт JSON:

json
{
  "predictions": [0, 1, 0, 0, 1, ...]
}
Описание модулей:

app/data_preprocessing.py
Содержит класс DataPreprocessor, который:
Удаляет строки с пропусками в ключевых колонках
Приводит бинарные признаки к типу int
Убирает столбец id

app/model.py
Содержит класс HeartRiskModel, который загружает модель CatBoost из файла saved_model/catboost_heart_model.cbm и делает предсказания.

app/main.py
FastAPI‑приложение с одним POST‑эндпоинтом /predict/, принимающим CSV‑файл и возвращающим предсказания.

test_client.py
Скрипт для отправки файла на эндпоинт и генерации submission.csv.

Контакт и поддержка
Если возникнут вопросы или ошибки, создайте Issue в репозитории.

Автор: Татьяна
Дата: July 4, 2025