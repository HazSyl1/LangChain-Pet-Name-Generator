import langchain_helper as lch
import streamlit as st 



st.title("Pet Name Generator")


with st.sidebar.form('inputs'):
    animal_type=st.text_input("Enter Pet:")
    
    animal_color=st.text_input(f"Enter color of your { animal_type if animal_type else 'Pet'}:")

    submit_button=st.form_submit_button('Get Names!')

if submit_button and animal_color :
    try:
        wait=st.text("Fetching Results...")
        response=lch.generate_pet_name(animal_type , animal_color)
        wait.empty()
        # st.subheader(f"Few names for your {animal_type} could be:")
        st.markdown(f"<span style='font-size: 20px;'>Few names for your {animal_type} could be</span>", unsafe_allow_html=True)

        
        st.text(response["pet_name"])
    except:
        st.warning("Something went wrong . Try Again.")


# # if animal_type:
# #     st.text(animal_type)
# # if st.sidebar.button("Next"):
# #     animal_color=st.sidebar.text_input(f"What Color is your {animal_type}:")

# if st.sidebar.button("Proceed"):
#     try:
#         print(animal_type,animal_color)
#         response=lch.generate_pet_name(animal_type , animal_color)
#         st.text(response)
#     except:
#         st.warning("Enter The Information")

