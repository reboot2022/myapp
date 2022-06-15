import logging.handlers
import os
import queue
from pathlib import Path
from uuid import uuid4

import streamlit as st


HERE = Path(__file__).parent

if 'show_video' not in st.session_state:
    st.session_state["show_video"] = False
if 'page' not in st.session_state:
    st.session_state["page"] = 'page1'


def play_video(address):
    st.video(address)

def login_values(login_id,password_):
    if (login_id == 'Ishant') and (password_=='123456'):
        print('running')
        st.session_state["page"] = 'page2'


def login_page():
    st.header("Login")
    login = st.text_input(label='LoginID',
                          value='',
                          key='loginid',
                          )
    password = st.text_input(label='Password',
                             value='',
                             key='password',
                             )
    st.button('Login',on_click=login_values,args=(login, password))
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        p_video = st.button('Get Help', key='video_play')

    with col3:
        close = st.button('close', key='close_play',kwargs={'allign':'left'})

    if p_video and not close:
        play_video('https://storage.googleapis.com/team-greyfriars.appspot.com/recording3.mov')

def memorable_info():
    st.header("Memorable Info")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.text_input(label='key1')
    with col2:
        st.text_input(label='key2')
    with col3:
        st.text_input(label='key3')

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        p_video = st.button('Get Help', key='video_play')

    with col3:
        close = st.button('close', key='close_play')

    if p_video and not close:
        play_video('https://storage.googleapis.com/team-greyfriars.appspot.com/recording4.mov')


def main():
    if st.session_state["page"] == 'page1':
        login_page()
    elif st.session_state["page"] == 'page2':
        memorable_info()





if __name__ == "__main__":
    main()