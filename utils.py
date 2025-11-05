import pandas as pd

def convert_datetime(olist):
    df = olist.copy()
    for col in ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']:
        df[col] = pd.to_datetime(olist[col])
    return df

def load_olist_main_processed():
    try:
        df = pd.read_csv('data/olist_main_dataset.csv', index_col=0)
        df = convert_datetime(df)

        return df
    except Exception as e:
        print(f"Could not load Olist dataset. {e}")
