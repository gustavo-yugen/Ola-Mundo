# =============================================================================
# BIBLIOTECAS NECESSÁRIAS
# =============================================================================
import requests
from bs4 import BeautifulSoup

# =============================================================================
# CONFIGURAÇÕES - URLs que vamos usar
# =============================================================================
# URL principal do site
url_principal = "https://caraguatatuba1.unifaveni.com"
# URL da página da instituição
url_instituicao = url_principal + "/a-instituicao/"

# =============================================================================
# CÓDIGO PRINCIPAL - SEM FUNÇÕES
# =============================================================================

print("Iniciando Web Scraper UniFAVENI - Menu Principal")
print("="*60)

# =============================================================================
# PASSO 1: CARREGAR A PÁGINA DA INTERNET
# =============================================================================
print("Carregando página:", url_instituicao)

# Faz a requisição para a página
pagina = requests.get(url_instituicao)

# Verifica se deu certo (código 200 = sucesso)
if pagina.status_code == 200:
    print("Página carregada com sucesso!")
    # Converte o HTML em algo que podemos trabalhar
    pghtml = BeautifulSoup(pagina.text, 'html.parser')
else:
    print(f"Erro ao carregar página. Código: {pagina.status_code}")
    exit()

# =============================================================================
# PASSO 2: ENCONTRAR O MENU PRINCIPAL
# =============================================================================
print("\nProcurando menu principal...")

# Procura pelo container do menu principal
menu_container = pghtml.find('div', class_='menu-menu-principal-container')

if not menu_container:
    print("Menu principal não encontrado")
    exit()

print("Menu principal encontrado!")

# =============================================================================
# PASSO 3: IDENTIFICAR OS 3 ITENS PRINCIPAIS E SEUS ELEMENTOS PAI
# =============================================================================
print("\nIdentificando os 3 itens principais e seus elementos pai...")

# Listas para guardar as informações encontradas
todos_links = []
graduacao_links = []
pos_graduacao_links = []
capacitacoes_links = []

# Procura pelos 3 itens principais
graduacao_principal = menu_container.find('a', string=lambda text: text and "Graduação EAD" in text.strip())
pos_graduacao_principal = menu_container.find('a', string=lambda text: text and "Pós-Graduação" in text.strip())
capacitacoes_principal = menu_container.find('a', string=lambda text: text and "Capacitações EAD" in text.strip())

print(f"Encontrado: Graduação EAD - {graduacao_principal is not None}")
print(f"Encontrado: Pós-Graduação - {pos_graduacao_principal is not None}")
print(f"Encontrado: Capacitações EAD - {capacitacoes_principal is not None}")

# =============================================================================
# PASSO 4: EXTRAIR LINKS DE CADA CATEGORIA COM HIERARQUIA
# =============================================================================
print("\nExtraindo links de cada categoria com hierarquia...")

# =============================================================================
# GRADUAÇÃO EAD
# =============================================================================
if graduacao_principal:
    print("\nProcurando links de Graduação EAD...")
    
    # Encontra o elemento pai (li) que contém o item principal
    elemento_pai_graduacao = graduacao_principal.find_parent('li')
    
    if elemento_pai_graduacao:
        # Procura por todos os links dentro deste elemento pai
        links_graduacao = elemento_pai_graduacao.find_all('a', recursive=True)
        
        for link in links_graduacao:
            texto_link = link.get_text().strip()
            endereco_link = link.get('href')
            
            if texto_link and endereco_link:
                # Calcula o nível de hierarquia contando os <li> pais
                nivel = 0
                elemento_atual = link
                
                # Sobe na hierarquia até encontrar o elemento pai principal
                while elemento_atual and elemento_atual != elemento_pai_graduacao:
                    if elemento_atual.name == 'li':
                        nivel += 1
                    elemento_atual = elemento_atual.parent
                
                info_link = {
                    'texto': texto_link,
                    'link': endereco_link,
                    'nivel': nivel
                }
                graduacao_links.append(info_link)
                todos_links.append(info_link)
                print(f"Graduação (nível {nivel}): {texto_link}")
        
        print(f"Total de links de Graduação encontrados: {len(graduacao_links)}")
    else:
        print("Elemento pai de Graduação não encontrado")

# =============================================================================
# PÓS-GRADUAÇÃO
# =============================================================================
if pos_graduacao_principal:
    print("\nProcurando links de Pós-Graduação...")
    
    # Encontra o elemento pai (li) que contém o item principal
    elemento_pai_pos = pos_graduacao_principal.find_parent('li')
    
    if elemento_pai_pos:
        # Procura por todos os links dentro deste elemento pai
        links_pos = elemento_pai_pos.find_all('a', recursive=True)
        
        for link in links_pos:
            texto_link = link.get_text().strip()
            endereco_link = link.get('href')
            
            if texto_link and endereco_link:
                # Calcula o nível de hierarquia contando os <li> pais
                nivel = 0
                elemento_atual = link
                
                # Sobe na hierarquia até encontrar o elemento pai principal
                while elemento_atual and elemento_atual != elemento_pai_pos:
                    if elemento_atual.name == 'li':
                        nivel += 1
                    elemento_atual = elemento_atual.parent
                
                info_link = {
                    'texto': texto_link,
                    'link': endereco_link,
                    'nivel': nivel
                }
                pos_graduacao_links.append(info_link)
                todos_links.append(info_link)
                print(f"Pós-Graduação (nível {nivel}): {texto_link}")
        
        print(f"Total de links de Pós-Graduação encontrados: {len(pos_graduacao_links)}")
    else:
        print("Elemento pai de Pós-Graduação não encontrado")

# =============================================================================
# CAPACITAÇÕES EAD
# =============================================================================
if capacitacoes_principal:
    print("\nProcurando links de Capacitações EAD...")
    
    # Encontra o elemento pai (li) que contém o item principal
    elemento_pai_capacitacoes = capacitacoes_principal.find_parent('li')
    
    if elemento_pai_capacitacoes:
        # Procura por todos os links dentro deste elemento pai
        links_capacitacoes = elemento_pai_capacitacoes.find_all('a', recursive=True)
        
        for link in links_capacitacoes:
            texto_link = link.get_text().strip()
            endereco_link = link.get('href')
            
            if texto_link and endereco_link:
                # Calcula o nível de hierarquia contando os <li> pais
                nivel = 0
                elemento_atual = link
                
                # Sobe na hierarquia até encontrar o elemento pai principal
                while elemento_atual and elemento_atual != elemento_pai_capacitacoes:
                    if elemento_atual.name == 'li':
                        nivel += 1
                    elemento_atual = elemento_atual.parent
                
                info_link = {
                    'texto': texto_link,
                    'link': endereco_link,
                    'nivel': nivel
                }
                capacitacoes_links.append(info_link)
                todos_links.append(info_link)
                print(f"Capacitações (nível {nivel}): {texto_link}")
        
        print(f"Total de links de Capacitações encontrados: {len(capacitacoes_links)}")
    else:
        print("Elemento pai de Capacitações não encontrado")

# =============================================================================
# PASSO 5: MOSTRAR RESULTADOS ORGANIZADOS COM HIERARQUIA
# =============================================================================
print("\n" + "="*60)
print("RESULTADOS ORGANIZADOS POR CATEGORIA COM HIERARQUIA")
print("="*60)

# =============================================================================
# GRADUAÇÃO EAD
# =============================================================================
if graduacao_links:
    print(f"\nGRADUAÇÃO EAD ({len(graduacao_links)} itens)")
    print("-" * 40)
    
    for link in graduacao_links:
        # Cria a tabulação baseada no nível
        tabulacao = "  " * link['nivel']
        print(f"{tabulacao}• {link['texto']}")
        if link['link'] != "#":
            print(f"{tabulacao}  {link['link']}")
        print()
else:
    print("\nGRADUAÇÃO EAD: Nenhum item encontrado")

# =============================================================================
# PÓS-GRADUAÇÃO
# =============================================================================
if pos_graduacao_links:
    print(f"\nPÓS-GRADUAÇÃO ({len(pos_graduacao_links)} itens)")
    print("-" * 40)
    
    for link in pos_graduacao_links:
        # Cria a tabulação baseada no nível
        tabulacao = "  " * link['nivel']
        print(f"{tabulacao}• {link['texto']}")
        if link['link'] != "#":
            print(f"{tabulacao}  {link['link']}")
        print()
else:
    print("\nPÓS-GRADUAÇÃO: Nenhum item encontrado")

# =============================================================================
# CAPACITAÇÕES EAD
# =============================================================================
if capacitacoes_links:
    print(f"\nCAPACITAÇÕES EAD ({len(capacitacoes_links)} itens)")
    print("-" * 40)
    
    for link in capacitacoes_links:
        # Cria a tabulação baseada no nível
        tabulacao = "  " * link['nivel']
        print(f"{tabulacao}• {link['texto']}")
        if link['link'] != "#":
            print(f"{tabulacao}  {link['link']}")
        print()
else:
    print("\nCAPACITAÇÕES EAD: Nenhum item encontrado")

# =============================================================================
# RESUMO FINAL
# =============================================================================
print("="*60)
print("RESUMO FINAL")
print("="*60)
print(f"Graduação EAD: {len(graduacao_links)} itens")
print(f"Pós-Graduação: {len(pos_graduacao_links)} itens")
print(f"Capacitações EAD: {len(capacitacoes_links)} itens")
print(f"Total de links processados: {len(todos_links)}")
print("\nProcesso concluído com sucesso!")