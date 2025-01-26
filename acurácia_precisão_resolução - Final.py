import numpy as np
import matplotlib.pyplot as plt

def desenhar_alvo(ax):
    """Desenha um alvo com círculos concêntricos."""
    for raio in range(1, 6):
        ax.add_patch(plt.Circle((0, 0), raio, color='black', fill=False, lw=1))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.plot(0, 0, 'ko', markersize=8)  # Centro do alvo

def plotar_tiros(ax, tiros, titulo, cor_fundo):
    """Plota os tiros e adiciona um título."""
    x, y = tiros.T
    ax.scatter(x, y, color='red', s=50, edgecolors='black')
    ax.set_title(titulo, fontsize=12, fontweight='bold', pad=20)
    ax.set_facecolor(cor_fundo)  # Define a cor de fundo

# Função para gerar tiros simulando Acurácia, Precisão e Resolução
def gerar_tiros(acuracia, precisao, resolucao):
    """Gera dados baseados nas combinações de acurácia, precisão e resolução."""
    loc = [0, 0] if acuracia == "Alta" else [3, 3]
    scale = 0.5 if precisao == "Alta" else 2.0
    n_points = 50 if resolucao == "Alta" else 15
    return np.random.normal(loc=loc, scale=scale, size=(n_points, 2))

COR_PESSEGO = "#B0E0E6"
COR_AZUL_CLARO = "#FFDAB9"

# Definição de cores
COR_AZUL_CLARO = "#B0E0E6"
COR_PESSEGO = "#FFDAB9"

# Configuração das simulações
np.random.seed(42)

def gerar_dados_acuracia():
    return np.random.normal(loc=0, scale=0.5, size=(15, 2)), np.random.normal(loc=[2, 2], scale=0.5, size=(15, 2))

def gerar_dados_precisao():
    return np.random.normal(loc=0, scale=0.5, size=(15, 2)), np.random.normal(loc=0, scale=1.5, size=(15, 2))

def gerar_dados_resolucao():
    return np.random.normal(loc=0, scale=1.0, size=(15, 2)), np.random.normal(loc=0, scale=1.0, size=(5, 2))

# Dados para os gráficos
dados_alta_acuracia, dados_baixa_acuracia = gerar_dados_acuracia()
dados_alta_precisao, dados_baixa_precisao = gerar_dados_precisao()
dados_alta_resolucao, dados_baixa_resolucao = gerar_dados_resolucao()

# Criar figura e eixos
fig, eixos = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Acurácia vs. Viés", fontsize=14, fontweight='bold')

# Gráfico da esquerda (Alta Acurácia, Baixo Viés)
desenhar_alvo(eixos[0])
plotar_tiros(eixos[0], dados_alta_acuracia, "↑ Acurácia", COR_AZUL_CLARO)

# Gráfico da direita (Baixa Acurácia, Alto Viés)
desenhar_alvo(eixos[1])
plotar_tiros(eixos[1], dados_baixa_acuracia, "↓ Acurácia (↑ Viés)", COR_PESSEGO)

# Exibir gráficos
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('Acurácia vs. Viés.png')

# Criar figura e eixos
fig, eixos = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Alta Precisão vs. Baixa Precisão", fontsize=14, fontweight='bold')

# Gráfico da esquerda (Alta Precisão)
desenhar_alvo(eixos[0])
plotar_tiros(eixos[0], dados_alta_precisao, "↑ Precisão", COR_AZUL_CLARO)

# Gráfico da direita (Baixa Precisão)
desenhar_alvo(eixos[1])
plotar_tiros(eixos[1], dados_baixa_precisao, "↓ Precisão", COR_PESSEGO)

# Exibir gráficos
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('Alta Precisão vs. Baixa Precisão.png')

# Criar figura e eixos
fig, eixos = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle("Alta Resolução vs Baixa Resolução", fontsize=14, fontweight='bold')

# Gráfico da esquerda (Alta Resolução)
desenhar_alvo(eixos[0])
plotar_tiros(eixos[0], dados_alta_resolucao, "↑ Resolução", COR_AZUL_CLARO)

# Gráfico da direita (Baixa Resolução)
desenhar_alvo(eixos[1])
plotar_tiros(eixos[1], dados_baixa_resolucao, "↓ Resolução", COR_PESSEGO)

# Exibir gráficos
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('Alta Resolução vs Baixa Resolução.png')

acc = ["Alta Acurácia","Baixa Acurácia"]
pre = ["Alta Precisão", "Baixa Precisão"]
res = ["Alta Resolução", "Baixa Resolução"]

# Criar o mosaico de gráficos
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
combinacoes = [
    ("⬆️", "⬆️", "⬆️"),
    ("⬆️", "⬆️", "⬇️"),
    ("⬆️", "⬇️", "⬆️"),
    ("⬆️", "⬇️", "⬇️"),
    ("⬇️", "⬆️", "⬆️"),
    ("⬇️", "⬆️", "⬇️"),
    ("⬇️", "⬇️", "⬆️"),
    ("⬇️", "⬇️", "⬇️"),
]

# Cor única de fundo da paleta fornecida
fundo_unico = "#DADBEF"

# Plotar cada combinação com fundo unificado
for ax, (acuracia, precisao, resolucao) in zip(axes.flatten(), combinacoes):
    tiros = gerar_tiros(
        acuracia="Alta" if acuracia == "⬆️" else "Baixa",
        precisao="Alta" if precisao == "⬆️" else "Baixa",
        resolucao="Alta" if resolucao == "⬆️" else "Baixa",
    )
    desenhar_alvo(ax)
    plotar_tiros(
        ax, tiros,
        titulo=f"Acurácia: {acuracia}, Precisão: {precisao}, Resolução: {resolucao}",
        cor_fundo=fundo_unico
    )

plt.tight_layout()
plt.savefig('Mosaico Comparativo Acurácia x Precisão x Resolução.png')