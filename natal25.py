import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Convite de Natal 🎄", page_icon="🎄", layout="centered")

# -------------------- ARQUIVO CSV --------------------
CSV_PATH = "convidados.csv"

if not os.path.exists(CSV_PATH):
    pd.DataFrame(columns=["nome", "item", "amigo_doce"]).to_csv(CSV_PATH, index=False)

def salvar_resposta(nome, item, amigo_doce):
    df = pd.read_csv(CSV_PATH)
    df.loc[len(df)] = [nome, item, amigo_doce]
    df.to_csv(CSV_PATH, index=False)


# -------------------- ESTILO CSS --------------------
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #b30000, #ffffff, #006400) !important;
}
.convite-box {
    background: rgba(255, 248, 240, 0.95);
    padding: 25px;
    border-radius: 20px;
    border: 4px solid green;
    box-shadow: 0 0 25px rgba(0,0,0,0.4);
}
.title {
    color: darkred;
    font-size: 2.6em;
    text-shadow: 2px 2px 6px #fff;
    text-align: center;
}
.boasvindas {
    color: green;
    font-size: 1.6em;
    text-shadow: 1px 1px 3px #fff;
    text-align: center;
}
.aviso {
    color: darkred;
    font-weight: bold;
    text-align: center;
    font-size: 1.1em;
}
</style>
""", unsafe_allow_html=True)


# -------------------- CAIXA DO CONVITE --------------------
st.markdown("<div class='convite-box'>", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🎄 Convite Especial de Natal 🎅</h1>", unsafe_allow_html=True)
st.markdown("<p class='boasvindas'>✨ Bem vindo a Andleide ✨</p>", unsafe_allow_html=True)
st.markdown("<p class='aviso'>⚠️ É obrigatório participar de no mínimo 1 a 2 brincadeiras!</p>", unsafe_allow_html=True)

st.write("Você está convidado para nossa festa de Natal! ✨")
st.write("Preencha o formulário para confirmar sua presença:")

# -------------------- FORMULÁRIO --------------------
with st.form("formulario"):
    nome = st.text_input("Seu nome")
    item = st.text_input("O que você vai levar?")
    amigo_doce = st.selectbox("Vai participar do Amigo Doce?", ["Selecione", "Sim", "Não"])

    enviado = st.form_submit_button("Confirmar")

    if enviado:
        if nome == "" or item == "" or amigo_doce == "Selecione":
            st.error("Por favor, preencha todos os campos!")
        else:
            salvar_resposta(nome, item, amigo_doce)
            st.success("Presença confirmada com sucesso! 🎄✨")

st.markdown("</div>", unsafe_allow_html=True)


# -------------------- LISTA DE CONVIDADOS --------------------
st.markdown("## 🎁 Lista de Convidados")

df = pd.read_csv(CSV_PATH)

if len(df) == 0:
    st.info("Nenhum convidado confirmou presença ainda.")
else:
    for i, row in df.iterrows():
        if row["amigo_doce"] == "Sim":
            st.write(f"**{row['nome']}** vai levar: **{row['item']}** + (Doce obrigatório + R$10 para o Amigo Doce)")
        else:
            st.write(f"**{row['nome']}** vai levar: **{row['item']}**")
