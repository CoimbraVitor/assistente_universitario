def get_f1_intents():
    return [

        # ---------------- MENU ----------------
        [r"(?i)oi|olá|ola|menu|iniciar",
         ["Olá! 👋\n\nO que você quer saber?\n\n"
          "1 - O que é Fórmula 1?\n"
          "2 - O que é DRS?\n"
          "3 - O que é Pit Stop?\n"
          "4 - Quem é Lewis Hamilton?\n"
          "5 - Quem é Max Verstappen?\n\n"
          "Ou pode falar livremente comigo 😄"]],

        # ---------------- CONCEITOS ----------------
        [r"(?i)\b1\b|o que é formula 1|o que é f1",
         ["A Fórmula 1 é a principal categoria do automobilismo mundial."]],

        [r"(?i)\b2\b|o que é drs",
         ["DRS é um sistema que reduz o arrasto para facilitar ultrapassagens."]],

        [r"(?i)\b3\b|o que é pit stop",
         ["Pit stop é a parada para troca de pneus e ajustes no carro."]],

        [r"(?i)o que é safety car",
         ["Safety car é usado para reduzir a velocidade da corrida em situações perigosas."]],

        [r"(?i)o que é classificação|qualifying",
         ["Classificação define o grid de largada da corrida."]],

        # ---------------- PILOTOS ----------------
        [r"(?i)\b4\b|quem é lewis hamilton",
         ["Lewis Hamilton é um piloto britânico, heptacampeão mundial."]],

        [r"(?i)\b5\b|quem é max verstappen",
         ["Max Verstappen é um piloto campeão mundial conhecido por sua agressividade."]],

        [r"(?i)quem é (.*)",
         ["%1 é um nome importante na Fórmula 1! Quer saber algo específico sobre ele?"]],

        # ---------------- EQUIPES ----------------
        [r"(?i)equipe favorita|times da f1|equipes",
         ["Algumas equipes são Ferrari, Red Bull, Mercedes, McLaren e Aston Martin."]],

        # ---------------- PNEUS ----------------
        [r"(?i)pneus|tipos de pneus",
         ["Na F1 existem pneus macios, médios e duros, cada um com características diferentes."]],

        # ---------------- BANDEIRAS ----------------
        [r"(?i)bandeira amarela",
         ["Bandeira amarela indica perigo na pista, é proibido ultrapassar."]],

        [r"(?i)bandeira vermelha",
         ["Bandeira vermelha interrompe a corrida imediatamente."]],

        # ---------------- CONVERSACIONAL ----------------
        [r"(?i)eu gosto de (.*)",
         ["Legal! Por que você gosta de %1?",
          "O que te chama atenção em %1?"]],

        [r"(?i)eu não gosto de (.*)",
         ["Entendi... por que você não gosta de %1?"]],

        [r"(?i)eu acho que (.*)",
         ["Interessante você achar que %1. Pode explicar melhor?"]],

        [r"(?i)meu piloto favorito é (.*)",
         ["%1 é um grande piloto! Boa escolha 😄"]],

        [r"(?i)o que você acha de (.*)",
         ["%1 é um assunto muito interessante na Fórmula 1!"]],

        # ---------------- INTERAÇÃO ----------------
        [r"(?i)como você está",
         ["Estou ótimo! Sempre pronto pra falar de F1 🏎️"]],

        [r"(?i)qual seu nome",
         ["Sou um chatbot especialista em Fórmula 1 😄"]],

        # ---------------- FALLBACK ----------------
        [r"(?i)(.*)",
         ["Não entendi muito bem 🤔\n\n"
          "Tente perguntar sobre:\n"
          "- DRS\n- Pilotos\n- Equipes\n- Ou digite 1 a 5 😊"]]
    ]