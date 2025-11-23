import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# --- CONFIG GOOGLE SHEETS ---
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "13T_5ziIDF_VjO5ngBFvD4RmVyOoUTu9yhelQ-h8rKnI"

creds = Credentials.from_service_account_file("service_account.json", scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1


# ---- FUNÇÃO PARA ENVIAR DADOS ----
def enviar_para_planilha(
    nome_principal, item, qtd_adultos, adultos, qtd_criancas, criancas, amigo_doce
):
    linha = [
        nome_principal,
        item,
        qtd_adultos,
        ", ".join(adultos) if adultos else "",
        qtd_criancas,
        ", ".join(criancas) if criancas else "",
        amigo_doce
    ]
    sheet.append_row(linha)


# ---------------- SEU CÓDIGO DO SITE AQUI ------------------

st.set_page_config(page_title="Convite de Natal 🎄", page_icon="🎄")

# --- FORMULÁRIO ---
with st.form("formulario_natal"):
    st.subheader("🎅 Informações Principais")

    nome_principal = st.text_input("Seu nome:")
    item = st.text_input("O que você vai levar:")

    st.write("### 🎄 Quantas pessoas irão?")
    qtd_adultos = st.number_input("Adultos:", min_value=0, step=1)
    qtd_criancas = st.number_input("Crianças:", min_value=0, step=1)

    adultos_nomes = []
    if qtd_adultos > 0:
        for i in range(qtd_adultos):
            adultos_nomes.append(st.text_input(f"Nome do adulto {i+1}:", key=f"adulto_{i}"))

    criancas_nomes = []
    if qtd_criancas > 0:
        for i in range(qtd_criancas):
            criancas_nomes.append(st.text_input(f"Nome da criança {i+1}:", key=f"crianca_{i}"))

    amigo_doce = st.radio("🍫 Você vai participar do Amigo Doce?", ["Não", "Sim"])

    enviado = st.form_submit_button("🎁 Enviar confirmação")

# ---- QUANDO O USUÁRIO ENVIAR ----
if enviado:
    st.success("🎄 Confirmação enviada!")

    enviar_para_planilha(
        nome_principal,
        item,
        qtd_adultos,
        adultos_nomes,
        qtd_criancas,
        criancas_nomes,
        amigo_doce
    )

    st.info("Os dados foram enviados automaticamente para a planilha ✔")
