import streamlit as st
import random

st.set_page_config(page_title="Maze Escape", page_icon="🧩")
st.title("🧩 Maze Escape")

# Game configuration
WIDTH = 10
HEIGHT = 10
LEVELS = 5

# Initialize state
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'player_pos' not in st.session_state:
    st.session_state.player_pos = [0, 0]
if 'maze' not in st.session_state:
    st.session_state.maze = []
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'moves' not in st.session_state:
    st.session_state.moves = 0
if 'visited' not in st.session_state:
    st.session_state.visited = set()
if 'move_request' not in st.session_state:
    st.session_state.move_request = None
if 'processed_move' not in st.session_state:
    st.session_state.processed_move = False

# Maze generation
def generate_maze(level):
    maze = [[1 if random.random() < 0.25 + (level * 0.03) else 0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    maze[0][0] = 0
    maze[HEIGHT-1][WIDTH-1] = 0
    return maze

# New level
if not st.session_state.maze:
    st.session_state.maze = generate_maze(st.session_state.level)

def move_player(dx, dy):
    x, y = st.session_state.player_pos
    new_x = max(0, min(WIDTH - 1, x + dx))
    new_y = max(0, min(HEIGHT - 1, y + dy))
    if st.session_state.maze[new_y][new_x] == 0:
        st.session_state.player_pos = [new_x, new_y]
        st.session_state.moves += 1
        st.session_state.visited.add((new_x, new_y))
        st.session_state.message = ""
        if [new_x, new_y] == [WIDTH-1, HEIGHT-1]:
            if st.session_state.level < LEVELS:
                st.session_state.level += 1
                st.session_state.maze = generate_maze(st.session_state.level)
                st.session_state.player_pos = [0, 0]
                st.session_state.moves = 0
                st.session_state.visited = set()
                st.session_state.message = f"🎉 Level {st.session_state.level} unlocked!"
            else:
                st.session_state.message = "🏆 You escaped all levels!"
    else:
        st.session_state.message = "🚧 Blocked!"

# Handle pending move only once
if st.session_state.move_request and not st.session_state.processed_move:
    move_player(*st.session_state.move_request)
    st.session_state.processed_move = True

# Display maze
emoji_map = {0: '⬜', 1: '⬛'}
grid = [[emoji_map[st.session_state.maze[y][x]] for x in range(WIDTH)] for y in range(HEIGHT)]
for vx, vy in st.session_state.visited:
    if grid[vy][vx] == '⬜':
        grid[vy][vx] = '▫️'

x, y = st.session_state.player_pos
grid[y][x] = '🚶'
grid[HEIGHT-1][WIDTH-1] = '🏁'

rendered = "\n".join("".join(row) for row in grid)
st.markdown(f"""```
{rendered}
```""")

st.markdown(f"**Level:** {st.session_state.level} | **Moves:** {st.session_state.moves}")
st.markdown(st.session_state.message)

# Controls
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️"):
        st.session_state.move_request = (0, -1)
        st.session_state.processed_move = False
col1, _, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("⬅️"):
        st.session_state.move_request = (-1, 0)
        st.session_state.processed_move = False
with col3:
    if st.button("➡️"):
        st.session_state.move_request = (1, 0)
        st.session_state.processed_move = False
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬇️"):
        st.session_state.move_request = (0, 1)
        st.session_state.processed_move = False

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.level = 1
    st.session_state.maze = generate_maze(1)
    st.session_state.player_pos = [0, 0]
    st.session_state.message = "Game restarted."
    st.session_state.moves = 0
    st.session_state.visited = set()
    st.session_state.move_request = None
    st.session_state.processed_move = False
