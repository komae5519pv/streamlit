import streamlit as st
import time

st.title('Stramlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

# プログレスバーを設定
latest_iteration = st.empty()
bar = st.progress(0)

# プログレスバー表示：0から100までカウントアップ(0.1秒間隔)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1) 

'Done!!!!!'

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
