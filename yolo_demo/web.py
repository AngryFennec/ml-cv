import streamlit as st
from PIL import Image
import numpy as np
import demo


def main():
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        result = demo.start(image_file=img_array, need_to_show=False)
        st.image(result, caption="")


if __name__ == "__main__":
    main()
