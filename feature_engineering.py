def feature_engineering(df):
    olist = df.copy()

    # Creating time-based features
    olist['delivery_delta'] = (olist['order_delivered_customer_date'] - olist['order_estimated_delivery_date']).dt.days
    olist['processing_time'] = (olist['order_delivered_carrier_date'] - olist['order_approved_at']).dt.days
    olist['shipping_time'] = (olist['order_delivered_customer_date'] - olist['order_delivered_carrier_date']).dt.days

    # Volume feature
    olist['product_volume_cm3'] = olist['product_length_cm'] * olist['product_height_cm'] * olist['product_width_cm']

    return olist
