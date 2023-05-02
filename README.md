# **Ajedrez**

el programa crea un tablero de ajedrez, coloca algunas piezas en el tablero y luego encuentra los movimientos válidos para esas piezas en el tablero.

## **-Estos son los pasos que sigue el algoritmo**

1. Se define una constante SIZE con un valor de 8, que representa el tamaño del tablero de ajedrez.

La función print_board recibe un parámetro board, que es una lista de listas que representa el tablero, e imprime el tablero en la consola. Cada elemento de la lista interior representa una celda del tablero.

La función find_valid_bishop_moves recibe como parámetros el tablero, la fila y la columna del alfil negro. Esta función busca los movimientos válidos para el alfil negro en las diagonales del tablero y los almacena en una lista llamada moves. Luego, imprime los movimientos válidos en la consola.

La función find_valid_king_moves recibe como parámetros el tablero, la fila y la columna del rey negro. Esta función busca los movimientos válidos para el rey negro en las direcciones vertical, horizontal y diagonal. Los movimientos válidos se almacenan en la lista moves y luego se imprimen en la consola.

La función find_valid_rook_moves recibe como parámetros el tablero, la fila y la columna de la torre blanca. Esta función busca los movimientos válidos para la torre blanca en las direcciones horizontal y vertical. Los movimientos válidos se almacenan en la lista moves y luego se imprimen en la consola.

La función find_valid_queen_moves recibe como parámetros el tablero, la fila y la columna de la reina blanca. Esta función busca los movimientos válidos para la reina blanca en las direcciones horizontal, vertical y diagonal. Los movimientos válidos se almacenan en la lista moves y luego se imprimen en la consola.

La función find_valid_knight_moves recibe como parámetros el tablero, la fila y la columna del caballo blanco. Esta función busca los movimientos válidos para el caballo blanco en forma de "L" en el tablero. Los movimientos válidos se almacenan en la lista moves y luego se imprimen en la consola.

La función main es la función principal del programa. Comienza creando un tablero de ajedrez representado por una lista de listas, donde cada elemento inicialmente es el carácter '-'.

Luego, solicita al usuario las posiciones de las piezas (alfil negro, rey negro, torre blanca, reina blanca y caballo blanco) y las almacena en las ubicaciones correspondientes en el tablero.

Imprime el tablero con las piezas colocadas.

Llama a las funciones find_valid_bishop_moves, find_valid_king_moves, find_valid_rook_moves, find_valid_queen_moves y find_valid_knight_moves pasando el tablero y las posiciones de las piezas correspondientes. Estas funciones encuentran los movimientos válidos para las piezas y los imprimen en la consola.
