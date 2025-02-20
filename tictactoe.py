import sys
import time
def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for row in board:
        print("+-----+-----+-----+")
        print("|     |     |     |")
        for elem in row:
            print("| ", end=" ")
            print(elem, end="  ") #esta sección es la que interpreta los datos
        print("|")
        print( "|     |     |     |")
    print("+-----+-----+-----+")
        
def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    mov_jugador = int(input("Ingresa tu movimiento: "))
    if mov_jugador <= 9 and mov_jugador > 0:
    #este if chequea que el input sea adecuado
        
        row = (mov_jugador - 1) // 3
        if mov_jugador <= 3:
            column = mov_jugador - 1
        elif mov_jugador > 3 and mov_jugador <= 6:
            column = mov_jugador - 4
        else:
            column = mov_jugador - 7
        coord = (row, column)
        #esta sección de código tradujo el input a coordenadas

        if coord not in free_fields:
            print("Este movimiento no es válido.")
            enter_move(board)
        else:
            global current_board
            current_board[row][column] = "O"
            display_board(current_board)
            victory_for(current_board, "O")
            make_list_of_free_fields(current_board)
            draw_move(current_board)
            
    else:
        print("Este movimiento no es válido.")
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
    #print(elems)
    #esta seccion obtiene los datos del tablero

    current_state = {}
    for i in range(9):
        current_state[coords[i]] = elems[i]
    #print(current_state)
    #esta sección crea un diccionario con la data obtenida

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
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    from random import randrange
    row = randrange(3)
    column = randrange(3)
    coord_maquina = (row, column)
    #print(coord_maquina)
    if coord_maquina not in free_fields:
            draw_move(board)
    else:
            global current_board
            current_board[row][column] = "X"
            display_board(current_board)
            victory_for(current_board, "X")
            make_list_of_free_fields(current_board)
            enter_move(current_board)

    
    
current_board = [[1,2,3], [4,"X",6], [7,8,9]]
# Estado inicial, nuestra función draw debe tomarlo como input y generar el tablero
display_board(current_board)
free_fields = make_list_of_free_fields(current_board)
enter_move(current_board)
