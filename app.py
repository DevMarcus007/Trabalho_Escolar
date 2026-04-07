import streamlit as st
import os

st.set_page_config(page_title="Trabalho de Ciências - Rochas", layout="wide")

st.title("🪨 Trabalho de Ciências - Tipos de Rochas")
st.caption('Por Manuela Monteiro')

# Textos em Markdown
textos = {
    "Granito epidotizado": """
### 🪨 Granito epidotizado
Trata-se de uma rocha ígnea plutônica onde os minerais originais (feldspato ou biotita) sofreram uma alteração química, muitas vezes causada pela circulação de fluidos quentes no subsolo (processo hidrotermal), resultando na coloração esverdeada.
""",

    "Rocha gnaisse": """
### 🪨 Rocha gnaisse
É uma rocha ígnea plutônica. Possui textura fanerítica, o que significa que os cristais de diferentes minerais são grandes o suficiente para serem vistos a olho nu. Isso indica que ela se formou a partir do resfriamento lento do magma sob a superfície terrestre.
""",

    "Quartzo leitoso": """
### 🪨 Quartzo leitoso
O quartzo é um dos minerais mais comuns da Terra, mas quando ocorre em massas grandes e opacas como esta, é frequentemente chamado de quartzo leitoso ou maciço.
""",

    "Quartzo": """
### 🪨 Quartzo
A rocha possui uma aparência granular e rugosa. A cor avermelhada/acastanhada na superfície não é a cor original da rocha inteira, mas sim resultado do intemperismo químico (exposição à água e oxigênio), que cria uma camada de "ferrugem" natural (limonita ou hematita).
""",

    "Granito rosa": """
### 🪨 Granito rosa
O granito é uma rocha ígnea plutônica (formada no interior da Terra). A cor característica deste tipo se deve à presença de feldspato potássico (ortoclásio). Apresenta textura granular fina a média, com cristais bem unidos.
""",

    "Arenito silicificado": """
### 🪨 Arenito silicificado
O arenito é uma rocha sedimentar formada pela compactação e cimentação de grãos de areia (geralmente quartzo). É uma das rochas mais comuns na crosta terrestre.
"""
}

# Caminhos das imagens locais
imagens = {
    "Granito epidotizado": "images/granito_epidotizado.jpg",
    "Rocha gnaisse": "images/gnaisse.jpg",
    "Quartzo leitoso": "images/quartzo_leitoso.jpg",
    "Quartzo": "images/quartzo.jpg",
    "Granito rosa": "images/granito_rosa.jpg",
    "Arenito silicificado": "images/arenito.jpg"
}

cols = st.columns(2)

for i, rocha in enumerate(textos.keys()):
    with cols[i % 2]:
        caminho = imagens[rocha]

        # Imagem
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.error(f"Imagem não encontrada: {caminho}")

        # Texto
        st.markdown(textos[rocha])

st.divider()

st.markdown("---")
st.caption("Página criada para apresentação de trabalho escolar de ciências de Manuela Monteiro - 6º ano.")