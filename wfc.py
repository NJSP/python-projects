import random
import heapq

def wave_function_collapse(grid_size, patterns, weights):
    width, height = grid_size
    # Initialize the grid with None values
    grid = [[None for _ in range(width)] for _ in range(height)]

    # Convert lists within patterns to tuples for hashability
    pattern_tuples = [{k: tuple(v) for k, v in p.items()} for p in patterns]

    def get_possible_patterns(x, y):
        # Start with all patterns as possible
        possible_patterns = set(tuple(sorted(p.items())) for p in pattern_tuples)
        # Check the left neighbor
        if x > 0:
            left_pattern = grid[y][x-1]
            if left_pattern is not None:
                left_pattern_dict = dict(left_pattern)
                possible_patterns &= set(tuple(sorted(p.items())) for p in pattern_tuples if p['right'] == left_pattern_dict['right'])
        # Check the top neighbor
        if y > 0:
            top_pattern = grid[y-1][x]
            if top_pattern is not None:
                top_pattern_dict = dict(top_pattern)
                possible_patterns &= set(tuple(sorted(p.items())) for p in pattern_tuples if p['bottom'] == top_pattern_dict['bottom'])
        return list(possible_patterns)

    def collapse():
        min_entropy = float('inf')
        min_entropy_coords = None

        # Find the cell with the minimum entropy (least number of possible patterns)
        for y in range(height):
            for x in range(width):
                if grid[y][x] is None:
                    possible_patterns = get_possible_patterns(x, y)
                    entropy = len(possible_patterns)
                    if entropy < min_entropy:
                        min_entropy = entropy
                        min_entropy_coords = (x, y)

        if min_entropy_coords is None:
            return False  # No more cells to collapse

        x, y = min_entropy_coords
        possible_patterns = get_possible_patterns(x, y)
        # Randomly choose one of the possible patterns, weighted by their likelihood
        chosen_pattern = random.choices(possible_patterns, weights=[weights[patterns.index({k: list(v) for k, v in dict(p).items()})] for p in possible_patterns])[0]
        grid[y][x] = chosen_pattern
        return True

    # Continue collapsing until no more cells can be collapsed
    while collapse():
        pass

    # Convert the grid back to dictionaries for the final output
    return [[dict(pattern) if pattern is not None else None for pattern in row] for row in grid]

def a_star_search(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            data.append(start)
            return data[::-1]  # Return reversed path

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1

            if 0 <= neighbor[0] < len(grid):
                if 0 <= neighbor[1] < len(grid[0]):
                    if grid[neighbor[0]][neighbor[1]] is None:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

def generate_map_and_path(grid_size, patterns, terrain_types, weights, start, goal):
    # Generate the map
    generated_map = wave_function_collapse(grid_size, patterns, weights)
    
    # Print the generated map with terrain types
    print("\nGenerated map:")
    for row in generated_map:
        row_output = []
        for pattern in row:
            if pattern is not None:
                # Find the index of the pattern in the original patterns list
                pattern_index = patterns.index({k: list(v) for k, v in pattern.items()})
                terrain_type = terrain_types[pattern_index]
                row_output.append(f"{terrain_type} ({pattern})")
            else:
                row_output.append("None")
        print(" | ".join(row_output))
    
    # Find the path using A* algorithm
    path = a_star_search(generated_map, start, goal)
    
    # Print the path
    print("\nPath from start to goal:")
    print(path)
    
    return generated_map, path

# Example usage:
patterns = [
    {'right': [2, 1], 'bottom': [2, 2]},  # Swamp
    {'right': [1, 2], 'bottom': [1, 1]},  # Beach
    {'right': [2, 2], 'bottom': [2, 1]},  # Cliff
    {'right': [1, 1], 'bottom': [1, 2]}   # Meadow
]

terrain_types = ["Swamp", "Beach", "Cliff", "Meadow"]
weights = [0.1, 0.2, 0.3, 0.4]  # Different weights for each pattern

grid_size = (5, 5)
start = (0, 0)
goal = (4, 4)

# Generate map and path
generate_map_and_path(grid_size, patterns, terrain_types, weights, start, goal)

# Another example usage:
patterns = [
    {'right': [1, 1], 'bottom': [1, 2]},  # Meadow
    {'right': [2, 2], 'bottom': [2, 1]},  # Cliff
    {'right': [1, 2], 'bottom': [1, 1]},  # Beach
    {'right': [2, 1], 'bottom': [2, 2]}   # Swamp
]

terrain_types = ["Meadow", "Cliff", "Beach", "Swamp"]
weights = [0.4, 0.3, 0.2, 0.1]  # Different weights for each pattern

grid_size = (6, 6)
start = (0, 0)
goal = (5, 5)

# Generate map and path
generate_map_and_path(grid_size, patterns, terrain_types, weights, start, goal)

# Another example usage:
patterns = [
    {'right': [1, 2], 'bottom': [1, 1]},  # Beach
    {'right': [2, 1], 'bottom': [2, 2]},  # Swamp
    {'right': [1, 1], 'bottom': [1, 2]},  # Meadow
    {'right': [2, 2], 'bottom': [2, 1]}   # Cliff
]

terrain_types = ["Beach", "Swamp", "Meadow", "Cliff"]
weights = [0.2, 0.1, 0.4, 0.3]  # Different weights for each pattern

grid_size = (4, 4)
start = (0, 0)
goal = (3, 3)

# Generate map and path
generate_map_and_path(grid_size, patterns, terrain_types, weights, start, goal)