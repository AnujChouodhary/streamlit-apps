#Student Registration Form
import streamlit as st

st.set_page_config("Student Registration Form", page_icon="📝")
st.title("Registration Form")
c1,c2,c3,c4=st.columns(4)
col1,col2,col3=st.columns([1,1,1])
with st.form("enter you details"):
    Name=c1.text_input("Student Name")
    age=c2.number_input("age in years", min_value=18, max_value=100)
    contact=c3.text_input("contact")
    img=c4.file_uploader("Student Photo", type=["png","jpeg"])

    submit=st.form_submit_button("Submit")

if submit :
    st.success("your details has been registered")
    st.write("### Details")
    st.write("Name:",Name)
    st.write("age:",age)
    st.write("contact no.:",contact)
    st.image(img,width=100 )
    