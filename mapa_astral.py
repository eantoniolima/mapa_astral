# importando bibliotecas
import streamlit as st
import os
import base64
from kerykeion import (
    AstrologicalSubjectFactory,
    ChartDataFactory,
    ChartDrawer
)

# Função para converter a imagem em base64


def imagem_base64(caminho):
    with open(caminho, "rb") as arquivo:
        return base64.b64encode(arquivo.read()).decode()


imagem = imagem_base64("roda.jpg")

st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: #0E1117;
            color: white;
        }}

        .topo {{
            text-align: center;
            margin-top: 10px;
            margin-bottom: 10px;
        }}

        .topo img {{
            width: 240px;
            height: 240px;
            object-fit: contain;
        }}

        .topo h1 {{
            margin-top: 10px;
            margin-bottom: 0;
            font-size: 40px;
            color: white;
        }}
    </style>

    <div class="topo">
        <img src="data:image/jpeg;base64,{imagem}">
        <h1>Mapa Astral</h1>
    </div>
    """,
    unsafe_allow_html=True
)
# Configurações da página
st.set_page_config(
    page_title="Mapa Astral",
    layout="wide"

)

# Configurando a variável de ambiente para o nome de usuário do GeoNames
os.environ["GEONAMES_USERNAME"] = "eantoniolima"


# Formulário de dados de nascimento
st.subheader("Dados de nascimento")

nome = st.text_input(
    "Nome",
    placeholder="Digite o nome"
)

col1, col2, col3 = st.columns(3)

with col1:
    dia = st.number_input(
        "Dia",
        min_value=1,
        max_value=31,
        value=1
    )

with col2:
    mes = st.number_input(
        "Mês",
        min_value=1,
        max_value=12,
        value=1
    )

with col3:
    ano = st.number_input(
        "Ano",
        min_value=1900,
        max_value=2100,
        value=1980
    )

col4, col5 = st.columns(2)

with col4:
    hora = st.number_input(
        "Hora",
        min_value=0,
        max_value=23,
        value=15
    )

with col5:
    minuto = st.number_input(
        "Minuto",
        min_value=0,
        max_value=59,
        value=30
    )

cidade = st.text_input(
    "Cidade",
    placeholder="Ex.: Rio de Janeiro"
)

pais = st.text_input(
    "País",
    value="BR",
    max_chars=2,
    help="Use o código ISO do país. Ex.: BR para Brasil."
)

# Botão para criar o mapa astral
st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(90deg, #6A1B9A, #1565C0) !important;
    color: black !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

if st.button("Criar mapa astral"):

    if not nome or not cidade or not pais:
        st.warning("Preencha nome, cidade e país.")

    else:

        #  Criando o mapa astral
        try:
            subject = AstrologicalSubjectFactory.from_birth_data(
                name=nome,
                year=int(ano),
                month=int(mes),
                day=int(dia),
                hour=int(hora),
                minute=int(minuto),
                city=cidade,
                nation=pais.upper(),
                online=True
            )

            st.success(f"Mapa astral criado para {nome}!")

            st.write("Cidade:", cidade)
            st.write("País:", pais.upper())
            st.write(
                "Data:",
                f"{dia:02d}/{mes:02d}/{ano}"
            )
            st.write(
                "Horário:",
                f"{hora:02d}:{minuto:02d}"
            )

            st.subheader("Posições astrológicas")

            st.write(
                f"☀️ Sol: {subject.sun.sign} "
                f"a {subject.sun.position:.2f}°"
            )

            st.write(
                f"🌙 Lua: {subject.moon.sign} "
                f"a {subject.moon.position:.2f}°"
            )

            st.write(
                f"⬆️ Ascendente: "
                f"{subject.first_house.sign}"
            )

            st.write(
                f"☀️ Posição absoluta do Sol: "
                f"{subject.sun.abs_pos:.2f}°"
            )

            chart_data = ChartDataFactory.create_natal_chart_data(
                subject
            )

            drawer = ChartDrawer(chart_data)

            svg_string = drawer.generate_svg_string()

            st.subheader("Mapa Natal")

            st.components.v1.html(
                svg_string,
                height=1000,
                scrolling=False
            )

        except Exception as e:
            st.error(
                f"Erro ao criar o mapa astral: {e}"
            )
