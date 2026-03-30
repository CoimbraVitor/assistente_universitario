import random
import re
from nltk.chat.util import Chat

from chatbot.intents import get_f1_intents
from chatbot.reflections import get_reflections


class F1Chatbot:

    def __init__(self):
        self.chat = Chat(get_f1_intents(), get_reflections())
        self.context = {}

        # 🔥 entidades conhecidas
        self.known_drivers = ["hamilton", "verstappen", "leclerc", "alonso"]
        self.known_topics = ["drs", "pit stop", "f1", "formula 1", "pneus"]

    # ---------------- EXTRAÇÃO DINÂMICA ----------------
    def extract_entities(self, text: str):
        entities = {}

        # pilotos
        for driver in self.known_drivers:
            if driver in text:
                entities["driver"] = driver

        # tópicos
        for topic in self.known_topics:
            if topic in text:
                entities["topic"] = topic

        return entities

    # ---------------- RESPOSTA ----------------
    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower()

        # 🔥 extrai automaticamente
        entities = self.extract_entities(user_input)

        # salva no contexto
        self.context.update(entities)

        # ---------------- FAVORITO DINÂMICO ----------------
        fav_match = re.search(r"meu piloto favorito é (.*)", user_input)
        if fav_match:
            driver = fav_match.group(1)
            self.context["favorite_driver"] = driver
            return f"{driver.title()} é uma ótima escolha! Vou lembrar disso 😄"

        # ---------------- USO DO CONTEXTO ----------------
        if "qual meu piloto favorito" in user_input:
            if "favorite_driver" in self.context:
                return f"Seu piloto favorito é {self.context['favorite_driver'].title()} 🏎️"
            return "Você ainda não me contou 😄"

        # ---------------- PERGUNTAS CONTEXTUAIS ----------------
        if user_input in ["por que", "por quê", "pq"]:
            if "driver" in self.context:
                return f"{self.context['driver'].title()} é muito talentoso e competitivo!"
            if "topic" in self.context:
                return f"{self.context['topic'].upper()} é importante na estratégia da corrida."
            return "Pode dar mais contexto? 😅"

        # ---------------- CONTINUAÇÃO ----------------
        if user_input in ["fala mais", "explica mais"]:
            if "topic" in self.context:
                return f"Posso te contar mais sobre {self.context['topic']}! Quer detalhes técnicos ou exemplos?"
            return "Sobre qual assunto você quer saber mais?"

        # ---------------- FALLBACK NLTK ----------------
        response = self.chat.respond(user_input)

        return response if response else random.choice([
            "Não entendi 😅",
            "Pode reformular?"
        ])