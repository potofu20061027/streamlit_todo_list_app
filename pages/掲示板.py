import streamlit as st
import pandas as pd
import datetime
import pytz

# ページタイトル
st.title("掲示板アプリ")


import streamlit as st
import pandas as pd

@st.cache_resource
def get_todo_data6():
    return[]
@st.cache_data
def get_time():
    return[]

#メモを入力
task = st.text_input("投稿")
now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
# 追加ボタンがクリックされた場合
if st.button("投稿する"):
    if task:
        # データを取得
        todo_list6 = get_todo_data6()
        time = get_time()
        # 新しいタスクを追加
        todo_list6.append({"投稿一覧":task, "投稿時間":now})
        # データを更新
        st.write("投稿しました！")
        # タスクリストを表示
        df = pd.DataFrame(todo_list6)
# タスクリストを表示
todo_list6 = get_todo_data6()
if not todo_list6:
    st.write("投稿はまだありません。")
else:
    df = pd.DataFrame(todo_list6)
    st.table(df)

if todo_list6:    
    delete_index = st.number_input("削除する投稿の番号を選択", min_value=0, max_value=len(todo_list6))
    if st.button("削除"):
        if delete_index >= 0 and delete_index <= len(todo_list6):
            del todo_list6[delete_index]  # 選択された項目を削除
            st.write(f"選択した投稿を削除しました。")
            # タスクリストを表示
            df = pd.DataFrame(todo_list6)
            st.table(df)