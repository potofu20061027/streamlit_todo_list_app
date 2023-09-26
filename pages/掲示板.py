import streamlit as st
import pandas as pd
from datetime import datetime
import pytz

# ページタイトル
st.title("掲示板アプリ")

# メッセージデータの初期化（初回のみ）
@st.cache_data
def initialize_messages():
    return []

if 'messages' not in st.session_state:
    st.session_state.messages = initialize_messages()

# メッセージ入力フィールド
message = st.text_area("新しいメッセージを入力してください:")

# メッセージを投稿
if st.button("投稿"):
    if message:
        now = datetime.now(pytz.timezone('Asia/Tokyo'))
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.messages.append((message, formatted_date))
        st.text("メッセージが投稿されました！")

# メッセージ一覧
st.header("メッセージ一覧")
if not st.session_state.messages:
    st.write("まだメッセージはありません。")
else:
    selected_index = st.selectbox("削除するメッセージを選んでください:", [f"{i+1}. {msg[0]} ({msg[1]})" for i, msg in enumerate(st.session_state.messages)])
    
    if st.button("選択したメッセージを削除"):
        selected_index = int(selected_index.split(".")[0]) - 1
        del st.session_state.messages[selected_index]

    for i, (msg, timestamp) in enumerate(st.session_state.messages):
        st.write(f"{i+1}. {msg} (投稿日時: {timestamp})")


