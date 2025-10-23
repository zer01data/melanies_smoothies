# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw: ")
st.write(
  """Choose the fruits you wan t in your custom Smoothie!.
  """
)

session = get_active_session()
name_on_order = st.text_input("Name on Smoothie:" )

#option = st.selectbox(
#    "What is your Favorite Fruit?",
#    ("Banana", "Strawberries", "Peaches"),
#)
#st.write("Your Favorite Fruit is:", option)
if name_on_order:
    
    st.write("Name on the Smoothie will be: ", name_on_order)
    my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
    #st.dataframe(data=my_dataframe, use_container_width=True)
    
    
    ingredients_list = st.multiselect ('Choose up to 5 ingredients:' ,my_dataframe ,max_selections=5)
    
    if ingredients_list:
        #st.write(ingredients_list)
        #st.text(ingredients_list)
        ingredients_string =''
        
        for fruit_choosen in ingredients_list:
            ingredients_string += fruit_choosen + ' '
        
        st.write(ingredients_string)
            
        my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
                    values ('""" + ingredients_string + """', '""" + name_on_order + """')"""
        
        #st.write(my_insert_stmt)
        #if ingredients_string:
        #    session.sql(my_insert_stmt).collect()
        #    st.success('Your Smoothie is ordered!', icon="✅")
        
        time_to_insert = st.button('Submit Order')
    
        if time_to_insert:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")
         
        














