def get_bounds(grid, row, col_start, col_end):
    bounds = {
        "elements": "",
        "coords": [],
    }
    height = len(grid)
    width = len(grid[row])

    if col_start > 0:
        bounds["elements"] += grid[row][col_start - 1]
        bounds["coords"].append(f"{row},{col_start - 1}")
    # top left
    if row > 0 and col_start > 0:
        bounds["elements"] += grid[row - 1][col_start - 1]
        bounds["coords"].append(f"{row - 1},{col_start - 1}")
    # top
    if row > 0:
        bounds["elements"] += grid[row - 1][col_start : col_end + 1]
        bounds["coords"].extend(
            map(lambda col: f"{row - 1},{col}", range(col_start, col_end + 1))
        )
    # top right
    if row > 0 and col_end < width:
        bounds["elements"] += grid[row - 1][col_end + 1]
        bounds["coords"].append(f"{row - 1},{col_end + 1}")
    # right
    if col_end < width:
        bounds["elements"] += grid[row][col_end + 1]
        bounds["coords"].append(f"{row},{col_end + 1}")
    # bottom right
    if row < height - 1 and col_end < width:
        bounds["elements"] += grid[row + 1][col_end + 1]
        bounds["coords"].append(f"{row + 1},{col_end + 1}")
    # bottom
    if row < height - 1:
        bounds["elements"] += grid[row + 1][col_start : col_end + 1]
        bounds["coords"].extend(
            map(lambda col: f"{row + 1},{col}", range(col_start, col_end + 1))
        )
    # bottom left
    if row < height - 1 and col_start > 0:
        bounds["elements"] += grid[row + 1][col_start - 1]
        bounds["coords"].append(f"{row + 1},{col_start - 1}")

    return bounds
