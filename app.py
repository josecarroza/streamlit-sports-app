import streamlit as st
from common.auth import init_session, login, logout

st.set_page_config(
    page_title="Sports Streamlit App",
    page_icon="🏆",
    layout="wide"
)

init_session()

st.title("Aplicación Deportiva con Streamlit")

if not st.session_state.logged_in:
    st.subheader("Iniciar sesión")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Entrar"):
        if login(username, password):
            st.success("Inicio de sesión correcto")
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")

    st.info("Usa usuario: admin y contraseña: admin")

else:
    st.success(f"Bienvenido, {st.session_state.username}")

    col1, col2 = st.columns([1, 5])

    with col1:
        if st.button("Cerrar sesión"):
            logout()
            st.rerun()

    st.markdown("### Inicio")
    st.write("La sesión está activa. Usa el menú lateral para navegar entre las páginas.")