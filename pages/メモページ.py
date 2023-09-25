import streamlit as st
import pandas as pd

@st.cache_resource
def get_todo_data5():
    return[]

# ページタイトル
st.title("メモ")

#メモを入力
task = st.text_input("メモ")

# 追加ボタンがクリックされた場合
if st.button("追加"):
    if task:
        # データを取得
        todo_list5 = get_todo_data5()
        # 新しいタスクを追加
        todo_list5.append({"メモ欄":task})
        # データを更新
        st.write("タスクが追加されました！")
        # タスクリストを表示
        df = pd.DataFrame(todo_list5)

# タスクリストを表示
st.header("メモ")
todo_list5 = get_todo_data5()
if not todo_list5:
    st.write("メモはまだありません。")
else:
    df = pd.DataFrame(todo_list5)
    st.table(df)

if todo_list5:    
    delete_index = st.number_input("削除する項目の番号を選択", min_value=0, max_value=len(todo_list5))
    if st.button("削除"):
        if delete_index >= 0 and delete_index <= len(todo_list5):
            del todo_list5[delete_index]  # 選択された項目を削除
            st.write(f"項目 {delete_index} を削除しました。")
            # タスクリストを表示
            df = pd.DataFrame(todo_list5)
            st.table(df)