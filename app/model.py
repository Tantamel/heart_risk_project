from catboost import CatBoostClassifier, Pool

class HeartRiskModel:
    """Загружает обученную модель CatBoost и делает предсказания."""

    def __init__(self, model_path: str):
        self.model = CatBoostClassifier()
        self.model.load_model(model_path)
        # Получаем список имён категориальных признаков из сохранённой модели
        
        try:
            self.cat_feature_names = self.model.get_cat_feature_names()
        except AttributeError:
            
            self.cat_feature_names = [
                'Diabetes','Family History','Smoking','Obesity',
                'Alcohol Consumption','Diet','Previous Heart Problems',
                'Medication Use','Stress Level','Physical Activity Days Per Week',
                'Gender'
            ]

    def predict(self, data: 'pd.DataFrame') -> list:
        """
        Принимает DataFrame с фичами, создаёт Pool c категориальными признаками
        и возвращает список меток 0/1.
        """
        # Создаём специальный Pool, чтобы CatBoost знал, какие признаки категориальные
        pool = Pool(data, cat_features=self.cat_feature_names)
        preds = self.model.predict(pool)
        return preds.astype(int).tolist()
