import pyautogui
from tkinter import messagebox
from pynput import keyboard

# Obtém as dimensões da tela
screen_width, screen_height = pyautogui.size()

# Obtém as coordenadas iniciais do mouse
x = screen_width // 2
y = screen_height // 2

# Define o deslocamento do mouse
offset = 10
messagebox.showinfo('Ausência em Home Office', 'Pressione OK para iniciar a sua ausência, depois de iniciada pressione qualquer tecla para finalizar.')

# Flag para controlar a execução do script
is_running = True
# Função para lidar com o pressionamento de tecla
def on_press(key):
    global is_running
    is_running = False
    return False

# Cria um listener para monitorar o pressionamento de teclas
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Move o mouse continuamente até que uma tecla seja pressionada
while is_running:
    # Move o mouse para a direita
    pyautogui.moveTo(x + offset, y, duration=0.25)
    pyautogui.click(x, y)
    # Move o mouse para baixo
    pyautogui.moveTo(x, y + offset, duration=0.25)
    pyautogui.click(x, y)
    # Move o mouse para a esquerda
    pyautogui.moveTo(x - offset, y, duration=0.25)
    pyautogui.click(x, y)
    # Move o mouse para cima
    pyautogui.moveTo(x, y - offset, duration=0.25)
    pyautogui.click(x, y)
    
# Esperar 5 segundos antes de encerrar completamente o programa
messagebox.showinfo('Fim da Ausência', 'Volte a trabalhar, seu morcego! 🦇')
