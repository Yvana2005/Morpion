
import tkinter



def print_winner():
    global win
    if win is False:
        win = True
        print("le joueur ", current_player, "a gagner le jeu!")

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def check_win(clicked_row, clicked_col):
    #detecter victoire horizontal
    count = 0
    for y in range(3):
        current_button = buttons[y][clicked_row]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
    #detecter verticalement
    count = 0
    for y in range(3):
        current_button = buttons[clicked_col][y]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()
    # detecter la victoire en diagonale
    count = 0
    for y in range(3):
        current_button = buttons[y][y]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # detecter la victoire en diagonale inverser
    count = 0
    for y in range(3):
        current_button = buttons[2-y][y]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
            print_winner()
    if win is False:
        count = 0
        for col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == 'X' or current_button['text'] == 'O':
                    count += 1
        if count == 9:
            print("Match Null")

def place_symbol(i, j):

    clicked_button = buttons[j][i]
    if clicked_button['text'] == "":
       clicked_button.config(text=current_player)

       check_win(i,j)
       switch_player()

def draw_grid():
    for j in range (3):
       buttons_in_cols = []
       for i in range (3):
          button = tkinter.Button(
              root, font=("Arial", 50),
              width=5, height=3,
              command=lambda r=i, c=j: place_symbol(r, c),
          )
          button.grid(row=i, column=j)
          buttons_in_cols.append(button)
       buttons.append(buttons_in_cols)

#stockage
buttons = []
current_player = 'X'
win = False
# buttons[1][1]

#Creer la fenetre
root = tkinter.Tk()
#Personaliser cette fenetre
root.title("JEU DU MORPION")
root.minsize(500, 500)
root.config(background='#4065A4')

draw_grid()
root.mainloop()