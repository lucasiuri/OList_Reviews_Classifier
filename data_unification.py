import pandas as pd
import os

def unify_olist_data():
    print('Unifying data.')
    
    path = 'C:/Users/lucas/OneDrive/Área de Trabalho/Lucas/Projetos/E-commerce_reviews_classification/data'
    os.chdir(path)

    olist = pd.read_csv('olist_orders_dataset.csv')

    tmp_df = pd.read_csv( 'olist_order_reviews_dataset.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'order_id')

    tmp_df = pd.read_csv( 'olist_order_payments_dataset.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'order_id')

    tmp_df = pd.read_csv( 'olist_customers_dataset.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'customer_id')


    tmp_df = pd.read_csv( 'olist_order_items_dataset.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'order_id')

    tmp_df = pd.read_csv( 'olist_products_dataset.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'product_id')

    tmp_df = pd.read_csv( 'olist_sellers_dataset.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'seller_id')

    tmp_df = pd.read_csv( 'product_category_name_translation.csv')
    olist = pd.merge(olist, tmp_df, 'left', 'product_category_name')

    print('Data unified.')

    cwd = 'C:/Users/lucas/OneDrive/Área de Trabalho/Lucas/Projetos/E-commerce_reviews_classification'
    os.chdir(cwd)

    return olist