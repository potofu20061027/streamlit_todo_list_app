import streamlit as st
import pandas as pd

@st.cache_resource
def get_todo_data4():
    return[]

# ページタイトル
st.title("TODOリストアプリ")

# 日時とやることを入力
due_date = st.date_input("日時")
task = st.text_input("やること")

# 追加ボタンがクリックされた場合
if st.button("追加"):
    if due_date and task:
        # データを取得
        todo_list4 = get_todo_data4()
        # 新しいタスクを追加
        todo_list4.append({"日時": due_date, "やること": task})
        # データを更新
        st.write("タスクが追加されました！")
        # タスクリストを表示
        df = pd.DataFrame(todo_list4)

# タスクリストを表示
st.header("TODOリスト")
todo_list4 = get_todo_data4()
if not todo_list4:
    st.write("タスクはまだありません。")
else:
    df = pd.DataFrame(todo_list4)
    st.table(df)

if todo_list4:    
    delete_index = st.number_input("削除する項目の番号を選択", min_value=0, max_value=len(todo_list4))
    if st.button("削除"):
        if delete_index >= 0 and delete_index <= len(todo_list4):
            del todo_list4[delete_index]  # 選択された項目を削除
            st.write(f"項目 {delete_index} を削除しました。")
            # タスクリストを表示
            df = pd.DataFrame(todo_list4)
            st.table(df)