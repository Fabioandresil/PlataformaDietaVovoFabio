/* =====================================================================
   PLATAFORMA DE DIETA — VOVÔ FABIO
   Todos os dados estão inline aqui (sem fetch, funciona offline)
   ===================================================================== */

// ── DADOS ─────────────────────────────────────────────────────────────────

const PLANO = {
  "paciente": {
    "nome": "Fabio Silveira",
    "idade": 79,
    "altura_cm": 162,
    "peso_kg": 55.3,
    "imc": 21.1,
    "condicoes": ["Doença Renal Crônica (DRC)", "Pré-diabético", "3 stents coronários"],
    "meta_hidratacao_ml": 2000,
    "meta_copos": 8
  },
  "refeicoes": [
    {
      "nome": "Café da Manhã",
      "horario": "07:00",
      "cor": "#1565C0",
      "itens": [
        "1 fatia de pão de forma integral (sem sal)",
        "1 col. chá de manteiga sem sal",
        "1 fruta de baixo potássio (maçã OU pera OU manga OU goiaba)",
        "1 xícara de chá de ervas (camomila, hortelã ou erva-cidreira) — SEM açúcar ou adoçante"
      ],
      "notas": ["Nunca pular o café da manhã", "Frutas tropicais devem ser consumidas com moderação"],
      "variacoes_de_pratos": [
        {
          "nome": "Café Tradicional",
          "descricao": "Pão integral com manteiga sem sal + fruta + chá de ervas",
          "ingredientes_principais": ["Pão de forma integral (sem sal)", "Manteiga sem sal", "Maçã", "Chá de camomila"]
        },
        {
          "nome": "Crepioca Salgada",
          "descricao": "Panqueca de tapioca com ovo + fruta + chá",
          "ingredientes_principais": ["Tapioca (goma)", "Ovo", "Queijo branco (pouco)", "Maçã", "Chá de hortelã"]
        },
        {
          "nome": "Mingau de Aveia",
          "descricao": "Mingau de aveia com fruta amassada + chá",
          "ingredientes_principais": ["Aveia em flocos", "Leite (ou água)", "Banana amassada", "Canela em pó", "Chá de camomila"]
        }
      ]
    },
    {
      "nome": "Lanche da Manhã",
      "horario": "10:00",
      "cor": "#2E7D32",
      "itens": [
        "1 fruta de baixo potássio (maçã, pera, manga OU goiaba)",
        "OU 1 porção de bolacha água e sal (3 unidades, sem excesso de sal)"
      ],
      "notas": ["Lanche leve para não prejudicar o almoço", "Se com pouca fome, apenas a fruta"],
      "variacoes_de_pratos": [
        {
          "nome": "Fruta + Chá",
          "descricao": "Fruta de baixo potássio com chá de ervas",
          "ingredientes_principais": ["Pera", "Chá de erva-cidreira"]
        },
        {
          "nome": "Bolacha + Fruta",
          "descricao": "Bolacha água e sal + 1 fruta pequena",
          "ingredientes_principais": ["Bolacha água e sal (3 un.)", "Maçã pequena"]
        },
        {
          "nome": "Iogurte Natural",
          "descricao": "Iogurte natural desnatado sem adoçante",
          "ingredientes_principais": ["Iogurte natural desnatado", "Canela em pó (pitada)"]
        }
      ]
    },
    {
      "nome": "Almoço",
      "horario": "12:00",
      "cor": "#E65100",
      "itens": [
        "3–4 col. sopa de arroz branco cozido (sem sal, preparado com tempero caseiro)",
        "1 concha pequena de feijão OU lentilha OU ervilha (cozidos sem sal)",
        "1 porção de proteína (frango OU peixe OU carne vermelha — máx. 2×/semana)",
        "1 col. sopa de azeite de oliva extra virgem",
        "Legumes cozidos à vontade: chuchu, abobrinha, cenoura, berinjela, cebola, alho",
        "Salada de folhas verdes: alface, rúcula, agrião (porção moderada)"
      ],
      "notas": [
        "Carne vermelha: MÁXIMO 2 vezes por semana",
        "Usar o Sal de Ervas (receita especial) no lugar do sal comum",
        "Fritar apenas com azeite de oliva extra virgem — NUNCA manteiga ou óleo de soja",
        "Não adicionar sal de cozinha — usar apenas Sal de Ervas"
      ],
      "variacoes_de_pratos": [
        {
          "nome": "Frango Grelhado com Legumes",
          "descricao": "Frango temperado com Sal de Ervas + arroz + legumes cozidos",
          "ingredientes_principais": ["Peito de frango", "Sal de Ervas caseiro", "Arroz branco", "Abobrinha", "Cenoura", "Azeite de oliva extra virgem", "Alho", "Cebola"]
        },
        {
          "nome": "Filé de Peixe Assado",
          "descricao": "Peixe de água doce (tilápia/merluza) assado + arroz + salada",
          "ingredientes_principais": ["Filé de tilápia (ou merluza)", "Limão", "Sal de Ervas caseiro", "Arroz branco", "Alface", "Tomate", "Azeite de oliva extra virgem"]
        },
        {
          "nome": "Carne Moída com Legumes",
          "descricao": "Carne moída refogada (máx 2×/semana) + arroz + feijão + legumes",
          "ingredientes_principais": ["Carne moída (patinho)", "Cebola", "Tomate", "Alho", "Sal de Ervas caseiro", "Arroz branco", "Feijão cozido", "Cenoura cozida", "Azeite de oliva extra virgem"]
        }
      ]
    },
    {
      "nome": "Lanche da Tarde",
      "horario": "15:30",
      "cor": "#6A1B9A",
      "itens": [
        "1 xícara de chá de ervas (camomila, hortelã ou erva-cidreira)",
        "1 fruta pequena (maçã OU pera) OU 3 bolachas água e sal"
      ],
      "notas": ["Horário importante para manter glicose estável", "Não comer biscoitos recheados ou doces industrializados"],
      "variacoes_de_pratos": [
        {
          "nome": "Chá + Bolacha",
          "descricao": "Chá de ervas + bolachas água e sal",
          "ingredientes_principais": ["Chá de camomila", "Bolacha água e sal (3 un.)"]
        },
        {
          "nome": "Fruta + Chá",
          "descricao": "Fruta de baixo potássio + chá de ervas",
          "ingredientes_principais": ["Pera", "Chá de hortelã"]
        },
        {
          "nome": "Torrada Integral",
          "descricao": "Torrada de pão integral + fio de azeite",
          "ingredientes_principais": ["Pão integral torrado", "Azeite de oliva extra virgem (fio)", "Chá de erva-cidreira"]
        }
      ]
    },
    {
      "nome": "Jantar",
      "horario": "19:30",
      "cor": "#00695C",
      "itens": [
        "Sopa de legumes caseira OU caldo de legumes OU prato leve similar ao almoço (porção menor)",
        "Proteína leve: ovo cozido OU omelete simples OU frango desfiado",
        "Pão integral (1 fatia) OU 3 bolachas água e sal",
        "1 fruta pequena (maçã OU pera)"
      ],
      "notas": [
        "Jantar deve ser mais leve que o almoço",
        "Comer pelo menos 2 horas antes de dormir",
        "Sopa caseira é a melhor opção: controle total dos ingredientes e sódio"
      ],
      "variacoes_de_pratos": [
        {
          "nome": "Sopa de Legumes Caseira",
          "descricao": "Sopa de abobrinha, cenoura e batata com caldo caseiro sem sal",
          "ingredientes_principais": ["Abobrinha", "Cenoura", "Batata (porção pequena)", "Cebola", "Alho", "Azeite de oliva extra virgem", "Cheiro-verde", "Sal de Ervas caseiro"]
        },
        {
          "nome": "Omelete Simples + Salada",
          "descricao": "Omelete com 2 ovos + salada de alface e tomate",
          "ingredientes_principais": ["Ovo (2 unidades)", "Azeite de oliva extra virgem", "Alface", "Tomate", "Sal de Ervas caseiro"]
        },
        {
          "nome": "Frango Desfiado + Pão Integral",
          "descricao": "Frango desfiado temperado + 1 fatia de pão integral + fruta",
          "ingredientes_principais": ["Peito de frango cozido desfiado", "Limão", "Cheiro-verde", "Pão de forma integral (sem sal)", "Maçã"]
        }
      ]
    }
  ]
};

const RECEITAS = [
  {
    "nome": "Crepioca Salgada",
    "tipo": "Café da Manhã / Lanche",
    "ingredientes": ["2 ovos", "3 col. sopa de tapioca (goma)", "1 col. sopa de queijo branco ralado (pouca quantidade)", "Sal de Ervas a gosto", "Azeite para untar a frigideira"],
    "modo_preparo": ["Misture os ovos e a tapioca em um bowl até formar uma massa homogênea.", "Adicione o queijo branco ralado e o Sal de Ervas.", "Unte uma frigideira antiaderente com um fio de azeite e aqueça em fogo médio.", "Despeje a massa e espalhe uniformemente (como uma panqueca).", "Deixe dourar por 2–3 minutos, vire e doure do outro lado.", "Sirva com uma fruta de baixo potássio e chá de ervas."]
  },
  {
    "nome": "Espaguete de Vegetais",
    "tipo": "Almoço / Jantar",
    "ingredientes": ["2 abobrinhas médias (espiralizadas)", "1 cenoura grande (espiralizada)", "1 xícara de molho de tomate caseiro (sem sal)", "2 dentes de alho", "Cebola a gosto", "Azeite de oliva extra virgem", "Sal de Ervas a gosto", "Cheiro-verde a gosto"],
    "modo_preparo": ["Espiralize a abobrinha e a cenoura (use um espirilizador ou descascador).", "Refogue o alho e a cebola no azeite em fogo médio até dourar.", "Adicione o molho de tomate e deixe reduzir por 5 minutos.", "Adicione os legumes espiralizados e mexa por 2–3 minutos (fica al dente).", "Tempere com Sal de Ervas e cheiro-verde.", "Sirva imediatamente."]
  },
  {
    "nome": "Nuggets de Frango Assado",
    "tipo": "Almoço / Jantar",
    "ingredientes": ["300g de peito de frango", "2 col. sopa de farinha de aveia", "1 ovo", "Sal de Ervas a gosto", "Limão (suco)", "Azeite de oliva (para pincelar)", "Alho e cebola em pó a gosto"],
    "modo_preparo": ["Corte o frango em cubos e tempere com Sal de Ervas, limão e alho/cebola em pó.", "Passe os cubos no ovo batido e depois na farinha de aveia.", "Disponha em assadeira forrada com papel manteiga.", "Pincele levemente com azeite.", "Asse em forno pré-aquecido a 200°C por 20–25 minutos.", "Vire na metade do tempo para dourar dos dois lados."]
  },
  {
    "nome": "Muffin de Legumes",
    "tipo": "Lanche / Café",
    "ingredientes": ["2 ovos", "1/2 xícara de farinha de aveia", "1/2 abobrinha ralada", "1/2 cenoura ralada", "1 col. sopa de azeite de oliva", "Sal de Ervas a gosto", "Cheiro-verde picado"],
    "modo_preparo": ["Pré-aqueça o forno a 180°C.", "Misture os ovos com o azeite até homogeneizar.", "Adicione a farinha de aveia e misture bem.", "Incorpore a abobrinha e cenoura raladas, o cheiro-verde e o Sal de Ervas.", "Distribua a massa em forminhas de muffin (unte com azeite).", "Asse por 25–30 minutos ou até dourar.", "Espere amornar antes de desenformar."]
  },
  {
    "nome": "Omelete de Carne Moída",
    "tipo": "Almoço / Jantar",
    "ingredientes": ["3 ovos", "80g de carne moída (patinho)", "1 tomate picado sem sementes", "Cebola e alho a gosto", "Sal de Ervas a gosto", "Azeite de oliva", "Cheiro-verde"],
    "modo_preparo": ["Refogue a carne moída com alho e cebola no azeite até cozinhar.", "Adicione o tomate picado e refogue mais 2 minutos.", "Bata os ovos e tempere com Sal de Ervas.", "Em frigideira antiaderente, despeje os ovos batidos.", "Coloque o recheio de carne moída sobre metade da omelete.", "Dobre a omelete ao meio e deixe firmar por 1 minuto.", "Finalize com cheiro-verde picado."]
  },
  {
    "nome": "Croquete de Grão-de-Bico",
    "tipo": "Lanche / Entrada",
    "ingredientes": ["1 xícara de grão-de-bico cozido (sem sal)", "1 ovo", "2 col. sopa de farinha de aveia", "Cebola e alho a gosto", "Sal de Ervas a gosto", "Salsinha picada", "Azeite para pincelar"],
    "modo_preparo": ["Amasse o grão-de-bico com um garfo até virar pasta (pode restar pedaços).", "Refogue o alho e a cebola no azeite e misture ao grão-de-bico.", "Adicione o ovo, a farinha de aveia, o Sal de Ervas e a salsinha.", "Modele em croquetes pequenos.", "Disponha em assadeira forrada com papel manteiga e pincele com azeite.", "Asse a 200°C por 20 minutos, virando na metade."]
  },
  {
    "nome": "Quibe de Atum",
    "tipo": "Almoço / Jantar",
    "ingredientes": ["1 lata de atum em água (escorrido e dessalgado)", "1 xícara de trigo para quibe hidratado", "1 cebola pequena", "Sal de Ervas a gosto", "Hortelã fresca picada", "1 ovo", "Azeite de oliva"],
    "modo_preparo": ["Hidrate o trigo para quibe em água por 15 minutos; esprema o excesso.", "Misture o atum escorrido, o trigo, a cebola picada, o ovo e o Sal de Ervas.", "Adicione a hortelã fresca picada e misture bem.", "Modele em formato oval (quibes) e disponha em assadeira.", "Pincele com azeite de oliva.", "Asse a 200°C por 25–30 minutos até dourar."]
  },
  {
    "nome": "Sorvete de Manga",
    "tipo": "Sobremesa",
    "ingredientes": ["2 mangas maduras (polpa)", "2 col. sopa de iogurte natural desnatado", "Suco de 1 limão"],
    "modo_preparo": ["Corte a polpa das mangas em cubos e congele por pelo menos 4 horas.", "Bata a manga congelada no liquidificador ou processador.", "Adicione o iogurte natural e o suco de limão enquanto bate.", "Bata até consistência cremosa.", "Sirva imediatamente (sorvete mole) ou volte ao freezer por 1 hora para firmar.", "Guarde em pote tampado no freezer por até 7 dias."]
  },
  {
    "nome": "Suflê de Brócolis",
    "tipo": "Almoço / Jantar",
    "ingredientes": ["2 xícaras de brócolis cozido e picado", "3 ovos (gemas e claras separadas)", "1 col. sopa de farinha de aveia", "Azeite de oliva", "Sal de Ervas a gosto", "Queijo branco ralado (pouca quantidade — opcional)"],
    "modo_preparo": ["Pré-aqueça o forno a 200°C.", "Misture as gemas com a farinha de aveia, o brócolis, o Sal de Ervas e o azeite.", "Bata as claras em neve firme.", "Incorpore as claras à mistura de brócolis delicadamente (movimento de baixo para cima).", "Despeje em ramequins untados com azeite.", "Polvilhe queijo branco se desejar.", "Asse por 20–25 minutos até firmar e dourar."]
  }
];

const ORIENTACOES = {
  "orientacoes_gerais": [
    "Fazer pelo menos 30 min de caminhada leve por dia (conforme tolerância)",
    "Comer devagar, mastigando bem cada garfada",
    "Manter horários regulares das refeições todos os dias",
    "Não pular refeições — mantém glicose e energia estáveis",
    "Evitar alimentos ultraprocessados, embutidos, enlatados e fastfood",
    "Verificar o rótulo dos produtos: procurar por sódio < 100mg por porção",
    "Usar sempre o Sal de Ervas caseiro no lugar do sal comum",
    "Preparar as refeições em casa com ingredientes frescos sempre que possível"
  ],
  "alimentos_proibidos": {
    "por_sodio_alto": ["Sal de cozinha (NaCl) — substituir pelo Sal de Ervas caseiro", "Temperos prontos industrializados (Maggi, Knorr etc.)", "Molho shoyu / soja", "Molho inglês", "Catchup e mostarda industrializados", "Alimentos em conserva (picles, azeitona, palmito em lata)", "Embutidos e frios (salsicha, presunto, mortadela, linguiça, salame)", "Queijos curados e amarelos (parmesão, cheddar, provolone)", "Salgadinhos de pacote e chips", "Biscoitos recheados e industrializados salgados", "Macarrão instantâneo (Miojo)", "Caldos e sopas industrializados"],
    "por_potassio_alto": ["Banana-nanica (grande)", "Abacate", "Melão cantaloupe", "Kiwi em excesso", "Espinafre cru em grandes quantidades", "Batata inglesa em grandes quantidades", "Tomate em excesso (cozido concentrado)", "Feijão preto em excesso"],
    "por_fosforo_alto": ["Refrigerantes (especialmente cola — contêm fósforo inorgânico)", "Cerveja e bebidas alcoólicas", "Achocolatado e chocolates ao leite", "Leite integral em grandes quantidades", "Queijos amarelos e curados"],
    "absolutamente_proibidos": ["CARAMBOLA (estrela-do-mar) — NEUROTÓXICO PARA RINS", "BIRIRI / PITANGA-DA-CAATINGA — NEUROTÓXICO PARA RINS", "Álcool em qualquer quantidade"]
  },
  "alerta_critico": {
    "titulo": "⚠️ PERIGO DE VIDA — JAMAIS CONSUMA",
    "itens": ["CARAMBOLA (Averrhoa carambola) — estrela-do-mar", "BIRIRI / Pitanga-da-Caatinga (Byrsonima crassifolia)"],
    "motivo": "Esses frutos contêm neurotoxinas que NÃO são eliminadas pelos rins com doença renal crônica. Podem causar solavancos, convulsões, confusão mental e óbito. NÃO EXISTEM exceções — nem suco, nem em pequenas quantidades.",
    "sinais_de_alerta": ["Solavancos ou soluços persistentes", "Confusão mental ou desorientação", "Fraqueza súbita ou dormência", "Qualquer sintoma neurológico após consumo"]
  },
  "dica_hidratacao": "Beba 1 copo de água a cada 1 hora acordado. Meta: 2 litros por dia (8 copos de 250ml). Água de coco com moderação é permitida. Evite sucos concentrados.",
  "regra_proteina": "Coma proteína animal em TODAS as refeições principais (almoço e jantar): frango, peixe, ovo ou carne vermelha magra. Proteínas vegetais (feijão, lentilha, grão-de-bico) complementam — não substituem.",
  "regra_carne_vermelha": "Carne vermelha: MÁXIMO 2 vezes por semana. Prefira cortes magros: patinho, coxão mole, alcatra. Evite: costela, picanha, fraldinha, gorduras visíveis."
};

const SUPLEMENTACAO = [
  {
    "nome": "Forza Nutricci",
    "tipo": "Suplemento Proteico Renal",
    "posologia": "1 scoop (porção) antes de dormir, diluído em 200ml de água",
    "objetivo": "Suprir necessidade proteica específica para pacientes com DRC",
    "obs": "Não substituir refeições. Usar conforme orientação da nutricionista.",
    "cor": "#1565C0",
    "contatos": ["TopMed: (61) 99999-0001", "Benenutri: (61) 99999-0002", "Viva Medicamentos: (61) 3322-0003"]
  },
  {
    "nome": "OmegaFor Plus",
    "tipo": "Ômega-3 Premium",
    "posologia": "2 cápsulas após o almoço + 1 cápsula após o jantar",
    "objetivo": "Proteção cardiovascular, anti-inflamatório, saúde renal",
    "obs": "Tomar com alimento para melhor absorção e evitar desconforto gástrico.",
    "cor": "#E65100",
    "contatos": ["TopMed: (61) 99999-0001", "Benenutri: (61) 99999-0002", "Viva Medicamentos: (61) 3322-0003"]
  }
];

const SAL_ERVAS = {
  "nome": "Sal de Ervas Caseiro",
  "descricao": "Tempero especial com baixo teor de sódio para substituir o sal comum",
  "ingredientes": [
    "100g de sal marinho integral grosso",
    "2 col. sopa de alecrim seco",
    "2 col. sopa de tomilho seco",
    "2 col. sopa de orégano seco",
    "2 col. sopa de manjericão seco",
    "1 col. sopa de sálvia seca",
    "1 col. sopa de salsinha desidratada",
    "1 col. sopa de cebolinha desidratada",
    "1 col. chá de pimenta-do-reino branca"
  ],
  "modo_preparo": [
    "Certifique-se que todas as ervas estão bem secas (sem umidade).",
    "Processe brevemente o sal grosso no liquidificador para ficar mais fino.",
    "Adicione todas as ervas ao liquidificador e processe por 30 segundos.",
    "Misture bem para homogeneizar.",
    "Guarde em pote de vidro bem vedado, longe de luz e umidade.",
    "Validade: até 6 meses em pote fechado."
  ],
  "info_nutricional": {
    "porcao": "1 col. chá rasa (3g)",
    "sodio_mg": 78,
    "sodio_comparacao": "Sal comum tem ~2.300mg por colher de chá — o Sal de Ervas tem 97% menos sódio!"
  },
  "beneficios": [
    "Redução drástica no consumo de sódio (protege os rins e o coração)",
    "Ervas anti-inflamatórias naturais (alecrim, tomilho)",
    "Melhora do sabor dos alimentos sem prejudicar a saúde",
    "Antioxidantes naturais das ervas",
    "Controle da pressão arterial"
  ]
};

// ── ESTADO DA APLICAÇÃO ────────────────────────────────────────────────────

let estado = {
  telaAtual: 'principal',
  fontDelta: 0,
  temaEscuro: false,
  coposhoje: parseInt(localStorage.getItem('coposHoje') || '0'),
  countdownSeg: 3600,    // 60 min
  countdownAtivo: false,
  abaPretos: 0,
  abaRec: 0,
  diasCarne: JSON.parse(localStorage.getItem('diasCarne') || '[]'),
};

// ── FONT ──────────────────────────────────────────────────────────────────

function mudarFonte(delta) {
  estado.fontDelta = Math.max(-4, Math.min(10, estado.fontDelta + delta));
  const base = 18 + estado.fontDelta;
  document.documentElement.style.setProperty('--fnt', base + 'px');
  document.documentElement.style.setProperty('--fnt-titulo', (base + 8) + 'px');
  document.documentElement.style.setProperty('--fnt-sub', (base + 2) + 'px');
  document.documentElement.style.setProperty('--fnt-btn', base + 'px');
  localStorage.setItem('fontDelta', estado.fontDelta);
}

// ── TEMA ─────────────────────────────────────────────────────────────────

function alternarTema() {
  estado.temaEscuro = !estado.temaEscuro;
  document.body.classList.toggle('theme-dark', estado.temaEscuro);
  document.body.classList.toggle('theme-light', !estado.temaEscuro);
  document.getElementById('btn-tema').textContent = estado.temaEscuro ? '☀️' : '🌙';
  localStorage.setItem('temaEscuro', estado.temaEscuro);
}

// ── NAVEGAÇÃO ─────────────────────────────────────────────────────────────

const TITULOS = {
  principal: '🍽️ Dieta — Vovô Fabio',
  pratos: '🍽️ Pratos Sugeridos',
  ingredientes: '📋 Ingredientes',
  preparo: '👨‍🍳 Forma de Preparo',
  supermercado: '🛒 Lista de Supermercado',
  dieta: '📄 Dieta Completa',
  recomendacoes: '⚠️ Recomendações Importantes'
};

function mostrarTela(nome) {
  document.querySelectorAll('.tela').forEach(t => t.classList.remove('active'));
  document.getElementById('tela-' + nome).classList.add('active');
  document.getElementById('header-title').textContent = TITULOS[nome] || nome;
  const btnVoltar = document.getElementById('btn-voltar');
  if (nome === 'principal') {
    btnVoltar.classList.add('hidden');
  } else {
    btnVoltar.classList.remove('hidden');
    carregarTela(nome);
  }
  estado.telaAtual = nome;
  window.scrollTo(0, 0);
}

function carregarTela(nome) {
  switch(nome) {
    case 'pratos': carregarPratos(); break;
    case 'ingredientes': carregarIngredientes(); break;
    case 'preparo': carregarPreparo(); break;
    case 'supermercado': carregarSupermercado(); break;
    case 'dieta': carregarDieta(); break;
    case 'recomendacoes': carregarRecomendacoes(); break;
  }
}

// ── TELA: PRATOS SUGERIDOS ─────────────────────────────────────────────────

let abaAtivaPratos = 0;

function carregarPratos() {
  const abas = document.getElementById('abas-pratos');
  const conteudo = document.getElementById('conteudo-pratos');
  if (abas.dataset.carregado) return; // já construído
  abas.dataset.carregado = '1';

  // Abas: uma por refeição + Receitas FDS
  const labels = PLANO.refeicoes.map(r => r.nome).concat(['👨‍🍳 Receitas FDS']);

  labels.forEach((lbl, i) => {
    const btn = document.createElement('button');
    btn.className = 'aba-btn' + (i === 0 ? ' active' : '');
    btn.textContent = lbl;
    btn.onclick = () => trocarAbaPratos(i);
    abas.appendChild(btn);
  });

  renderAbaPratos(0);
}

function trocarAbaPratos(i) {
  abaAtivaPratos = i;
  document.querySelectorAll('#abas-pratos .aba-btn').forEach((b, j) => {
    b.classList.toggle('active', i === j);
  });
  renderAbaPratos(i);
}

function renderAbaPratos(i) {
  const conteudo = document.getElementById('conteudo-pratos');
  conteudo.innerHTML = '';

  if (i < PLANO.refeicoes.length) {
    const ref = PLANO.refeicoes[i];

    // Card da refeição principal
    const cardPrinc = criarCard(ref.cor, ref.nome + ' — ' + ref.horario, null);
    const corpo = document.createElement('div');
    corpo.className = 'card-body';
    const ul = document.createElement('ul');
    ul.style.paddingLeft = '20px';
    ref.itens.forEach(it => {
      const li = document.createElement('li');
      li.style.marginBottom = '6px';
      li.textContent = it;
      ul.appendChild(li);
    });
    corpo.appendChild(ul);
    if (ref.notas && ref.notas.length) {
      const p = document.createElement('p');
      p.style.cssText = 'margin-top:12px;color:var(--txt2);font-size:0.92em;';
      p.innerHTML = '📌 <em>' + ref.notas.join(' &nbsp;·&nbsp; ') + '</em>';
      corpo.appendChild(p);
    }
    cardPrinc.appendChild(corpo);
    conteudo.appendChild(cardPrinc);

    // Variações
    const h3 = document.createElement('h3');
    h3.style.cssText = 'margin:16px 0 10px;font-size:var(--fnt-sub);';
    h3.textContent = '🔄 Variações de Pratos';
    conteudo.appendChild(h3);

    ref.variacoes_de_pratos.forEach(v => {
      const card = criarCard(ref.cor, v.nome, v.descricao);
      const cb = document.createElement('div');
      cb.className = 'card-body';
      cb.innerHTML = '<strong>Ingredientes principais:</strong><ul style="padding-left:20px;margin-top:6px">' +
        v.ingredientes_principais.map(ing => `<li style="margin-bottom:4px">${ing}</li>`).join('') + '</ul>';
      card.appendChild(cb);
      conteudo.appendChild(card);
    });

  } else {
    // Receitas FDS
    const h3 = document.createElement('h3');
    h3.style.cssText = 'margin-bottom:14px;font-size:var(--fnt-sub);';
    h3.textContent = '👨‍🍳 Receitas de Fim de Semana';
    conteudo.appendChild(h3);

    RECEITAS.forEach(r => {
      const card = criarCard('#37474F', r.nome, r.tipo);
      const cb = document.createElement('div');
      cb.className = 'card-body';
      cb.innerHTML = '<strong>Ingredientes:</strong><ul style="padding-left:20px;margin-top:6px">' +
        r.ingredientes.map(ing => `<li style="margin-bottom:4px">${ing}</li>`).join('') + '</ul>';
      card.appendChild(cb);
      conteudo.appendChild(card);
    });
  }
}

function criarCard(cor, titulo, subtitulo) {
  const card = document.createElement('div');
  card.className = 'card';
  const header = document.createElement('div');
  header.className = 'card-header';
  header.style.background = cor;
  header.innerHTML = `<h3>${titulo}</h3>` + (subtitulo ? `<div class="horario">${subtitulo}</div>` : '');
  card.appendChild(header);
  return card;
}

// ── TELA: INGREDIENTES ────────────────────────────────────────────────────

function carregarIngredientes() {
  const nav = document.getElementById('lista-ingredientes-nav');
  if (nav.dataset.carregado) return;
  nav.dataset.carregado = '1';

  PLANO.refeicoes.forEach(ref => {
    const grp = document.createElement('div');
    grp.className = 'grupo-label';
    grp.textContent = ref.nome;
    nav.appendChild(grp);

    ref.variacoes_de_pratos.forEach((v, vi) => {
      const btn = document.createElement('button');
      btn.className = 'nav-item';
      btn.textContent = v.nome;
      btn.dataset.tipo = 'prato';
      btn.dataset.refIdx = PLANO.refeicoes.indexOf(ref);
      btn.dataset.varIdx = vi;
      btn.onclick = function() { selecionarIngredientes(this); };
      nav.appendChild(btn);
    });
  });

  const grpFds = document.createElement('div');
  grpFds.className = 'grupo-label';
  grpFds.textContent = 'Receitas FDS';
  nav.appendChild(grpFds);

  RECEITAS.forEach((r, ri) => {
    const btn = document.createElement('button');
    btn.className = 'nav-item';
    btn.textContent = r.nome;
    btn.dataset.tipo = 'receita';
    btn.dataset.recIdx = ri;
    btn.onclick = function() { selecionarIngredientes(this); };
    nav.appendChild(btn);
  });
}

function selecionarIngredientes(btn) {
  document.querySelectorAll('#lista-ingredientes-nav .nav-item').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  const detalhe = document.getElementById('detalhe-ingredientes');
  detalhe.innerHTML = '';

  let titulo = '', ings = [];

  if (btn.dataset.tipo === 'prato') {
    const ref = PLANO.refeicoes[parseInt(btn.dataset.refIdx)];
    const v = ref.variacoes_de_pratos[parseInt(btn.dataset.varIdx)];
    titulo = v.nome;
    ings = v.ingredientes_principais;
  } else {
    const r = RECEITAS[parseInt(btn.dataset.recIdx)];
    titulo = r.nome;
    ings = r.ingredientes;
  }

  const h3 = document.createElement('h3');
  h3.style.cssText = 'margin-bottom:12px;font-size:var(--fnt-sub);';
  h3.textContent = '📋 ' + titulo;
  detalhe.appendChild(h3);

  ings.forEach(ing => {
    const row = document.createElement('div');
    row.className = 'ing-row';
    row.textContent = '• ' + ing;
    detalhe.appendChild(row);
  });
}

// ── TELA: FORMA DE PREPARO ────────────────────────────────────────────────

function carregarPreparo() {
  const nav = document.getElementById('lista-preparo-nav');
  if (nav.dataset.carregado) return;
  nav.dataset.carregado = '1';

  const grpFds = document.createElement('div');
  grpFds.className = 'grupo-label';
  grpFds.textContent = 'Receitas Passo a Passo';
  nav.appendChild(grpFds);

  RECEITAS.forEach((r, ri) => {
    const btn = document.createElement('button');
    btn.className = 'nav-item';
    btn.textContent = r.nome;
    btn.dataset.recIdx = ri;
    btn.onclick = function() { selecionarPreparo(this); };
    nav.appendChild(btn);
  });

  // Sal de Ervas
  const grpSe = document.createElement('div');
  grpSe.className = 'grupo-label';
  grpSe.textContent = 'Tempero Especial';
  nav.appendChild(grpSe);

  const btnSe = document.createElement('button');
  btnSe.className = 'nav-item';
  btnSe.textContent = '🌿 Sal de Ervas';
  btnSe.dataset.tipo = 'salervas';
  btnSe.onclick = function() { selecionarPreparo(this); };
  nav.appendChild(btnSe);
}

function selecionarPreparo(btn) {
  document.querySelectorAll('#lista-preparo-nav .nav-item').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');

  const detalhe = document.getElementById('detalhe-preparo');
  detalhe.innerHTML = '';

  let titulo = '', passos = [];

  if (btn.dataset.tipo === 'salervas') {
    titulo = SAL_ERVAS.nome;
    passos = SAL_ERVAS.modo_preparo;
  } else {
    const r = RECEITAS[parseInt(btn.dataset.recIdx)];
    titulo = r.nome;
    passos = r.modo_preparo;
  }

  const h3 = document.createElement('h3');
  h3.style.cssText = 'margin-bottom:16px;font-size:var(--fnt-sub);';
  h3.textContent = '👨‍🍳 ' + titulo;
  detalhe.appendChild(h3);

  passos.forEach((p, i) => {
    const row = document.createElement('div');
    row.className = 'passo-row';
    const num = document.createElement('span');
    num.className = 'passo-num';
    num.textContent = 'Passo ' + (i + 1);
    const txt = document.createElement('span');
    txt.className = 'passo-txt';
    txt.textContent = p;
    row.appendChild(num);
    row.appendChild(txt);
    detalhe.appendChild(row);
  });
}

// ── TELA: LISTA DE SUPERMERCADO ───────────────────────────────────────────

const CATEGORIAS_KEYWORDS = {
  'Proteínas': ['frango', 'peixe', 'carne', 'atum', 'ovo', 'tilápia', 'merluza', 'patinho'],
  'Laticínios': ['leite', 'iogurte', 'queijo', 'manteiga'],
  'Grãos e Cereais': ['arroz', 'feijão', 'lentilha', 'ervilha', 'grão-de-bico', 'aveia', 'tapioca', 'farinha', 'trigo', 'pão'],
  'Legumes e Verduras': ['abobrinha', 'cenoura', 'chuchu', 'berinjela', 'brócolis', 'tomate', 'cebola', 'alface', 'rúcula', 'agrião', 'batata'],
  'Frutas': ['maçã', 'pera', 'manga', 'goiaba', 'banana', 'limão'],
  'Temperos e Óleos': ['azeite', 'alho', 'cheiro-verde', 'salsinha', 'cebolinha', 'sal de ervas', 'hortelã', 'canela'],
  'Bebidas e Infusões': ['chá', 'camomila', 'erva-cidreira', 'hortelã'],
  'Outros': []
};

function categorizar(ing) {
  const lower = ing.toLowerCase();
  for (const [cat, keywords] of Object.entries(CATEGORIAS_KEYWORDS)) {
    if (keywords.some(kw => lower.includes(kw))) return cat;
  }
  return 'Outros';
}

function carregarSupermercado() {
  const cont = document.getElementById('checkboxes-pratos');
  if (cont.dataset.carregado) return;
  cont.dataset.carregado = '1';

  PLANO.refeicoes.forEach(ref => {
    const grp = document.createElement('div');
    grp.className = 'check-grupo';
    grp.textContent = ref.nome;
    cont.appendChild(grp);

    ref.variacoes_de_pratos.forEach((v, vi) => {
      const lbl = document.createElement('label');
      lbl.className = 'check-label';
      const chk = document.createElement('input');
      chk.type = 'checkbox';
      chk.dataset.refIdx = PLANO.refeicoes.indexOf(ref);
      chk.dataset.varIdx = vi;
      chk.addEventListener('change', atualizarLista);
      lbl.appendChild(chk);
      lbl.appendChild(document.createTextNode(v.nome));
      cont.appendChild(lbl);
    });
  });

  const grpFds = document.createElement('div');
  grpFds.className = 'check-grupo';
  grpFds.textContent = 'Receitas FDS';
  cont.appendChild(grpFds);

  RECEITAS.forEach((r, ri) => {
    const lbl = document.createElement('label');
    lbl.className = 'check-label';
    const chk = document.createElement('input');
    chk.type = 'checkbox';
    chk.dataset.tipo = 'receita';
    chk.dataset.recIdx = ri;
    chk.addEventListener('change', atualizarLista);
    lbl.appendChild(chk);
    lbl.appendChild(document.createTextNode(r.nome));
    cont.appendChild(lbl);
  });
}

function atualizarLista() {
  const ingsSet = new Set();
  document.querySelectorAll('#checkboxes-pratos input[type=checkbox]:checked').forEach(chk => {
    let ings = [];
    if (chk.dataset.tipo === 'receita') {
      ings = RECEITAS[parseInt(chk.dataset.recIdx)].ingredientes;
    } else {
      const ref = PLANO.refeicoes[parseInt(chk.dataset.refIdx)];
      ings = ref.variacoes_de_pratos[parseInt(chk.dataset.varIdx)].ingredientes_principais;
    }
    ings.forEach(i => ingsSet.add(i));
  });

  const output = document.getElementById('lista-compras-output');
  if (!ingsSet.size) {
    output.innerHTML = '<p class="placeholder">← Marque pratos para gerar a lista</p>';
    return;
  }

  // Agrupar por categoria
  const grupos = {};
  ingsSet.forEach(ing => {
    const cat = categorizar(ing);
    if (!grupos[cat]) grupos[cat] = [];
    grupos[cat].push(ing);
  });

  output.innerHTML = '';
  for (const [cat, ings] of Object.entries(grupos)) {
    if (!ings.length) continue;
    const titulo = document.createElement('div');
    titulo.className = 'cat-titulo';
    titulo.textContent = '📦 ' + cat;
    output.appendChild(titulo);
    ings.forEach(ing => {
      const item = document.createElement('div');
      item.className = 'lista-item';
      item.textContent = ing;
      output.appendChild(item);
    });
  }
}

function limparSelecao() {
  document.querySelectorAll('#checkboxes-pratos input[type=checkbox]').forEach(c => c.checked = false);
  atualizarLista();
}

function copiarLista() {
  const output = document.getElementById('lista-compras-output');
  const texto = gerarTextoLista();
  if (!texto) { alert('Selecione pratos primeiro!'); return; }
  navigator.clipboard.writeText(texto).then(() => alert('Lista copiada para a área de transferência! ✅'));
}

function salvarLista() {
  const texto = gerarTextoLista();
  if (!texto) { alert('Selecione pratos primeiro!'); return; }
  const blob = new Blob([texto], {type: 'text/plain;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'lista_compras_vovoFabio.txt';
  a.click();
  URL.revokeObjectURL(url);
}

function gerarTextoLista() {
  const output = document.getElementById('lista-compras-output');
  const placeholder = output.querySelector('.placeholder');
  if (placeholder) return '';
  return '🛒 LISTA DE COMPRAS — VOVÔ FABIO\n' +
    new Date().toLocaleDateString('pt-BR') + '\n\n' +
    Array.from(output.querySelectorAll('.cat-titulo, .lista-item'))
      .map(el => el.classList.contains('cat-titulo') ? '\n' + el.textContent : '  • ' + el.textContent)
      .join('\n');
}

// ── TELA: DIETA COMPLETA ──────────────────────────────────────────────────

function carregarDieta() {
  const cont = document.getElementById('conteudo-dieta');
  if (cont.dataset.carregado) return;
  cont.dataset.carregado = '1';

  const p = PLANO.paciente;
  const cardPac = document.createElement('div');
  cardPac.className = 'paciente-card';
  cardPac.innerHTML = `
    <h2>👤 ${p.nome}</h2>
    <p>
      <strong>Idade:</strong> ${p.idade} anos &nbsp;·&nbsp;
      <strong>Altura:</strong> ${p.altura_cm} cm &nbsp;·&nbsp;
      <strong>Peso:</strong> ${p.peso_kg} kg &nbsp;·&nbsp;
      <strong>IMC:</strong> ${p.imc}<br>
      <strong>Condições:</strong> ${p.condicoes.join(', ')}<br>
      <strong>Meta de Hidratação:</strong> ${p.meta_hidratacao_ml}ml/dia (${p.meta_copos} copos)
    </p>`;
  cont.appendChild(cardPac);

  PLANO.refeicoes.forEach(ref => {
    const titulo = document.createElement('div');
    titulo.className = 'ref-titulo';
    titulo.innerHTML = `🕐 ${ref.horario} — ${ref.nome}`;
    cont.appendChild(titulo);

    ref.itens.forEach(it => {
      const item = document.createElement('div');
      item.className = 'ref-item';
      item.textContent = it;
      cont.appendChild(item);
    });

    if (ref.notas && ref.notas.length) {
      ref.notas.forEach(n => {
        const nota = document.createElement('div');
        nota.className = 'ref-nota';
        nota.textContent = '📌 ' + n;
        cont.appendChild(nota);
      });
    }

    const div = document.createElement('hr');
    div.className = 'divider';
    cont.appendChild(div);
  });

  // Suplementação
  const sup = document.createElement('div');
  sup.className = 'ref-titulo';
  sup.textContent = '💊 Suplementação';
  cont.appendChild(sup);

  SUPLEMENTACAO.forEach(s => {
    const it = document.createElement('div');
    it.className = 'ref-item';
    it.innerHTML = `<strong>${s.nome}</strong>: ${s.posologia}`;
    cont.appendChild(it);
  });

  const footer = document.createElement('p');
  footer.className = 'nutricionista-footer';
  footer.textContent = 'Verônica Alves — CRN/1 20331 — NefroClínicas Brasília-DF';
  cont.appendChild(footer);
}

// ── TELA: RECOMENDAÇÕES ───────────────────────────────────────────────────

let abaAtivaRec = 0;

const ABAS_REC = [
  { label: '💧 Hidratação', fn: renderRecHidratacao },
  { label: '🥩 Proteínas', fn: renderRecProteina },
  { label: '⚠️ Orientações', fn: renderRecOrientacoes },
  { label: '💊 Suplementos', fn: renderRecSupl },
  { label: '🌿 Sal de Ervas', fn: renderRecSalErvas }
];

function carregarRecomendacoes() {
  const abas = document.getElementById('abas-rec');
  if (abas.dataset.carregado) return;
  abas.dataset.carregado = '1';

  ABAS_REC.forEach((a, i) => {
    const btn = document.createElement('button');
    btn.className = 'aba-btn' + (i === 0 ? ' active' : '');
    btn.textContent = a.label;
    btn.onclick = () => trocarAbaRec(i);
    abas.appendChild(btn);
  });

  renderRecHidratacao();
}

function trocarAbaRec(i) {
  abaAtivaRec = i;
  document.querySelectorAll('#abas-rec .aba-btn').forEach((b, j) => b.classList.toggle('active', i === j));
  ABAS_REC[i].fn();
}

function renderRecHidratacao() {
  const cont = document.getElementById('conteudo-rec');
  cont.innerHTML = '';

  const card = document.createElement('div');
  card.className = 'hidra-card';
  card.innerHTML = `
    <h3>⏱️ Próximo lembrete de água</h3>
    <div class="timer-grande" id="rec-countdown">${formatarTempo(estado.countdownSeg)}</div>
    <progress class="progresso" id="rec-prog" max="3600" value="${estado.countdownSeg}"></progress>
    <h3 style="margin-top:16px">🥛 Copos hoje</h3>
    <div class="copos-grande" id="rec-copos">${estado.coposhoje}/8</div>
    <progress class="progresso" id="rec-copos-prog" max="8" value="${estado.coposhoje}" style="accent-color:#2E7D32"></progress>
    <button class="btn-nav" style="--cor:#2E7D32;--corh:#1B5E20;margin-top:10px" onclick="bebiCopo()">
      💧 Bebi meu copo!
    </button>
    <p style="margin-top:16px;color:var(--txt2);font-size:0.92em">${ORIENTACOES.dica_hidratacao}</p>`;
  cont.appendChild(card);
}

function renderRecProteina() {
  const cont = document.getElementById('conteudo-rec');
  cont.innerHTML = '';

  const h3 = document.createElement('h3');
  h3.style.cssText = 'margin-bottom:10px;font-size:var(--fnt-sub);';
  h3.textContent = '🥩 Regras de Proteína';
  cont.appendChild(h3);

  [ORIENTACOES.regra_proteina, ORIENTACOES.regra_carne_vermelha].forEach(r => {
    const item = document.createElement('div');
    item.className = 'rec-item';
    item.textContent = r;
    cont.appendChild(item);
  });

  const h4 = document.createElement('h3');
  h4.style.cssText = 'margin:20px 0 10px;font-size:var(--fnt-sub);';
  h4.textContent = '📅 Controle de Carne Vermelha (semana atual)';
  cont.appendChild(h4);

  const semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];
  semana.forEach((dia, i) => {
    const lbl = document.createElement('label');
    lbl.className = 'check-label';
    const chk = document.createElement('input');
    chk.type = 'checkbox';
    chk.checked = estado.diasCarne.includes(i);
    chk.addEventListener('change', function() {
      if (this.checked) {
        if (estado.diasCarne.length >= 2) {
          alert('⚠️ Máximo de 2 vezes por semana!');
          this.checked = false;
          return;
        }
        estado.diasCarne.push(i);
      } else {
        estado.diasCarne = estado.diasCarne.filter(d => d !== i);
      }
      localStorage.setItem('diasCarne', JSON.stringify(estado.diasCarne));
      chk.parentElement.style.fontWeight = chk.checked ? 'bold' : 'normal';
    });
    lbl.appendChild(chk);
    lbl.appendChild(document.createTextNode(dia));
    lbl.style.fontWeight = estado.diasCarne.includes(i) ? 'bold' : 'normal';
    cont.appendChild(lbl);
  });

  const info = document.createElement('p');
  info.style.cssText = 'margin-top:12px;color:var(--txt2);font-size:0.9em;';
  info.textContent = `Consumido esta semana: ${estado.diasCarne.length}/2 vezes`;
  cont.appendChild(info);
}

function renderRecOrientacoes() {
  const cont = document.getElementById('conteudo-rec');
  cont.innerHTML = '';

  // Alerta crítico
  const alerta = document.createElement('div');
  alerta.className = 'alerta-critico';
  const ac = ORIENTACOES.alerta_critico;
  alerta.innerHTML = `
    <h2>🚨 ${ac.titulo}</h2>
    <p>${ac.itens.map(i => '❌ ' + i).join('<br>')}</p>
    <p style="margin-top:12px;font-size:0.9em;opacity:.9">${ac.motivo}</p>
    <p style="margin-top:10px;font-size:0.85em">Sinais de alerta: ${ac.sinais_de_alerta.join(' · ')}</p>`;
  cont.appendChild(alerta);

  const h3 = document.createElement('h3');
  h3.style.cssText = 'margin:16px 0 10px;font-size:var(--fnt-sub);';
  h3.textContent = '✅ Orientações Gerais';
  cont.appendChild(h3);

  ORIENTACOES.orientacoes_gerais.forEach(or => {
    const item = document.createElement('div');
    item.className = 'rec-item';
    item.textContent = or;
    cont.appendChild(item);
  });

  const h4 = document.createElement('h3');
  h4.style.cssText = 'margin:20px 0 10px;font-size:var(--fnt-sub);color:#B71C1C;';
  h4.textContent = '🚫 Alimentos Proibidos';
  cont.appendChild(h4);

  const grupos = ORIENTACOES.alimentos_proibidos;
  const labels = {
    'por_sodio_alto': 'Por Sódio Alto',
    'por_potassio_alto': 'Por Potássio Alto',
    'por_fosforo_alto': 'Por Fósforo Alto',
    'absolutamente_proibidos': '🚨 Absolutamente Proibidos'
  };
  for (const [key, ings] of Object.entries(grupos)) {
    const grp = document.createElement('div');
    grp.className = 'grupo-label';
    grp.textContent = labels[key] || key;
    cont.appendChild(grp);
    ings.forEach(it => {
      const item = document.createElement('div');
      item.className = 'proib-item';
      item.textContent = it;
      cont.appendChild(item);
    });
  }
}

function renderRecSupl() {
  const cont = document.getElementById('conteudo-rec');
  cont.innerHTML = '';

  SUPLEMENTACAO.forEach(s => {
    const card = document.createElement('div');
    card.className = 'supl-card';
    card.style.background = s.cor;
    card.innerHTML = `
      <h3>💊 ${s.nome}</h3>
      <p><strong>Tipo:</strong> ${s.tipo}<br>
         <strong>Posologia:</strong> ${s.posologia}<br>
         <strong>Objetivo:</strong> ${s.objetivo}<br>
         <em>${s.obs}</em></p>`;
    cont.appendChild(card);

    const h4 = document.createElement('h3');
    h4.style.cssText = 'margin:10px 0 6px;font-size:var(--fnt);';
    h4.textContent = '📞 Onde Comprar:';
    cont.appendChild(h4);

    s.contatos.forEach(c => {
      const item = document.createElement('div');
      item.className = 'rec-item';
      item.textContent = c;
      cont.appendChild(item);
    });

    const spacer = document.createElement('hr');
    spacer.className = 'divider';
    cont.appendChild(spacer);
  });
}

function renderRecSalErvas() {
  const cont = document.getElementById('conteudo-rec');
  cont.innerHTML = '';

  const h3 = document.createElement('h3');
  h3.style.cssText = 'margin-bottom:12px;font-size:var(--fnt-sub);';
  h3.textContent = '🌿 ' + SAL_ERVAS.nome;
  cont.appendChild(h3);

  const desc = document.createElement('div');
  desc.className = 'rec-item';
  desc.textContent = SAL_ERVAS.descricao;
  cont.appendChild(desc);

  const h4 = document.createElement('h3');
  h4.style.cssText = 'margin:14px 0 8px;font-size:var(--fnt);';
  h4.textContent = '🧂 Ingredientes';
  cont.appendChild(h4);

  SAL_ERVAS.ingredientes.forEach(ing => {
    const item = document.createElement('div');
    item.className = 'ing-row';
    item.textContent = '• ' + ing;
    cont.appendChild(item);
  });

  const h5 = document.createElement('h3');
  h5.style.cssText = 'margin:14px 0 8px;font-size:var(--fnt);';
  h5.textContent = '👨‍🍳 Modo de Preparo';
  cont.appendChild(h5);

  SAL_ERVAS.modo_preparo.forEach((p, i) => {
    const row = document.createElement('div');
    row.className = 'passo-row';
    const num = document.createElement('span');
    num.className = 'passo-num';
    num.textContent = 'Passo ' + (i + 1);
    const txt = document.createElement('span');
    txt.className = 'passo-txt';
    txt.textContent = p;
    row.appendChild(num);
    row.appendChild(txt);
    cont.appendChild(row);
  });

  const ni = SAL_ERVAS.info_nutricional;
  const infoCard = document.createElement('div');
  infoCard.className = 'rec-item';
  infoCard.style.background = '#E8F5E9';
  infoCard.innerHTML = `<strong>📊 Info Nutricional (${ni.porcao}):</strong><br>
    Sódio: <strong>${ni.sodio_mg}mg</strong><br>
    <em style="color:#2E7D32">${ni.sodio_comparacao}</em>`;
  cont.appendChild(infoCard);

  const hb = document.createElement('h3');
  hb.style.cssText = 'margin:14px 0 8px;font-size:var(--fnt);';
  hb.textContent = '✨ Benefícios';
  cont.appendChild(hb);

  SAL_ERVAS.beneficios.forEach(b => {
    const item = document.createElement('div');
    item.className = 'rec-item';
    item.textContent = '✅ ' + b;
    cont.appendChild(item);
  });
}

// ── HIDRATAÇÃO / TIMER ────────────────────────────────────────────────────

function formatarTempo(seg) {
  const m = Math.floor(seg / 60).toString().padStart(2, '0');
  const s = (seg % 60).toString().padStart(2, '0');
  return m + ':' + s;
}

function bebiCopo() {
  estado.coposhoje = Math.min(estado.coposhoje + 1, 99);
  localStorage.setItem('coposHoje', estado.coposhoje);
  estado.countdownSeg = 3600;

  document.getElementById('copos-count').textContent = estado.coposhoje;
  atualizarRecHidratacao();
}

function atualizarRecHidratacao() {
  const rc = document.getElementById('rec-countdown');
  const rp = document.getElementById('rec-prog');
  const rcp = document.getElementById('rec-copos');
  const rcpp = document.getElementById('rec-copos-prog');
  if (rc) rc.textContent = formatarTempo(estado.countdownSeg);
  if (rp) rp.value = estado.countdownSeg;
  if (rcp) rcp.textContent = estado.coposhoje + '/8';
  if (rcpp) rcpp.value = estado.coposhoje;
}

function tickHidratacao() {
  if (estado.countdownSeg > 0) {
    estado.countdownSeg--;
  } else {
    estado.countdownSeg = 3600;
    document.getElementById('modal-agua').classList.remove('hidden');
  }

  document.getElementById('countdown-display').textContent = formatarTempo(estado.countdownSeg);
  atualizarRecHidratacao();

  setTimeout(tickHidratacao, 1000);
}

function fecharModal() {
  document.getElementById('modal-agua').classList.add('hidden');
}

// ── INICIALIZAÇÃO ─────────────────────────────────────────────────────────

(function init() {
  // Restaurar preferências salvas
  const savedDelta = parseInt(localStorage.getItem('fontDelta') || '0');
  if (savedDelta !== 0) {
    estado.fontDelta = 0; // mudarFonte acumula
    mudarFonte(savedDelta);
  }

  const savedTema = localStorage.getItem('temaEscuro') === 'true';
  if (savedTema) alternarTema();

  // Verificar se copos devem ser resetados (novo dia)
  const hoje = new Date().toDateString();
  const ultimoDia = localStorage.getItem('ultimoDia');
  if (ultimoDia !== hoje) {
    localStorage.setItem('ultimoDia', hoje);
    localStorage.setItem('coposHoje', '0');
    localStorage.removeItem('diasCarne');
    estado.coposhoje = 0;
    estado.diasCarne = [];
  }

  document.getElementById('copos-count').textContent = estado.coposhoje;

  // Iniciar timer
  tickHidratacao();
})();
