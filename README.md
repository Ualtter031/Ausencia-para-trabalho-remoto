# Ausência em Home Office

Este script Python simula movimentos contínuos do mouse na tela para evitar que o computador entre em estado de inatividade enquanto você está ausente e mantém o status ativo no MS Teams. É útil quando você está em home office e deseja manter seu status ativo.

## 🚀 Como funciona
O script move o cursor do mouse em um pequeno quadrado repetidamente, clicando levemente em cada ponto para garantir atividade contínua. A execução do script é interrompida quando qualquer tecla é pressionada.

## 📋 Pré-requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `pyautogui`
  - `pynput`
  - `tkinter` (parte da biblioteca padrão do Python)

Você pode instalar as dependências com o comando:
```
pip install pyautogui pynput
```

## 📌 Uso

1. Salve o código Python em um arquivo chamado `ausencia_home_office.py`.
2. Execute o script com:
```
python ausencia_home_office.py
```

3. Uma mensagem pop-up aparecerá com o título **"Ausência em Home Office"** e uma mensagem indicando que você deve pressionar **OK** para iniciar a simulação de ausência.
4. Para parar o script, pressione qualquer tecla.
5. Uma mensagem pop-up final será exibida indicando que o script foi interrompido.

## 📄 Código Python
```python
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
```

## 🔑 Como funciona o script

- **Movimentação do Mouse:** O cursor se move continuamente em um quadrado pequeno (direita, baixo, esquerda, cima).
- **Interrupção:** Ao pressionar qualquer tecla, o script para e exibe uma mensagem final.

## 💡 Observações
- Este script é apenas para fins educacionais. Use-o com responsabilidade.

## 📜 Licença
Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

