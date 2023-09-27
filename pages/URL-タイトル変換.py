import streamlit as st
import requests
from bs4 import BeautifulSoup

# Streamlitアプリケーションのタイトルを設定
st.title("ウェブページタイトル取得アプリ")

# URLを入力するウィジェット
url = st.text_input("ウェブページのURLを入力してください:")

# タイトルを表示するコールバック
if url:
    try:
        # URLからウェブページのHTMLを取得
        response = requests.get(url)
        response.raise_for_status()  # エラーチェック

        # BeautifulSoupを使用してHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # タイトルタグからタイトルを取得
        title = soup.title.string

        # タイトルを表示
        st.subheader("ウェブページのタイトル:")
        st.write(title)

    except requests.exceptions.RequestException as e:
        # エラーが発生した場合のメッセージ
        st.error(f"エラー: {e}")

# Streamlitアプリケーションを実行
if __name__ == "__main__":
    st.run()


