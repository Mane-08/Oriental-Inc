import requests
import streamlit as st
#from streamlit_lottie import st_lottie

st.set_page_config(page_title="my webpage",page_icon=":tada",layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_F9aiyX22UC.json")

#-----Header section------
with st.container():
    st.subheader("Hi,welcome:wave:")
    st.title("ORIENTAL Inc")
    st.write("We are a company that offer services")
#---What we do----
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("what we do")
        st.write("##")
        st.write("""""At Oriental Inc, our value lies in our people – how we grow them, how we inspire them, how we empower them. Building a future means building our employees, and in order to ensure our collective ongoing success, our business practices are founded on respect, responsibility, integrity, and uncompromising principles:\n
        -To provide significant opportunities for growth.\n
    -To recognise individual contributions and reward hard work.\n
    -To encourage active employee participation to achieve results.\n
    -To ensure a safe, controlled working environment at all times.\n
    -To train, mentor and nurture our employees in order to ensure the continued growth, evolution and profitability of our company.""""")
#with right_column:
  #  streamlit_lottie(lottie_coding,height=300,key="coding")
#----contact-----
with st.container():
    st.write("----")
    st.header("GET IN TOUCH WITH US!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ngwenyamanelisi4@gmail.com" method="POST">
        <input type = "hidden"name"_captcha" value="false">
         <input type="text" name="name"placeholder="Your name" required>
         <input type="email" name="name"placeholder="Your email" required>
         <textarea name="message"placeholder="Your message here" required ></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()