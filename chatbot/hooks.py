def get_f1_hooks():
    """
    Returns a dictionary of conversational hooks grouped by phase.
    Each hook is a question or statement designed to lead the user to the next topic.
    """
    return {
        "WELCOME": [
            "Você acompanha a F1 há muito tempo ou está começando agora? 🏎️",
            "Qual o seu nível de conhecimento sobre as corridas? Gosta de detalhes técnicos ou mais da emoção?",
            "Antes de começarmos, você já tem uma equipe favorita ou está 'neutro' nesta temporada? 😄"
        ],
        "BASICS": [
            "Sabia que a F1 começou oficialmente em 1950? É muita história! Quer saber qual foi a primeira corrida?",
            "A categoria é considerada o auge do automobilismo. Você sabe o que diferencia um carro de F1 de um carro comum, além da velocidade?",
            "Falando em equipes, você conhece a história da Ferrari? Eles são a equipe mais antiga do grid! 🐎"
        ],
        "TECH": [
            "Já ouviu falar do DRS? É aquele sistema de asa móvel que ajuda nas ultrapassagens. Quer que eu te explique como funciona?",
            "Os carros são verdadeiros aviões de cabeça para baixo por causa da aerodinâmica. Você se interessa por essa parte técnica?",
            "Sabia que o volante de um F1 tem mais de 20 botões? É quase um videogame! Quer saber o que eles controlam?"
        ],
        "STRATEGY": [
            "Uma corrida não se ganha só na pista, mas também nos boxes. Você sabe quanto tempo dura um pit stop perfeito hoje em dia? ⏱️",
            "Existem diferentes tipos de pneus: macios, médios e duros. Você entende como as equipes decidem qual usar?",
            "Já viu as bandeiras coloridas durante a corrida? Sabe o que a bandeira quadriculada preta e branca (não a do final) significa?"
        ],
        "DRIVERS": [
            "Entre os pilotos atuais, quem você acha que tem mais talento: Hamilton ou Verstappen? ⚔️",
            "O Brasil tem uma história incrível na F1. Você conhece as conquistas do Ayrton Senna?",
            "Sabia que ser piloto de F1 exige um preparo físico de triatleta? O pescoço deles sofre muito nas curvas!"
        ],
        "CLOSING": [
            "Nossa, falamos de muita coisa hoje! O que você mais gosta de ver em um final de semana de GP?",
            "Acha que a F1 está ficando mais emocionante com as novas regras?",
            "Foi um prazer conversar sobre F1 com você! Tem algum outro detalhe que queira explorar antes de encerrarmos? 😊"
        ]
    }
