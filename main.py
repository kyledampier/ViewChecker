from cProfile import label
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import title_gen
import image_classification

st.set_option('deprecation.showfileUploaderEncoding', False)

st.write("# ViewChecker")
st.write("## Generate Title Sentiment")

st.text_input("Enter Title", key="title")

cats = {}

if len(st.session_state.title) > 7:
    categories = title_gen.generate_categories(st.session_state.title)
    cats = pd.DataFrame.from_dict(categories)
    cats.drop('sequence', axis=1, inplace=True)
    st.dataframe(cats.head(5))
    st.bar_chart(cats['scores'])

# file_buffer = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# if file_buffer is not None:
#     with Image.open(file_buffer, 'rgb') as image:
#         st.image(image, use_column_width=True)
#         im = image.resize((224, 224)).convert('RGB')
#         print(im.size)
#         img_arr = np.array(im)
#         classes = image_classification.classify(img_arr)
#         st.write(classes)

# if st.session_state.thumbnail is not None:
#     thumbnail = st.session_state.thumbnail
#     # To read file as bytes:
#     bytes_data = thumbnail.getvalue()
#     st.image(bytes_data)
#     classes = image_classification.classify(bytes_data)
#     st.write(classes)
