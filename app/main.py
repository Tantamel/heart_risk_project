from fastapi import FastAPI, UploadFile, File
import pandas as pd

from app.model import HeartRiskModel
from app.data_preprocessing import DataPreprocessor

# Инициализация FastAPI приложения
app = FastAPI()

# Загрузка модели и препроцессора один раз при запуске сервера
model = HeartRiskModel("saved_model/catboost_heart_model.cbm")
preprocessor = DataPreprocessor()

# Маршрут для получения предсказаний
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Чтение CSV-файла из запроса
    df = pd.read_csv(file.file)

    # Обработка данных
    df_transformed = preprocessor.transform(df)

    # Получаем предсказания
    predictions = model.predict(df_transformed)

    # Возвращаем результат в JSON формате
    return {"predictions": predictions}