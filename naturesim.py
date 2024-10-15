import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 30
CELL_SIZE = 20
SCREEN_SIZE = GRID_SIZE * CELL_SIZE
FPS = 2  # Slower FPS for easier visualization

# Colors
COLORS = {
    'Grassland': (34, 139, 34),
    'Forest': (0, 100, 0),
    'Desert': (210, 180, 140),
    'Water': (0, 0, 255),
    'Mountain': (139, 137, 137),
    'Herbivore': (0, 255, 0),
    'Carnivore': (255, 0, 0),
    'Omnivore': (0, 0, 255),
    'Plant': (0, 255, 0),
    'Night': (0, 0, 0)
}

# Terrain types with probabilities
TERRAINS = {
    'Grassland': 0.3,
    'Forest': 0.2,
    'Desert': 0.2,
    'Water': 0.1,
    'Mountain': 0.2
}

# Weather types
WEATHERS = ['Sunny', 'Rainy', 'Snowy']

# Adjust screen size to fit the full legend
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 200))  # Increased extra space for text and legend
pygame.display.set_caption("Nature Simulation")

# Font for text
font = pygame.font.SysFont(None, 24)

# Clock
clock = pygame.time.Clock()

def generate_grid():
    """Generate the grid based on predefined probabilities."""
    terrain_choices = list(TERRAINS.keys())
    terrain_weights = list(TERRAINS.values())
    return [[random.choices(terrain_choices, terrain_weights)[0] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Initialize grid
grid = generate_grid()

# Initialize animals and plants
animals = []
plants = []

# Animal class
class Animal:
    def __init__(self, x, y, species):
        self.x = x
        self.y = y
        self.species = species
        self.energy = 100
        self.is_nocturnal = species == 'Carnivore'  # Example: Carnivores are nocturnal

    def move(self):
        """Move the animal based on its species-specific behavior."""
        if self.species == 'Herbivore':
            self.move_herbivore()
        elif self.species == 'Carnivore':
            self.move_carnivore()
        elif self.species == 'Omnivore':
            self.move_omnivore()

    def move_herbivore(self):
        """Herbivores move randomly but avoid water and mountains."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = (self.x + dx) % GRID_SIZE
            new_y = (self.y + dy) % GRID_SIZE
            if grid[new_y][new_x] not in ['Water', 'Mountain']:
                self.x, self.y = new_x, new_y
                break

    def move_carnivore(self):
        """Carnivores move towards herbivores if nearby, otherwise move randomly."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for animal in animals:
            if animal.species == 'Herbivore' and abs(animal.x - self.x) <= 2 and abs(animal.y - self.y) <= 2:
                dx = 1 if animal.x > self.x else -1 if animal.x < self.x else 0
                dy = 1 if animal.y > self.y else -1 if animal.y < self.y else 0
                self.x = (self.x + dx) % GRID_SIZE
                self.y = (self.y + dy) % GRID_SIZE
                return
        self.x = (self.x + random.choice([-1, 0, 1])) % GRID_SIZE
        self.y = (self.y + random.choice([-1, 0, 1])) % GRID_SIZE

    def move_omnivore(self):
        """Omnivores move randomly but prefer grassland and forest."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_x = (self.x + dx) % GRID_SIZE
            new_y = (self.y + dy) % GRID_SIZE
            if grid[new_y][new_x] in ['Grassland', 'Forest']:
                self.x, self.y = new_x, new_y
                break

    def reproduce(self):
        """Reproduce if the animal has enough energy."""
        if self.energy > 150:
            self.energy -= 50
            return Animal(self.x, self.y, self.species)
        return None

    def eat(self):
        """Eat plants if herbivore or omnivore, eat herbivores if carnivore."""
        if self.species in ['Herbivore', 'Omnivore']:
            for plant in plants:
                if plant.x == self.x and plant.y == self.y:
                    self.energy += 50
                    plants.remove(plant)
                    return
        elif self.species == 'Carnivore':
            for animal in animals:
                if animal.species == 'Herbivore' and animal.x == self.x and animal.y == self.y:
                    self.energy += 50
                    animals.remove(animal)
                    return

    def avoid_predator(self):
        """Herbivores avoid nearby carnivores."""
        if self.species == 'Herbivore':
            for animal in animals:
                if animal.species == 'Carnivore' and abs(animal.x - self.x) <= 1 and abs(animal.y - self.y) <= 1:
                    self.move_herbivore()

# Plant class
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def grow(self):
        """Plants grow and spread based on terrain type and weather conditions."""
        if random.random() < 0.1:  # 10% chance to spread
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            dx, dy = random.choice(directions)
            new_x = (self.x + dx) % GRID_SIZE
            new_y = (self.y + dy) % GRID_SIZE
            if grid[new_y][new_x] in ['Grassland', 'Forest']:
                plants.append(Plant(new_x, new_y))

# Initialize animals and plants
for _ in range(10):
    animals.append(Animal(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), 'Herbivore'))
    animals.append(Animal(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), 'Carnivore'))
    animals.append(Animal(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1), 'Omnivore'))
for _ in range(50):
    plants.append(Plant(random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)))

# Weather system
current_weather = random.choice(WEATHERS)

def update_weather():
    """Randomly update the weather."""
    global current_weather
    current_weather = random.choice(WEATHERS)

def apply_weather_effects():
    """Apply weather effects on plants and animals."""
    for plant in plants:
        if current_weather == 'Rainy' and grid[plant.y][plant.x] in ['Grassland', 'Forest']:
            plant.grow()
        elif current_weather == 'Snowy' and grid[plant.y][plant.x] in ['Grassland', 'Desert']:
            plants.remove(plant)

    for animal in animals:
        if current_weather == 'Rainy' and animal.species == 'Herbivore':
            animal.energy -= 1
        elif current_weather == 'Snowy':
            animal.energy -= 2  # All animals lose more energy in snowy weather

# Day-night cycle
is_day = True

def update_day_night_cycle():
    """Toggle between day and night."""
    global is_day
    is_day = not is_day

def apply_day_night_effects():
    """Apply day-night effects on animal behavior."""
    for animal in animals:
        if is_day and animal.is_nocturnal:
            animal.energy -= 1  # Nocturnal animals lose energy during the day
        elif not is_day and not animal.is_nocturnal:
            animal.energy -= 1  # Diurnal animals lose energy during the night

# Natural events
def trigger_natural_event():
    """Randomly trigger a natural event."""
    event = random.choice(['Wildfire', 'Flood', 'Drought'])
    if event == 'Wildfire':
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if grid[y][x] == 'Forest' and random.random() < 0.1:
                    grid[y][x] = 'Grassland'
    elif event == 'Flood':
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if grid[y][x] == 'Desert' and random.random() < 0.1:
                    grid[y][x] = 'Water'
    elif event == 'Drought':
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if grid[y][x] == 'Grassland' and random.random() < 0.1:
                    grid[y][x] = 'Desert'

def draw_text(text, x, y):
    """Draw text on the screen."""
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

def draw_legend():
    """Draw the legend on the screen."""
    legend_items = [
        ("Grassland", COLORS['Grassland']),
        ("Forest", COLORS['Forest']),
        ("Desert", COLORS['Desert']),
        ("Water", COLORS['Water']),
        ("Mountain", COLORS['Mountain']),
        ("Herbivore", COLORS['Herbivore']),
        ("Carnivore", COLORS['Carnivore']),
        ("Omnivore", COLORS['Omnivore']),
        ("Plant", COLORS['Plant'])
    ]
    y_offset = SCREEN_SIZE + 30
    for i, (label, color) in enumerate(legend_items):
        pygame.draw.rect(screen, color, (10, y_offset + i * 20, 15, 15))
        draw_text(label, 30, y_offset + i * 20)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update weather
    if random.random() < 0.01:  # 1% chance to change weather each frame
        update_weather()

    # Apply weather effects
    apply_weather_effects()

    # Update day-night cycle
    if random.random() < 0.01:  # 1% chance to change day-night cycle each frame
        update_day_night_cycle()

    # Apply day-night effects
    apply_day_night_effects()

    # Trigger natural events
    if random.random() < 0.01:  # 1% chance to trigger a natural event each frame
        trigger_natural_event()

    # Update animals
    new_animals = []
    for animal in animals:
        animal.move()
        animal.eat()
        animal.avoid_predator()
        new_animal = animal.reproduce()
        if new_animal:
            new_animals.append(new_animal)
    animals.extend(new_animals)

    # Update plants
    for plant in plants:
        plant.grow()

    # Draw grid
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            terrain = grid[y][x]
            color = COLORS[terrain]
            if not is_day:
                color = tuple(c // 2 for c in color)  # Darken colors at night
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw plants
    for plant in plants:
        pygame.draw.rect(screen, COLORS['Plant'], (plant.x * CELL_SIZE, plant.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw animals
    for animal in animals:
        pygame.draw.rect(screen, COLORS[animal.species], (animal.x * CELL_SIZE, animal.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Clear text area
    pygame.draw.rect(screen, COLORS['Night'], (0, SCREEN_SIZE, SCREEN_SIZE, 100))

    # Draw text
    draw_text(f"Weather: {current_weather}", 10, SCREEN_SIZE + 10)
    draw_text(f"Time: {'Day' if is_day else 'Night'}", 200, SCREEN_SIZE + 10)
    draw_text(f"Animals: {len(animals)}", 300, SCREEN_SIZE + 10)
    draw_text(f"Plants: {len(plants)}", 400, SCREEN_SIZE + 10)

    # Draw legend
    draw_legend()

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# Adjust screen size to fit the full legend
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 200))  # Increased extra space for text and legend