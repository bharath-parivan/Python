import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Step 1: Set grid size
GRID_SIZE = 50

# Step 2: Create a random initial grid
def random_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.8, 0.2]).reshape(size, size)

# Step 3: Define the update rules
def update(frame_num, img, grid, size):
    new_grid = grid.copy()
    for i in range(size):
        for j in range(size):
            # Count live neighbors with wrap-around (toroidal array)
            total = int((
                grid[i, (j-1)%size] + grid[i, (j+1)%size] +
                grid[(i-1)%size, j] + grid[(i+1)%size, j] +
                grid[(i-1)%size, (j-1)%size] + grid[(i-1)%size, (j+1)%size] +
                grid[(i+1)%size, (j-1)%size] + grid[(i+1)%size, (j+1)%size]
            ))

            # Apply Conway's rules
            if grid[i, j] == 1:
                if total < 2 or total > 3:
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

# Step 4: Set up and run animation
def run_game():
    grid = random_grid(GRID_SIZE)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='binary')
    ani = animation.FuncAnimation(
        fig, update, fargs=(img, grid, GRID_SIZE),
        frames=100, interval=200, save_count=50
    )
    plt.show()

# Step 5: Run the simulation
if __name__ == "__main__":
    run_game()
