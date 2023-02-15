import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Stramlit 超入門')

st.write('Interactive Widgets')

# カラムを2つに設定
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')


# エクスパンダーを設定
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：',condition

# if st.checkbox('かわいい生きものがみたいならチェック！'):
    # img = Image.open('cat.jpg')
    # st.image(img, caption='Neko', use_column_width=True)