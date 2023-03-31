import streamlit as st

def login_page():
    pass

def register():
    pass

def log_out():
    pass



def load_view():
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Login", "Register", "Logout")
    )
    
    if add_selectbox == 'login':
        login_page()
    elif add_selectbox == 'Register':
        register()
    elif add_selectbox == 'Log out':
        log_out()



if __name__ == '__main__':
    load_view()