# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col 

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
  #  """Replace this example with your own code!
   # **And if you're new to Streamlit,** check
    #out our easy-to-follow guides at
    #[docs.streamlit.io](https://docs.streamlit.io).
    """Choose the fruits you want in your custom smoothie"""
)

#option = st.selectbox(
 #   "What is your favourite Fruit?",
  #  ("Banana", "Strawberries", "Peaches"),
#)
#st.write("You selected:", option)

cnx=st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list = st.multiselect('Choose up to five ingredients',my_dataframe)
if ingredients_list:
    ingredients_string=''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

#    st.write(my_insert_stmt)
    time_to_insert = st.button('Submit')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
