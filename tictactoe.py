import sys
import time
from random import randrange
import random
import copy

def coin_flip():
    # Esta función ingresa al loop del juego en si, "tira una moneda al aire" y dependiendo de 
    # quién gane realiza el primer movimiento, luego del cual el programa no se detendrá hasta que alguien gane. 
    player_choice = input("Elija CARA o CECA: ")
    player_choice = player_choice.lower()
    if player_choice == "cara" or player_choice == "ceca":
        flip = random.random()
        if flip <= 0.5:
            flip = "cara"
        else:
            flip = "ceca"
        print("La moneda cayó en ", flip)
        
        if player_choice == flip:
            print('El Jugador arrancará la partida')
            time.sleep(1)
            enter_move(current_board)            
        else:
            print('La PC arrancará la partida')
            time.sleep(1)
            draw_move_minmax()
    else:
        print("Escriba nuevamente su elección")
        coin_flip()

def display_board(board):
    # La función acepta una lista de la cual obtiene el estado actual del tablero
    # y lo muestra en la consola.
    for row in board:
        print("+-----+-----+-----+")
        print("|     |     |     |")
        for elem in row:
            print("| ", end=" ")
            print(elem, end="  ") # Esta sección es la que muestra los datos del tablero
        print("|")
        print( "|     |     |     |")
    print("+-----+-----+-----+")
        
def enter_move(board):
    # La función toma el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica si el movimiento es posible y actualiza el tablero acorde a la decisión del usuario.
    # Printea diversos mensajes si el input no se condice con un movimiento posible. 
    while True:
        try:
            mov_jugador = int(input('Elija un casillero: '))
            break
        except ValueError:
            print('Ingrese un casillero del 1 al 9 que esté vacío. Sin letras u otros caracteres')
            continue
    # Este tipo de código chequea que el tipo del input sea correcto y vuelve a pedir inputs hasta obtener
    # uno que sea válido

    if mov_jugador <= 9 and mov_jugador > 0:
    # Este if chequea que el entero inputeado esté en el rango adecuado
        
        row = (mov_jugador - 1) // 3
        if mov_jugador <= 3:
            column = mov_jugador - 1
        elif mov_jugador > 3 and mov_jugador <= 6:
            column = mov_jugador - 4
        else:
            column = mov_jugador - 7
        coord = (row, column)
        # Esta sección de código tradujo el input a coordenadas

        if coord not in free_fields:
            print("Ese casillero está ocupado.")
            enter_move(board)
        else:
            global current_board
            current_board[row][column] = "O"
            display_board(current_board)
            victory_for(current_board, "O")
            make_list_of_free_fields(current_board)
            time.sleep(2)
            draw_move_minmax()
            
    else:
        print("Elija un casillero del 1 al 9.")
        enter_move(board)

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    global free_fields
    free_fields = []
    for row in range(len(board)):
        for column in range(3):
            if isinstance((board[row][column]), int):
                free_fields.append((row, column))
    return free_fields

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    coords = []
    elems = []
    for row in range(len(board)):
        for column in range(3):
            coords.append((row, column))
    for row in board:
        for elem in row:
            elems.append(elem)
    # Esta seccion obtiene los datos del tablero actual y las ordena en listas

    current_state = {}
    for i in range(9):
        current_state[coords[i]] = elems[i]

    row1 = [elems[0], elems[1], elems[2]]
    row2 = [elems[3], elems[4], elems[5]]
    row3 = [elems[6], elems[7], elems[8]]
    col1 = [elems[0], elems[3], elems[6]]
    col2 = [elems[1], elems[4], elems[7]]
    col3 = [elems[2], elems[5], elems[8]]
    diag1 = [elems[0], elems[4], elems[8]]
    diag2 = [elems[2], elems[4], elems[6]]
    if (row1 == [sign, sign, sign] or row2 == [sign, sign, sign] or row3 == [sign, sign, sign] or col1 == [sign, sign, sign] or col2 ==[sign, sign, sign] or col3 ==[sign, sign, sign] or
         diag1 == [sign, sign, sign] or diag2 == [sign, sign, sign]):
        print("La partida ha terminado!")
        time.sleep(3)
        sys.exit()
    elif all(type(x) == type(elems[0]) for x in elems):
        print("Empate!")
        time.sleep(3)
        sys.exit()

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero, eligiendo al azar un espacio.
    row = randrange(3)
    column = randrange(3)
    coord_maquina = (row, column)
    if coord_maquina not in free_fields:
            draw_move(board)
    else:
            global current_board
            current_board[row][column] = "X"
            display_board(current_board)
            victory_for(current_board, "X")
            make_list_of_free_fields(current_board)
            enter_move(current_board)

def victory_check(board, sign):
    # La función analiza el estatus del tablero para verificar solamente si se ha ganado el juego.
    # A diferencia de la anterior función, devuelve True or False y True solamente ante una victoria
    coords = []
    elems = []
    for row in range(len(board)):
        for column in range(3):
            coords.append((row, column))
    for row in board:
        for elem in row:
            elems.append(elem)

    current_state = {}
    for i in range(9):
        current_state[coords[i]] = elems[i]

    row1 = [elems[0], elems[1], elems[2]]
    row2 = [elems[3], elems[4], elems[5]]
    row3 = [elems[6], elems[7], elems[8]]
    col1 = [elems[0], elems[3], elems[6]]
    col2 = [elems[1], elems[4], elems[7]]
    col3 = [elems[2], elems[5], elems[8]]
    diag1 = [elems[0], elems[4], elems[8]]
    diag2 = [elems[2], elems[4], elems[6]]
    if (row1 == [sign, sign, sign] or row2 == [sign, sign, sign] or row3 == [sign, sign, sign] or col1 == [sign, sign, sign] or col2 ==[sign, sign, sign] or col3 ==[sign, sign, sign] or
         diag1 == [sign, sign, sign] or diag2 == [sign, sign, sign]):
        return True
    elif all(type(x) == type(elems[0]) for x in elems):
        return False
    else:
        return False 

def draw_move_minmax():
    i = 0 # Numero de iteraciones, reservo memoria para llevar una cuenta de las casillas vacías iterados
    # La función dibuja el movimiento de la máquina y actualiza el tablero, usando un algoritmo para elegir un espacio.
    for free_space in free_fields:
        i += 1
        #vc = 0 # "victory constant" reservo memoria para la variable que determina si se llego a victoria o derrota/reseteo la misma
        #mc = 0 # "move counter" reservo memoria para la variable que cuenta los pasos/reseteo la misma

        #print(free_space[0], "-", free_space[1], "//", vc, "--", mc)

        internal_board_ai = copy.deepcopy(current_board)
        internal_board_ai[free_space[0]][free_space[1]] = "X"

        internal_board_human = copy.deepcopy(current_board)
        internal_board_human[free_space[0]][free_space[1]] = "O"

        if victory_check(internal_board_human, "O") is True:
            current_board[free_space[0]][free_space[1]] = "X"
            display_board(current_board)
            victory_for(current_board, "X")
            enter_move(current_board)
            break
        elif victory_check(internal_board_ai, "X") is True:
            current_board[free_space[0]][free_space[1]] = "X"
            display_board(current_board)
            victory_for(current_board, "X")
            break
            # Esta parte del codigo hace mate ni bien detecta una victoria posible en el próximo movimiento o tapa al humano
        elif i == len(free_fields) and victory_check(internal_board_ai, "X") is False:
            draw_move(current_board)
            break
        else:
            continue

current_board = [[1,2,3], [4,5,6], [7,8,9]]
# Estado inicial, nuestra función draw debe tomarlo como input y generar el tablero

display_board(current_board)
free_fields = make_list_of_free_fields(current_board)

coin_flip()
# Llamar a esta función inicia el juego