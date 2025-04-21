---

# AI Search Algorithms Visualizer

A Python project for visualizing fundamental search algorithms in Artificial Intelligence, including **BFS**, **A\***, **UCS**, and **Bidirectional IDDFS**. The project features an interactive Pygame environment, pathfinding with customizable maps, obstacles, and teleporters, plus real-time animation and visual feedback of algorithm progress.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Demo](#demo)
- [Algorithms Implemented](#algorithms-implemented)
- [Features](#features)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [How Maps Work](#how-maps-work)
- [Custom Map Generation](#custom-map-generation)
- [Code Flow](#code-flow)
- [Requirements](#requirements)
- [Acknowledgements](#acknowledgements)

---

## Project Overview

This application allows you to:
- Experiment with classic graph search algorithms
- **Visualize** the search process, explored nodes, and resulting paths
- Design your own maps with obstacles and teleporters
- Understand how search strategies navigate complex environments, including cost-varying teleports

Great for AI learners, educators, and anyone interested in pathfinding!

---

## Demo

![Demo GIF or Screenshot Placeholder](https://your.demo.link/or-demo-here.gif)

*Shows a grid map, obstacles (black), teleporters (animated color circles), explored area (gradient), and the solution path (red circles).*


---

## Algorithms Implemented

| Algorithm           | Inheritance      | Optimal? | Informed? | Notes |
|---------------------|------------------|----------|-----------|-------|
| **BFS**             | `BFSAgent`       | ✓        | ✗         | Uniform cost (steps), shortest-path |
| **A\* (AStar)**     | `AStarAgent`     | ✓        | ✓         | Euclidean heuristic by default      |
| **UCS**             | `UCSAgent`       | ✓        | ✗         | Handles custom costs                |
| **Bidirectional IDDFS** | `BiIDDFSAgent` | ✗        | ✗         | Layered bidirectional search, fast for very large state spaces |

All agents inherit from `AbstractSearchAgent`, which defines core utilities for path extraction and neighbor finding.

---

## Features

- **Interactive Visualization**: See explored areas and solution path build up in real time
- **Rich Map Editor**: Design custom maps using obstacles & matching teleporter gates
- **Teleporters**: Jump instantly across the map with unique, cost-based teleport gates
- **Multiple Cost Models**: Diagonal, straight, and teleport moves have different costs and random noise for realism
- **Animated UI**: Slick Pygame interface with gradual reveal and animated teleport visuals
- **Flexible Agent Selection**: Run any algorithm easily from the command line UI

---

## Project Structure

```
.
├── agent.py              # Abstract agent base, shared search utilities
├── env.py                # Map environment and state space representation
├── generator.py          # Interactive map editor (create obstacles/teleports)
├── implemented_agents.py # All search algorithms (BFS, UCS, A*, BiIDDFS)
├── main.py               # Entry point: user chooses algorithm & runs animation
├── Maps/
│   └── default.json      # Example map (JSON: obstacles & teleports)
├── plotting.py           # Handles Pygame animation and drawing
└── README.md             # This file!
```

---

## How to Run

1. **Install dependencies** (see [Requirements](#requirements)):
   ```bash
   pip install pygame
   ```
2. **Launch the main program:**
   ```bash
   python main.py
   ```
3. **Choose an algorithm** (A*, BFS, UCS, BiIDDFS) via the CLI prompt.

4. **See search and pathfinding animated!**

---

## How Maps Work

- Maps are stored as **JSON** in `Maps/`.
- **Obstacles**: Listed as `[x, y]` pairs (impassable squares).
- **Teleporters**: Listed as pairs of coordinates, linking entry and exit points.

Example `Maps/default.json`:
```json
{
  "obstacles": [[5, 6], [5, 7], [6, 6]],
  "teleports": [
    [[10, 10], [30, 15]],
    [[20, 2], [40, 20]]
  ]
}
```

---

## Custom Map Generation

Design your map **visually**:
```bash
python generator.py
```
- **Left Click** to toggle obstacles
- **Press `T`** to switch to teleporter mode
- **Left Click** twice to create a teleporter pair
- **Press `Enter`** to save and quit

Obstacles (black squares), teleporters (colored/animated circles), and clear grid shown as you edit.

---

## Code Flow

- **`main.py`**:
  1. Loads the environment and chosen map
  2. Prompts user to select algorithm
  3. Runs the agent's `.searching()` method
  4. Collects path and visited nodes
  5. Animates search in the Pygame window

- **Agents**:
    - All extend `AbstractSearchAgent` (`agent.py`)
    - Use shared neighbor/cost logic, store parent information for path extraction
    - Maintain COST, VISITED, and PARENT for runtime and animation

---

## Requirements

- Python 3.7+
- **pygame**

Install with:
```bash
pip install pygame
```

---

## Acknowledgements

- Developed for **[Your University Name / AI Course Name]**
- Author: [Your Name]
- Special thanks to [your professor/TAs/etc.]

---

> *Feel free to open issues or submit pull requests for new features, bugs, or improvements!*

---

**Enjoy learning about search algorithms and AI pathfinding!**

