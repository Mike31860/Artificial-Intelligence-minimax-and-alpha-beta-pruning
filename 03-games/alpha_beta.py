
def is_game_over(node):
    winning_indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for indexes in winning_indexes:
        hit_count = 0
        chosen_symbol = node[indexes[0]]

        for index in indexes:
            if node[index] is not None and node[index] == chosen_symbol:
                hit_count = hit_count + 1

        if hit_count == 3:
            return True, chosen_symbol

    if node.count(None) == 0:
        return True, None

    return False, None

def generate_children(node, chosen_symbol): # TODO: Create a function to generate the children states for minimax evaluation
    #generatethe
    generarHijos = []

    for indexHijos in range(len(node)):

        if node[indexHijos] == None or node[indexHijos] == -1:
            hijoGenerado = node.copy()
            hijoGenerado[indexHijos] = chosen_symbol
            generarHijos.append(hijoGenerado)
    return generarHijos

def alternate_symbol(symbol):
    return 'o' if symbol == 'x' else 'x'

def mini_max_ab(node, is_maximizing_player_turn, chosen_symbol, alpha, beta): # TODO: Modify this minimax in order to turn it into an alpha-beta pruning version with depth cutting
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    childrens = generate_children(node, chosen_symbol)

    if is_maximizing_player_turn:
        PUNTUACION = -9999
        unHijo = []

        for hijo in childrens:
            hijo2 = mini_max_ab(hijo, not is_maximizing_player_turn, alternate_symbol(chosen_symbol), alpha, beta)
            if PUNTUACION < hijo2[0]:
                unHijo = hijo

            PUNTUACION = max(PUNTUACION, hijo2[0])
            alpha = max(alpha, hijo2[0])
            if beta <= alpha:
                break

        return PUNTUACION, unHijo


    else:

        PUNTUACIONBAJA = 9999
        unHijo = []

        for hijo in childrens:
            hijo2 = mini_max_ab(hijo, not is_maximizing_player_turn, alternate_symbol(chosen_symbol), alpha, beta)
            if PUNTUACIONBAJA > hijo2[0]:
                unHijo = hijo

            PUNTUACIONBAJA = min(PUNTUACIONBAJA, hijo2[0])
            beta = min(beta, hijo2[0])
            if beta <= alpha:
               break

        return PUNTUACIONBAJA, unHijo



def mini_max(node, is_maximizing_player_turn, chosen_symbol):
    game_result = is_game_over(node)

    if game_result[0]:
        if game_result[1] is None:
            return 0, node

        return (-1, node) if is_maximizing_player_turn else (1, node)

    children = generate_children(node, chosen_symbol)
    children_results = list(map(
        lambda child: [
            mini_max(child, not is_maximizing_player_turn, alternate_symbol(chosen_symbol))[0],
            child
        ],
        children
    ))

    return max(children_results, key=str) if is_maximizing_player_turn else min(children_results, key=str)
