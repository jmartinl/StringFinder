# String Finder Project - Copilot Instructions

This workspace contains a Python implementation for finding strings in a 2D character matrix using horizontal and vertical single-step moves only.

## Architecture Overview

Two main algorithms with optimization strategy:
- `find_string_in_matrix()` - Returns boolean result, delegates to path finder
- `find_string_with_path()` - Core algorithm with Manhattan distance optimization and character frequency analysis

**Key optimization pattern**: Start search from the rarest character in the target string to minimize search space.

## Core Algorithm Components

### Character Position Mapping
```python
# Pattern: Pre-compute all character positions for O(1) lookup
char_positions = {char: get_char_positions_in_matrix(matrix, char) for char in set(target_string)}
```

### Bidirectional Path Building
The algorithm builds paths in both directions from the starting position:
- Backward search: `idx > 0` iterating toward string start
- Forward search: `idx < len(target_string) - 1` iterating toward string end

### Helper Functions
- `is_valid_position(matrix, row, col)` - Bounds checking
- `get_valid_moves(matrix, row, col)` - Returns 4-directional neighbors (no diagonals)
- `manhattan_distance(p1, p2)` - Distance calculation utility

## Testing Strategy

### Multi-Modal Testing
1. **Automated**: `pytest test_string_finder.py -v`
2. **Interactive**: `python test_data/test_runner.py --interactive`
3. **Debug**: VS Code launch configurations for algorithm and tests

### Test Matrix Categories
- `SIMPLE_MATRIX` - 3x3 basic patterns (ABC, ADG, etc.)
- `REPEAT_MATRIX` - Duplicate character handling
- `WORD_MATRIX` - Real word finding (HELLO, WORLD)
- `LARGE_MATRIX` - Performance testing

### Common Test Patterns
```python
# Edge cases always tested
assert find_string_in_matrix([], "A") == False        # Empty matrix
assert find_string_in_matrix(matrix, "") == True      # Empty string
assert find_string_in_matrix([['A']], "A") == True    # Single cell
```

## Development Workflow

### VS Code Integration
- Launch configs: "Launch String Finder" and "Run Tests"
- Python environment auto-configured via `.venv/`
- Requirements: `pytest>=7.0.0`, optional `black`, `mypy`

### Interactive Testing Commands
```bash
# Run specific test patterns
python test_data/test_runner.py
# Interactive mode with commands:
# - "SIMPLE_MATRIX ABC" (test specific case)
# - "show SIMPLE_MATRIX" (display matrix)
# - "quit" (exit)
```

## Critical Implementation Notes

- **Movement constraints**: Only `[(0,1), (0,-1), (1,0), (-1,0)]` directions allowed
- **Path validation**: Check `all(pos is not None for pos in path)` before returning
- **Optimization**: Character frequency analysis via `get_char_positions_in_string()` to start from rarest chars
- **Memory management**: Use `visited` sets to prevent cycles in path building