import requests
from bs4 import BeautifulSoup
import streamlit as st


# URLを入力として受け取る関数
def get_webpage_title(url):
    try:
        # URLからウェブページのHTMLを取得
        response = requests.get(url)
        response.raise_for_status()  # エラーチェック

        # BeautifulSoupを使用してHTMLを解析
        soup = BeautifulSoup(response.text, 'html.parser')

        # タイトルタグからタイトルを取得
        title = soup.title.string

        return title

    except requests.exceptions.RequestException as e:
        return f"エラー: {e}"

# ユーザーからURLを入力してもらう
url = st.text_input("URLを入力してください。")


# タイトルを取得して表示
title = get_webpage_title(url)
st.write(title)


