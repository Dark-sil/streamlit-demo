import streamlit as st

st.title('hello world!')

st.header("header")

st.subheader("sub header")

st.text("like we can implemnt text")

st.markdown(""" # h1 tag
## h2 tag 
### h3
:moon:<br>
:sunglasses:
""")

st.latex(r''' \sum_{k=0}^{n-1} ar^k ''')

st.write(sum)

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])


st.line_chart(chart_data)


with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

video_file = open('[Kayoanime] shiki - S01E01.mkv', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)