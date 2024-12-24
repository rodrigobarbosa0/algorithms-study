
import time



def contagem_regressiva(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1

    print("Tempo esgotado!")

# Exemplo de uso
contagem_regressiva(10)  # Contagem regressiva de 10 segundos
