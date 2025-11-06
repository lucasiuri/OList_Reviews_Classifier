from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np


app = Flask(__name__)

model = joblib.load('customer_satisfaction_model.joblib')

@app.route('/')
def home():
    """Render the home page with input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Receive user input, make a prediction, and return the result."""
    form_data = request.form.to_dict()

    try:
        numerical_values = {k: float(v) for k,v in form_data.items() if k not in ['payment_type', 'customer_state', 'product_category_name_english']}

        all_values = {**numerical_values, **{k: v for k,v in form_data.items() if k not in ['payment_type', 'customer_state', 'product_category_name_english']}}

        input_df = pd.DataFrame([all_values])

        model_features = ['price', 'freight_value', 'payment_installments', 'payment_value',
            'product_name_lenght', 'product_description_lenght', 'product_photos_qty',
            'product_weight_g', 'delivery_delta', 'processing_time', 'shipping_time',
            'product_volume_cm3', 'payment_type', 'customer_state', 'product_category_name_english'
            ]
        
        input_df = input_df[model_features]

        prediction = model.predict(input_df)

        output = int(prediction)

        return render_template('result.html', prediction = output)
    
    except Exception as e:
        error_message = f'An error occurred: {e}'
        return render_template('result.html', error = error_message)
    
if __name__ == '__main__':
     app.run(debug=True)