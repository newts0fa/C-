def a_star_algorithm(draw, grid, start, end, weighted=False):
    """
    Реализация алгоритма A* с визуализацией
    :param draw: функция отрисовки
    :param grid: сетка ячеек
    :param start: начальная точка
    :param end: конечная точка
    :param weighted: учитывать веса ячеек
    :return: True если путь найден, иначе False
    """
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    
    # Инициализация g_score и f_score
    g_score = {cell: float("inf") for row in grid for cell in row}
    g_score[start] = 0
    f_score = {cell: float("inf") for row in grid for cell in row}
    f_score[start] = heuristic(start.get_pos(), end.get_pos())
    
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            # Расчет стоимости с учетом веса
            weight = neighbor.weight if weighted else 1
            temp_g_score = g_score[current] + weight

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw()

        if current != start:
            current.make_closed()

    return False
