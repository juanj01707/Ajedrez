SIZE = 8

def print_board(board):
    for row in board:
        print(" ".join(row))

def find_valid_bishop_moves(board, arow, acol):
    print("Movimientos válidos para el alfil negro:")
    moves = []

    # Movimientos en diagonal superior izquierda
    i, j = arow - 1, acol - 1
    while i >= 0 and j >= 0:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i -= 1
        j -= 1

    # Movimientos en diagonal superior derecha
    i, j = arow - 1, acol + 1
    while i >= 0 and j < SIZE:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i -= 1
        j += 1

    # Movimientos en diagonal inferior izquierda
    i, j = arow + 1, acol - 1
    while i < SIZE and j >= 0:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i += 1
        j -= 1

    # Movimientos en diagonal inferior derecha
    i, j = arow + 1, acol + 1
    while i < SIZE and j < SIZE:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i += 1
        j += 1

    for move in moves:
        print(move)

def find_valid_king_moves(board, krow, kcol):
    print("Movimientos válidos para el rey negro:")
    moves = []

    # Movimientos verticales y horizontales
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_row = krow + direction[0]
        new_col = kcol + direction[1]
        if 0 <= new_row < SIZE and 0 <= new_col < SIZE and board[new_row][new_col] == '-':
            moves.append((new_row, new_col))

    # Movimientos en diagonales
    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    for direction in directions:
        new_row = krow + direction[0]
        new_col = kcol + direction[1]
        if 0 <= new_row < SIZE and 0 <= new_col < SIZE and board[new_row][new_col] == '-':
            moves.append((new_row, new_col))

    for move in moves:
        print(move)

def find_valid_rook_moves(board, trow, tcol):
    print("Movimientos válidos para la torre blanca:")
    moves = []

    # Movimientos horizontales a la derecha
    for c in range(tcol + 1, SIZE):
        if board[trow][c] == '-':
            moves.append((trow, c))
        else:
            break

    # Movimientos horizontales a la izquierda
    for c in range(tcol - 1, -1, -1):
        if board[trow][c] == '-':
            moves.append((trow, c))
        else:
            break

    # Movimientos verticales hacia abajo
    for r in range(trow + 1, SIZE):
        if board[r][tcol] == '-':
            moves.append((r, tcol))
        else:
            break

    # Movimientos verticales hacia arriba
    for r in range(trow - 1, -1, -1):
        if board[r][tcol] == '-':
            moves.append((r, tcol))
        else:
            break

    for move in moves:
        print(move)

def find_valid_queen_moves(board, qrow, qcol):
    print("Movimientos válidos para la reina blanca:")
    moves = []

    # Movimientos horizontales a la derecha
    for c in range(qcol + 1, SIZE):
        if board[qrow][c] == '-':
            moves.append((qrow, c))
        else:
            break

    # Movimientos horizontales a la izquierda
    for c in range(qcol - 1, -1, -1):
        if board[qrow][c] == '-':
            moves.append((qrow, c))
        else:
            break

    # Movimientos verticales hacia abajo
    for r in range(qrow + 1, SIZE):
        if board[r][qcol] == '-':
            moves.append((r, qcol))
        else:
            break

    # Movimientos verticales hacia arriba
    for r in range(qrow - 1, -1, -1):
        if board[r][qcol] == '-':
            moves.append((r, qcol))
        else:
            break

    # Movimientos diagonales superiores derechas
    i, j = qrow - 1, qcol + 1
    while i >= 0 and j < SIZE:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i -= 1
        j += 1

    # Movimientos diagonales superiores izquierdas
    i, j = qrow - 1, qcol - 1
    while i >= 0 and j >= 0:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i -= 1
        j -= 1

    # Movimientos diagonales inferiores derechas
    i, j = qrow + 1, qcol + 1
    while i < SIZE and j < SIZE:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i += 1
        j += 1

    # Movimientos diagonales inferiores izquierdas
    i, j = qrow + 1, qcol - 1
    while i < SIZE and j >= 0:
        if board[i][j] == '-':
            moves.append((i, j))
        else:
            break
        i += 1
        j -= 1

    for move in moves:
        print(move)

def find_valid_knight_moves(board, hrow, hcol):
    print("Movimientos válidos para el caballo blanco:")
    moves = []

    # Movimientos del caballo en forma de L
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for direction in directions:
        new_hrow = hrow + direction[0]
        new_hcol = hcol + direction[1]
        if 0 <= new_hrow < SIZE and 0 <= new_hcol < SIZE and board[new_hrow][new_hcol] == '-':
            moves.append((new_hrow, new_hcol))

    for move in moves:
        print(move)

def main():
    # Crear el tablero de ajedrez
    board = [['-' for _ in range(SIZE)] for _ in range(SIZE)]

    # Pedir al usuario las posiciones de las piezas
    arow, acol = map(int, input("Ingrese la posición del alfil negro (fila columna): ").split())
    board[arow][acol] = 'A'

    krow, kcol = map(int, input("Ingrese la posición del rey negro (fila columna): ").split())
    board[krow][kcol] = 'K'

    trow, tcol = map(int, input("Ingrese la posición de la torre blanca (fila columna): ").split())
    board[trow][tcol] = 'T'

    qrow, qcol = map(int, input("Ingrese la posición de la reina blanca (fila columna): ").split())
    board[qrow][qcol] = 'Q'

    hrow, hcol = map(int, input("Ingrese la posición del caballo blanco (fila columna): ").split())
    board[hrow][hcol] = 'H'

    # Imprimir el tablero con las piezas colocadas
    print("Tablero de ajedrez con las piezas colocadas:")
    print_board(board)

    # Encontrar movimientos válidos para el alfil negro
    find_valid_bishop_moves(board, arow, acol)

    # Encontrar movimientos válidos para el rey negro
    find_valid_king_moves(board, krow, kcol)

    # Encontrar movimientos válidos para la torre blanca
    find_valid_rook_moves(board, trow, tcol)

    # Encontrar movimientos válidos para la reina blanca
    find_valid_queen_moves(board, qrow, qcol)

     # Encontrar movimientos válidos para el caballo blanco
    find_valid_knight_moves(board, hrow, hcol)


# Llamar a la función main
main()