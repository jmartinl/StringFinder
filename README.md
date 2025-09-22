# String Finder in 2D Matrix

A Python implementation for finding strings in a 2D character matrix using horizontal and vertical single-step moves only.

## Problem Description

Given a 2D matrix of characters and a target string, find if the string can be formed by moving through adjacent cells in the matrix. Movement is restricted to:
- Horizontal moves (left ↔ right)
- Vertical moves (up ↔ down)
- Single-step moves only (no diagonal movement)

## Project Structure

```
StringFinder/
├── string_finder.py          # Main algorithm implementation (your code goes here)
├── test_string_finder.py     # Comprehensive pytest test suite
├── test_data/               
│   ├── sample_matrices.py    # Sample matrices and test cases
│   └── test_runner.py        # Manual test runner script
├── README.md                # This file
└── .github/
    └── copilot-instructions.md  # Copilot workspace instructions
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pytest (for running the test suite)

### Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install pytest (optional, for running automated tests):
   ```bash
   pip install pytest
   ```

### Your Task

Implement the main algorithms in `string_finder.py`:

1. **`find_string_in_matrix(matrix, target_string)`**
   - Returns `True` if the string can be found, `False` otherwise

2. **`find_string_with_path(matrix, target_string)`**
   - Returns a list of (row, col) coordinates forming the path
   - Returns `None` if the string cannot be found

The helper functions `is_valid_position()` and `get_valid_moves()` are already implemented to assist you.

## Testing Your Implementation

### Option 1: Automated Tests (Recommended)
Run the comprehensive test suite:
```bash
# Run all tests
pytest test_string_finder.py

# Run with verbose output
pytest -v test_string_finder.py

# Run specific test class
pytest test_string_finder.py::TestStringFinder
```

### Option 2: Manual Testing
Use the interactive test runner:
```bash
# Run all predefined test cases
python test_data/test_runner.py

# Interactive mode for custom testing
python test_data/test_runner.py --interactive
```

In interactive mode, you can:
- Test custom strings: `SIMPLE_MATRIX ABC`
- Display matrices: `show SIMPLE_MATRIX`
- Type `quit` to exit

### Option 3: Direct Testing
Run the main file to test with sample data:
```bash
python string_finder.py
```

## Example Usage

```python
from string_finder import find_string_in_matrix, find_string_with_path

# Sample 3x3 matrix
matrix = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

# Test if string can be found
result = find_string_in_matrix(matrix, "ABC")  # Should return True
print(f"Found 'ABC': {result}")

# Get the path
path = find_string_with_path(matrix, "ABC")
print(f"Path: {path}")  # Should return [(0,0), (0,1), (0,2)]
```

## Test Cases Included

The test suite covers:

### Basic Cases
- Empty matrices and strings
- Single character matrices
- Horizontal strings (left-to-right and right-to-left)
- Vertical strings (top-to-bottom and bottom-to-top)

### Complex Cases
- L-shaped paths requiring direction changes
- Zigzag patterns
- Matrices with repeated characters
- Large matrices with word patterns

### Edge Cases
- Single row/column matrices
- Strings longer than possible paths
- Case sensitivity
- Invalid diagonal patterns (should return False)

### Sample Matrices
- **SIMPLE_MATRIX**: 3x3 basic alphabet grid
- **WORD_MATRIX**: Contains words like "HELLO", "WORLD", "PYTHON"
- **REPEAT_MATRIX**: Matrix with repeated characters for testing complex paths
- **LARGE_MATRIX**: 5x6 matrix for performance testing

## Algorithm Hints

Consider these approaches:
1. **Backtracking**: Try each starting position and explore all valid paths
2. **DFS/BFS**: Use depth-first or breadth-first search from each starting position
3. **Dynamic Programming**: For optimization (advanced)

Key considerations:
- Track visited cells to avoid cycles
- Handle string reversal (paths can go in any direction)
- Optimize for early termination when string cannot be completed

## Expected Results

Some example test cases and their expected results:

```python
# Matrix: [['A','B','C'], ['D','E','F'], ['G','H','I']]
find_string_in_matrix(matrix, "ABC")    # True  (horizontal)
find_string_in_matrix(matrix, "ADG")    # True  (vertical)
find_string_in_matrix(matrix, "AEI")    # False (diagonal not allowed)
find_string_in_matrix(matrix, "ADE")    # True  (L-shaped path)
find_string_in_matrix(matrix, "ABEF")   # True  (complex path)
```

## Contributing

Feel free to:
- Add more test cases
- Optimize the algorithm
- Add additional features (like finding all possible paths)
- Improve documentation

## License

This project is for educational purposes. Feel free to use and modify as needed.

---

**Happy Coding!** 🚀

Start by implementing the `find_string_in_matrix` function and use the tests to validate your solution.