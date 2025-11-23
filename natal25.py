import streamlit as st

st.set_page_config(page_title="Convite de Natal 🎄", page_icon="🎅", layout="centered")

# =========================================================
# =============  EFEITOS E DECORAÇÕES NATALINAS  ==========
# =========================================================

decoracoes_css = """
<style>

body {
    background: linear-gradient(180deg, #b30000, #ffffff, #006400);
    background-attachment: fixed;
}

/* --- Luzinhas piscando nas bordas --- */
.luzes {
    position: fixed;
    top: 0;
    width: 100%;
    height: 50px;
    background-image: url('https://i.imgur.com/MT4yq2Y.png');
    background-size: contain;
    animation: piscar 1.2s infinite;
    z-index: 9999;
}

@keyframes piscar {
    0% { filter: brightness(0.6); }
    50% { filter: brightness(1.3); }
    100% { filter: brightness(0.6); }
}

/* --- Neve caindo --- */
.snowflake {
    position: fixed;
    top: -10px;
    color: white;
    font-size: 24px;
    animation-name: snow;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

@keyframes snow {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(100vh); opacity: 0; }
}

/* --- Enfeites animados nas laterais --- */
.enfeite-esq, .enfeite-dir {
    position: fixed;
    top: 20%;
    width: 120px;
    animation: balancar 2.5s infinite ease-in-out;
}
.enfeite-esq { left: 0; }
.enfeite-dir { right: 0; }

@keyframes balancar {
    0% { transform: rotate(-8deg); }
    50% { transform: rotate(8deg); }
    100% { transform: rotate(-8deg); }
}

/* --- Caixa branca central --- */
.main-container {
    background: rgba(255, 255, 255, 0.92);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 18px rgba(0,0,0,0.25);
    margin-top: 90px;
}

/* --- Rodapé com Papai Noel --- */
.rodape {
    text-align: center;
    margin-top: 40px;
    padding: 10px;
    color: white;
    font-size: 18px;
}
</style>
"""

# Inserindo efeitos visuais
st.markdown(decoracoes_css, unsafe_allow_html=True)

# Luzes pisando
st.markdown('<div class="luzes"></div>', unsafe_allow_html=True)

# Enfeites animados laterais
st.markdown('<img class="enfeite-esq" src="https://i.imgur.com/Lc9pS3Q.png">', unsafe_allow_html=True)
st.markdown('<img class="enfeite-dir" src="https://i.imgur.com/Lc9pS3Q.png">', unsafe_allow_html=True)

# Neve caindo (50 flocos)
for i in range(50):
    st.markdown(
        f"<div class='snowflake' style='left:{i*2}%; animation-duration:{3+i%5}s; animation-delay:{i%4}s;'>❄️</div>",
        unsafe_allow_html=True
    )


# =========================================================
# ==================  CONTEÚDO DO SITE  ====================
# =========================================================

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align:center;'>
        <h1 style='color:#b30000; text-shadow:2px 2px 4px #000;'>🎄 Convite de Natal 🎅</h1>
        <h2>✨ Bem vindo a Andleide ✨</h2>
        <p style='font-size:18px;'>Confirme sua presença para nossa festa especial!</p>
    </div>
""", unsafe_allow_html=True)


# ---------------- FORMULÁRIO -----------------
with st.form("form_natal"):

    st.subheader("🎁 Informações principais")

    nome = st.text_input("Seu nome:")
    item = st.text_input("O que você vai levar:")

    st.subheader("🎄 Quem vai com você?")
    qtd_adultos = st.number_input("Adultos:", min_value=0, step=1)
    qtd_criancas = st.number_input("Crianças:", min_value=0, step=1)

    adultos_nomes = []
    criancas_nomes = []

    if qtd_adultos > 0:
        st.write("👨‍🦳 Nomes dos adultos:")
        for i in range(qtd_adultos):
            adultos_nomes.append(st.text_input(f"Adulto {i+1}:", key=f"a{i}"))

    if qtd_criancas > 0:
        st.write("🧸 Nomes das crianças:")
        for i in range(qtd_criancas):
            criancas_nomes.append(st.text_input(f"Criança {i+1}:", key=f"c{i}"))

    st.subheader("🍫 Amigo Doce")
    amigo = st.radio(
        "Vai participar? (A barra de chocolate + R$10 são por **pessoa**, não por família!)",
        ["Não", "Sim"]
    )

    if amigo == "Sim":
        st.info("🍫 Cada pessoa precisa levar: **1 barra de chocolate + R$10**.")

    enviar = st.form_submit_button("🎁 Enviar confirmação")

# ----------- RESPOSTA -----------

if enviar:
    st.success("✨ Confirmação enviada com sucesso!")

    st.write("## 🎄 Resumo da sua participação")
    st.write(f"**Nome:** {nome}")
    st.write(f"**Vai levar:** {item}")

    st.write(f"### 👨‍👩‍👧‍👦 Adultos ({qtd_adultos}):")
    for n in adultos_nomes:
        st.write(f"- {n}")

    st.write(f"### 🧸 Crianças ({qtd_criancas}):")
        for n in criancas_nomes:
            st.write(f"- {n}")

    st.write(f"### 🍫 Amigo Doce: **{amigo}**")

    st.warning("⚠ É obrigatório participar de 1 a 2 brincadeiras!")


# ----------- RODAPÉ COM PAPAI NOEL -----------
st.markdown("""
<div class='rodape'>
    <img src='https://i.imgur.com/0Z3iV4H.png' width='120'><br>
    🎅 <b>Ho Ho Ho! Te esperamos na nossa Noite Mágica de Natal!</b> 🎄
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
