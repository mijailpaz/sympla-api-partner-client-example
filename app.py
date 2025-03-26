import streamlit as st
import requests
import json

# Configuração da página
st.set_page_config(page_title="Eventos da Sympla", layout="wide")

# CSS customizado para os cards
st.markdown(
    """
    <style>
    .card {
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .card img {
        max-width: 100%;
        height: auto;
        border-radius: 4px;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título e introdução
st.title("Sympla-api-partner-client-example")
st.write("Bem-vindo ao aplicativo para explorar eventos da API de Parceiros da Sympla!")

# Introdução à API
st.header("O que é a API de Parceiros da Sympla?")
st.write(
    """
    A API de Parceiros da Sympla é uma interface que permite acessar o discovery da plataforma Sympla. 
    Ela possibilita obter informações detalhadas sobre eventos criados, exclusivamente aqueles vinculados à conta de um parceiro autenticado.
    
    Com suporte a filtros e paginação, a API oferece flexibilidade para personalizar os resultados e trabalhar com intervalos de dados específicos.
    Para mais detalhes, acesse a [documentação oficial](https://developers.sympla.com.br/api-doc/partners/).
    """
)

# Área de setup (sidebar) para inserir o token e os parâmetros da query string
with st.sidebar:
    st.header("Setup")
    token = st.text_input("Token de Acesso", type="password")
    page = st.number_input("Página", min_value=1, value=1, step=1)
    limit = st.number_input("Quantidade de eventos por página", min_value=1, value=16, step=1)
    fetch_data = st.button("Carregar Eventos")

# Se o botão for clicado e o token for informado
if fetch_data and token:
    headers = {
        "Accept": "application/json",
        "s_token": token
    }
    # Monta a URL do endpoint utilizando os parâmetros page e limit
    EVENTS_ENDPOINT = f"https://search.sympla.com.br/partners/events?limit={limit}&page={page}"
    
    try:
        response = requests.get(EVENTS_ENDPOINT, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao conectar com a API: {e}")
    else:
        try:
            result = response.json()
        except json.JSONDecodeError as e:
            st.error("Erro ao decodificar a resposta JSON.")
            st.error(e)
            result = {}

        # Extrai a lista de eventos e os parâmetros de paginação
        # Handle both list and dictionary responses
        if isinstance(result, list):
            events = result
            total = len(result)
            current_page = page
            current_limit = limit
        else:
            events = result.get("data", [])
            total = result.get("total", 0)
            current_page = result.get("page", page)
            current_limit = result.get("limit", limit)
        
        if events:
            st.write(f"Foram encontrados {total} eventos (mostrando {len(events)} na página {current_page}).")
            # Cria colunas para os cards: 3 colunas por linha
            cols = st.columns(3)
            col_idx = 0

            for event in events:
                # Verifica se o item é um dicionário
                if not isinstance(event, dict):
                    st.warning(f"Formato inesperado de evento: {event}")
                    continue

                # Extraindo os dados do evento conforme o JSON retornado
                event_name = event.get("name", "Nome não disponível")
                start_date = event.get("start_date", "Data de início não disponível")
                end_date = event.get("end_date", "Data de fim não disponível")
                event_type = event.get("type", "Tipo não informado")
                discount = event.get("discount", "")
                
                # Dados da imagem, se disponível
                images = event.get("images", {})
                image_url = images.get("original", "")
                
                # Dados da localização
                location = event.get("location", {})
                address = location.get("address", "")
                city = location.get("city", "")
                state = location.get("state", "")
                country = location.get("country", "")
                
                # URL do evento
                url = event.get("url", "#")
                
                # Cria o HTML do card
                card_html = f"""
                <div class="card">
                    <h4>{event_name}</h4>
                    {'<img src="' + image_url + '" alt="Imagem do evento">' if image_url else ""}
                    <p><strong>Início:</strong> {start_date}</p>
                    <p><strong>Fim:</strong> {end_date}</p>
                    <p><strong>Tipo:</strong> {event_type}</p>
                    {"<p><strong>Desconto:</strong> " + discount + "</p>" if discount else ""}
                    <p><strong>Local:</strong> {address} - {city}/{state}, {country}</p>
                    <p><a href="{url}" target="_blank">Link evento</a></p>
                </div>
                """
                # Escreve o card na coluna atual
                cols[col_idx].markdown(card_html, unsafe_allow_html=True)
                col_idx += 1

                # Quando preencher 3 colunas, cria uma nova linha de colunas
                if col_idx == 3:
                    cols = st.columns(3)
                    col_idx = 0
        else:
            st.warning("Nenhum evento encontrado.")
else:
    if not token:
        st.info("Por favor, insira seu token na barra lateral para carregar os eventos.")