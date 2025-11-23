import streamlit as st

st.set_page_config(page_title="Convite de Natal 🎄", page_icon="🎄")

# --- BACKGROUND COM CORES NATALINAS ---
page_bg = """
<style>
body {
    background: linear-gradient(180deg, #b30000, #ffffff, #006400);
    background-attachment: fixed;
    background-size: cover;
    background-repeat: no-repeat;
}

/* Caixa branca no centro */
.main-container {
    background: rgba(255, 255, 255, 0.90);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 18px rgba(0,0,0,0.25);
    margin-top: 20px;
}

/* Enfeites natalinos */
h1, h2 {
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.natal-icon {
    font-size: 32px;
    margin-right: 10px;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Wrapper manual
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# ---- TÍTULO ----
st.markdown("""
    <div style='text-align:center;'>
        <span class='natal-icon'>🎄✨🎅</span>
        <h1 style='color:#b30000;'>Convite de Natal</h1>
        <h2>Bem vindo a Andleide 🎁</h2>
        <p style='font-size:18px;'>Preencha abaixo sua confirmação para nossa noite especial!</p>
        <span class='natal-icon'>❄️🕯️🌟</span>
    </div>
""", unsafe_allow_html=True)


# ---- FORMULÁRIO ----
with st.form("formulario_natal"):

    st.subheader("🎅 Informações Principais")

    nome_principal = st.text_input("Seu nome:")
    item = st.text_input("O que você vai levar:")

    st.write("### 🎄 Quantas pessoas irão?")

    qtd_adultos = st.number_input("Adultos:", min_value=0, step=1)
    qtd_criancas = st.number_input("Crianças:", min_value=0, step=1)

    st.write("---")

    adultos_nomes = []
    if qtd_adultos > 0:
        with st.expander("👨‍🦳 Nomes dos adultos"):
            for i in range(qtd_adultos):
                nome_adulto = st.text_input(
                    f"Nome do adulto {i+1}:",
                    key=f"adulto_nome_{i}"
                )
                adultos_nomes.append(nome_adulto)

    criancas_nomes = []
    if qtd_criancas > 0:
        with st.expander("👶 Nomes das crianças"):
            for i in range(qtd_criancas):
                nome_crianca = st.text_input(
                    f"Nome da criança {i+1}:",
                    key=f"crianca_nome_{i}"
                )
                criancas_nomes.append(nome_crianca)

    st.write("---")

    # AMIGO DOCE
    amigo_doce = st.radio(
        "🍫 Você vai participar do *Amigo Doce*?",
        ["Não", "Sim"]
    )

    if amigo_doce == "Sim":
        st.info("Para participar, é necessário **dez reais físico e uma barra de chocolate por pessoa!** 🍫")

    enviado = st.form_submit_button("🎁 Enviar confirmação")


# ---- RESPOSTA APÓS ENVIO ----
if enviado:
    st.success("🎄 Sua confirmação foi enviada com sucesso! Obrigada ❤️")

    st.write("## 🌟 Resumo:")

    st.write(f"**Nome:** {nome_principal}")
    st.write(f"**Vai levar:** {item}")

    st.write(f"### 👨‍👩‍👧‍👦 Adultos ({qtd_adultos}):")
    for nome in adultos_nomes:
        st.write(f"- {nome}")

    st.write(f"### 🧸 Crianças ({qtd_criancas}):")
    for nome in criancas_nomes:
        st.write(f"- {nome}")

    st.write(f"### 🍫 Amigo Doce: **{amigo_doce}**")
    if amigo_doce == "Sim":
        st.write("➡ Será necessário R$10 e 1 barra de chocolate por pessoa.")

    st.warning("⚠ É obrigatório participar de no mínimo 1 a 2 brincadeiras.")

# fecha caixa branca
st.markdown("</div>", unsafe_allow_html=True)
