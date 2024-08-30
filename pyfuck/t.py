import streamlit as st
import time as wt
import pyfiglet
import termcolor
import random
import base64


code = st.text_input("Paste your code here :")

wt.sleep(5)

if code:
  with open("input.py", "w") as f:
    f.write(code)

  from t import main
  main()
  st.success("yay")