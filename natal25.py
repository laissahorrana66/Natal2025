import random
import time

# Banco de dados de personagens e falas para simular conversas infinitas
DIAL_BANCO = {
    "Percy": {
        "saudacoes": ["E aí! Beleza?", "Pronto para o treino de esgrima?", "Oi! Estava procurando por você."],
        "conversas": [
            "O Sr. D me deu um castigo hoje. Quer me ajudar a colher morangos?",
            "Você prefere azul? Tudo fica melhor se for azul.",
            "Tava pensando... se a gente enfrentasse um Minotauro agora, quem correria primeiro?"
        ],
        "reacoes_alta": ["Cara, você é demais. Fico feliz que esteja no acampamento.", "Sabe, eu confio muito em você."],
        "reacoes_baixa": ["Cuidado para não virar comida de monstro com essa atitude.", "Tanto faz, vou falar com o Grover."]
    },
    "Annabeth": {
        "saudacoes": ["Olá. Já leu o manual do acampamento hoje?", "Oi, preciso de ajuda com um plano de batalha.", "Oi! Tudo bem?"],
        "conversas": [
            "Estou redesenhando a arquitetura do chalé de Atena. O que acha de colunas jônicas?",
            "Você acha que a estratégia é mais importante que a força bruta?",
            "Quíron está agindo de forma estranha hoje. Notou algo?"
        ],
        "reacoes_alta": ["Sua mente funciona de um jeito interessante. Gosto disso.", "Você tem potencial para ser um grande estrategista."],
        "reacoes_baixa": ["Sério? Vá ler um livro.", "Não tenho tempo para distrações agora."]
    },
    "Nico": {
        "saudacoes": ["...Oi.", "O que você quer?", "Não me irrite hoje."],
        "conversas": [
            "O Mundo Inferior está agitado. Fantasmas não calam a boca.",
            "Você tem medo do escuro? O escuro é a melhor parte.",
            "Se eu conjurar um esqueleto agora, você grita?"
        ],
        "reacoes_alta": ["Você... não é tão irritante quanto os outros.", "Obrigado por não se afastar de mim."],
        "reacoes_baixa": ["Volte para a luz do sol. Me deixe em paz.", "Não gaste meu tempo."]
    }
}

class JogoAmorDoceCHB:
    def __init__(self):
        self.nome_jogador = ""
        self.pai_olimpo = ""
        self.afinidade = {"Percy": 50, "Annabeth": 50, "Nico": 50}
        self.jogando = True

    def iniciar_jogo(self):
        print("⚡ BEM-VINDO AO ACAMPAMENTO MEIO-SANGUE: AMOR & DEUSES ⚡\n")
        self.nome_jogador = input("Qual é o seu nome, semideus(a)? ").strip()
        print(f"\nPrazer, {self.nome_jogador}! Escolha seu parentesco divino:")
        print("[1] Afrodite (Charme e Beleza)")
        print("[2] Ares (Força e Coragem)")
        print("[3] Hermes (Astúcia e Velocidade)")
        
        escolha = input("Digite o número do seu pai/mãe olimpiano: ")
        if escolha == "1": self.pai_olimpo = "Afrodite"
        elif escolha == "2": self.pai_olimpo = "Ares"
        else: self.pai_olimpo = "Hermes"
        
        print(f"\nAnúncio no Refeitório: {self.nome_jogador}, filho(a) de {self.pai_olimpo} foi determinado(a)!")
        time.sleep(1.5)
        self.menu_principal()

    def menu_principal(self):
        while self.jogando:
            print("\n" + "="*40)
            print(f"📍 MAPA DO ACAMPAMENTO | Chalé de {self.pai_olimpo}")
            print("="*40)
            print("Com quem você quer interagir agora?")
            print("[1] Ir para o Lago de Canoagem (Falar com Percy)")
            print("[2] Ir para a Biblioteca do Chalé 6 (Falar com Annabeth)")
            print("[3] Ir para a Floresta do Acampamento (Falar com Nico)")
            print("[4] Ver Status de Afinidade (Loveômetro)")
            print("[5] Sair do Jogo")
            
            opcao = input("Escolha uma rota/ação: ").strip()
            
            if opcao == "1": self.conversar_com("Percy")
            elif opcao == "2": self.conversar_com("Annabeth")
            elif opcao == "3": self.conversar_com("Nico")
            elif opcao == "4": self.mostrar_loveometro()
            elif opcao == "5": 
                print("\nAté logo! Seus sentimentos pelos semideuses foram salvos no Olimpo.")
                self.jogando = False
            else:
                print("Opção inválida! Os monstros te pegaram no caminho.")

    def conversar_com(self, personagem):
        print(f"\n👣 Você caminha até o encontro de {personagem}...")
        time.sleep(1)
        
        # Saudação inicial baseada no banco
        saudacao = random.choice(DIAL_BANCO[personagem]["saudacoes"])
        print(f"\n💬 [{personagem}]: \"{saudacao}\"")
        
        # Loop de conversa infinita com o personagem escolhido
        while True:
            pergunta = random.choice(DIAL_BANCO[personagem]["conversas"])
            print(f"\n💬 [{personagem}]: \"{pergunta}\"")
            print("\nComo você vai responder?")
            print("[1] Responder de forma Gentil/Romântica")
            print("[2] Responder de forma Irônica/Provocativa")
            print("[3] Responder de forma Neutra/Desinteressada")
            print("[4] Mudar de lugar (Voltar ao menu)")
            
            resposta = input("Sua escolha: ").strip()
            
            if resposta == "4":
                print(f"Você se despede de {personagem} por enquanto.")
                break
                
            # Lógica do Loveômetro (Amor Doce)
            if resposta == "1":
                self.afinidade[personagem] += 10
                print(f"\n💖 +10 de afinidade! {personagem} gostou da resposta.")
                if self.afinidade[personagem] >= 80:
                    print(f"🥰 [{personagem}]: \"{random.choice(DIAL_BANCO[personagem]['reacoes_alta'])}\"")
            elif resposta == "2":
                self.afinidade[personagem] -= 10
                print(f"\n💔 -10 de afinidade! {personagem} achou você difícil.")
                if self.afinidade[personagem] <= 30:
                    print(f"😒 [{personagem}]: \"{random.choice(DIAL_BANCO[personagem]['reacoes_baixa'])}\"")
            elif resposta == "3":
                print(f"\n😐 Afinidade inalterada. A conversa ficou morna.")
            else:
                print("Opção inválida. Você gaguejou e ficou um silêncio constrangedor.")
            
            # Limita a afinidade entre 0 e 100
            self.afinidade[personagem] = max(0, min(100, self.afinidade[personagem]))
            time.sleep(1)

    def mostrar_loveometro(self):
        print("\n📊 === LOVEÔMETRO (STATUS DE AFINIDADE) ===")
        for personagem, pontos in self.afinidade.items():
            barra = "♥" * (pontos // 10) + "♡" * ((100 - pontos) // 10)
            status = "Melhores Amigos/Crush" if pontos >= 80 else ("Neutro" if pontos >= 40 else "Rivalidade")
            print(f"{personagem:10}: [{barra}] {pontos} pts ({status})")
        time.sleep(2)

# Executar o jogo
if __name__ == "__main__":
    jogo = JogoAmorDoceCHB()
    jogo.iniciar_jogo()
