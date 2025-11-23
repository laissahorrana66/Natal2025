import streamlit as st

st.set_page_config(page_title="Convite de Natal 🎄", page_icon="🎄")

# ---- TÍTULO ----
st.markdown("""
    <h1 style='text-align:center; color:#b30000;'>Convite de Natal 🎄</h1>
    <h2 style='text-align:center;'>Bem vindo a Andleide</h2>
    <p style='text-align:center; font-size:18px;'>Preencha o formulário abaixo para confirmar sua presença.</p>
""", unsafe_allow_html=True)


# ---- FORMULÁRIO ----
with st.form("formulario_natal"):

    st.subheader("Informações principais")

    nome_principal = st.text_input("Seu nome:")
    item = st.text_input("O que você vai levar:")

    st.write("### Quantas pessoas irão?")

    qtd_adultos = st.number_input("Quantidade de adultos:", min_value=0, step=1)
    qtd_criancas = st.number_input("Quantidade de crianças:", min_value=0, step=1)

    st.write("---")

    # ---- NOMES DOS ADULTOS ----
    adultos_nomes = []
    if qtd_adultos > 0:
        st.write("### Nomes dos adultos")
        for i in range(qtd_adultos):
            nome_adulto = st.text_input(f"Nome do adulto {i+1}:", key=f"adulto_{i}")
            adultos_nomes.append(nome_adulto)

    # ---- NOMES DAS CRIANÇAS ----
    criancas_nomes = []
    if qtd_criancas > 0:
        st.write("### Nomes das crianças")
        for i in range(qtd_criancas):
            nome_crianca = st.text_input(f"Nome da criança {i+1}:", key=f"crianca_{i}")
            criancas_nomes.append(nome_crianca)

    st.write("---")

    # ---- PERGUNTA DO AMIGO DOCE ----
    amigo_doce = st.radio(
        "Você vai participar do *Amigo Doce*? (a barra de chocolate e os R$10 são por pessoa, não por família)",
        ["Não", "Sim"]
    )

    if amigo_doce == "Sim":
        st.info("Para a participação é necessário **dez reais físico e uma barra de chocolate (por pessoa, não por família).**")

    enviado = st.form_submit_button("Enviar confirmação 🎄")


# ---- RESPOSTA APÓS ENVIO ----
if enviado:
    st.success("✔ Confirmação enviada com sucesso!")

    st.write("## 🎁 Resumo da sua confirmação")
    st.write(f"**Nome:** {nome_principal}")
    st.write(f"**Levará:** {item}")

    st.write(f"**Adultos ({qtd_adultos}):**")
    for nome in adultos_nomes:
        st.write(f"- {nome}")

    st.write(f"**Crianças ({qtd_criancas}):**")
    for nome in criancas_nomes:
        st.write(f"- {nome}")

    st.write(f"**Participará do Amigo Doce:** {amigo_doce}")

    if amigo_doce == "Sim":
        st.write("🍫 *Você está participando do Amigo Doce!*")
        st.write("➡ Será necessário **R$10 físico e uma barra de chocolate por pessoa**.")

    st.warning("⚠ É obrigatório participar de no mínimo 1 a 2 brincadeiras.")
