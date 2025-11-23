import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Convite de Natal", page_icon="🎄")

# ----------------------------
#  Conexão com a Google Sheet
# ----------------------------
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file("service_account.json", scopes=SCOPE)
client = gspread.authorize(creds)

# Abra sua planilha pelo ID
SHEET_ID = "13T_5ziIDF_VjO5ngBFvD4RmVyOoUTu9yhelQ-h8rKnI"
sheet = client.open_by_key(SHEET_ID).sheet1

# ----------------------------
#     INTERFACE DO SITE
# ----------------------------

st.markdown("""
<h1 style="text-align:center; color:white;">🎄 Bem vindo à Andleide 🎄</h1>
<p style="text-align:center; color:white; font-size:18px;">
Confirme sua presença e diga o que irá levar!
</p>
""", unsafe_allow_html=True)

with st.form("formulario"):
    nome = st.text_input("Seu nome:")
    levar = st.text_input("O que você vai levar?")
    amigo_doce = st.selectbox("Você vai participar do Amigo Doce?", ["Sim", "Não"])
    enviado = st.form_submit_button("Enviar")

if enviado:
    # Adiciona os dados na planilha
    sheet.append_row([nome, levar, amigo_doce])

    st.success("🎉 Seus dados foram enviados com sucesso!")
    st.balloons()

st.markdown("""
<p style="margin-top:40px; color:white; text-align:center;">
É obrigatório participar de 1 a 2 brincadeiras! 🎁
</p>
""", unsafe_allow_html=True)
