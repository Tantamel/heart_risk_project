import requests
import pandas as pd

def main():
    url = "http://127.0.0.1:8000/predict/"
    input_path = "heart_test.csv"           # файл без меток
    output_path = "submission.csv"    # файл, который формирует предсказания для отправки на проверку

    # Отправляем запрос
    with open(input_path, "rb") as f:
        files = {"file": (input_path, f, "text/csv")}
        response = requests.post(url, files=files)

    if response.status_code != 200:
        print(f"Ошибка {response.status_code}: {response.text}")
        return

    # Получаем предсказания
    preds = response.json()["predictions"]

    # Читаем input, добавляем колонку prediction и сохраняем
    df = pd.read_csv(input_path)
    df_result = pd.DataFrame({
        "id": df["id"],
        "prediction": preds
    })
    df_result.to_csv(output_path, index=False)
    print(f"Сохранено {output_path}")

if __name__ == "__main__":
    main()