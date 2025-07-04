class DataPreprocessor: 
    def transform(self, df):
        df = df.copy()

        binary_cols = ['Diabetes', 'Family History', 'Smoking', 'Obesity',
                       'Alcohol Consumption', 'Previous Heart Problems', 'Medication Use']

        for col in binary_cols:
            df[col] = df[col].fillna(0).astype(int)  

        df['Stress Level'] = df['Stress Level'].fillna(0).astype(int)
        df['Physical Activity Days Per Week'] = df['Physical Activity Days Per Week'].fillna(0).astype(int)

        if 'id' in df.columns:
            df = df.drop(columns=['id'])

        return df