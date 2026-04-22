# 🍽️ Plataforma de Dieta — Vovô Fabio

Aplicativo desktop para gerenciamento da dieta prescrita para Fabio Silveira, 79 anos, paciente com DRC, pré-diabetes e histórico cardíaco.

---

## Pré-requisitos

- Python 3.10 ou superior
- Windows 10 / 11

---

## Instalação

```bash
# 1. Clone ou baixe o projeto
# 2. Abra um terminal na pasta do projeto
# 3. Crie um ambiente virtual (recomendado)
python -m venv .venv
.venv\Scripts\activate

# 4. Instale as dependências
pip install -r requirements.txt
```

---

## Execução

```bash
python main.py
```

---

## Funcionalidades

| Tela | Descrição |
|------|-----------|
| 🍽️ Pratos Sugeridos | Visualize as refeições do dia e receitas de fim de semana |
| 📋 Ingredientes | Consulte ingredientes de cada prato |
| 👨‍🍳 Forma de Preparo | Passo a passo de cada receita |
| 🛒 Lista de Supermercado | Monte a lista da semana com checkboxes |
| 📄 Dieta Completa | Plano alimentar completo prescrito |
| ⚠️ Recomendações | Hidratação, proteínas, orientações, suplementação, sal de ervas |

### Acessibilidade
- Botões **A+** e **A−** ajustam o tamanho da fonte globalmente
- Botão **🌙/☀️** alterna entre modo escuro e claro
- Timer de hidratação com popup a cada 60 minutos

---

## Gerar executável (.exe)

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name VovoFabioDieta main.py
```

O executável ficará em `dist/VovoFabioDieta.exe`.

---

## Estrutura do projeto

```
PlataformaDietaVovoFabio/
├── main.py                          # Ponto de entrada
├── requirements.txt
├── preferences.json                 # Gerado automaticamente (preferências)
│
├── data/
│   ├── plano_alimentar.json
│   ├── receitas_fds.json
│   ├── orientacoes.json
│   ├── suplementacao.json
│   └── tempero_sal_ervas.json
│
├── views/
│   ├── __init__.py                  # BaseTela
│   ├── tela_principal.py
│   ├── tela_pratos.py
│   ├── tela_ingredientes.py
│   ├── tela_preparo.py
│   ├── tela_lista_supermercado.py
│   ├── tela_dieta_completa.py
│   └── tela_recomendacoes.py
│
└── utils/
    ├── __init__.py
    └── helpers.py
```

---

## Nutricionista

**Verônica Alves — CRN/1 20331 — NefroClínicas Brasília-DF**
