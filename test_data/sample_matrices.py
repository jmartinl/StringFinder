# Sample matrices for testing the string finder algorithm

# Simple 3x3 matrix for basic testing
SIMPLE_MATRIX = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

# Matrix with words
WORD_MATRIX = [
    ['H', 'E', 'L', 'L', 'O'],
    ['W', 'O', 'R', 'L', 'D'],
    ['P', 'Y', 'T', 'H', 'O'],
    ['N', 'A', 'L', 'G', 'N']
]

# Matrix with repeated characters
REPEAT_MATRIX = [
    ['A', 'A', 'B', 'A'],
    ['A', 'B', 'A', 'B'],
    ['B', 'A', 'A', 'A'],
    ['A', 'B', 'B', 'A']
]

# Larger matrix for complex testing
LARGE_MATRIX = [
    ['Q', 'W', 'E', 'R', 'T', 'Y'],
    ['A', 'S', 'D', 'F', 'G', 'H'],
    ['Z', 'X', 'C', 'V', 'B', 'N'],
    ['M', 'L', 'K', 'J', 'I', 'O'],
    ['P', 'U', 'Q', 'W', 'E', 'R']
]

# Test cases with expected results
TEST_CASES = [
    # (matrix_name, search_string, expected_result, description)
    ("SIMPLE_MATRIX", "ABC", True, "Horizontal line, first row"),
    ("SIMPLE_MATRIX", "ADG", True, "Vertical line, first column"),
    ("SIMPLE_MATRIX", "AEI", False, "Diagonal line (not allowed)"),
    ("SIMPLE_MATRIX", "ADE", True, "L-shaped path"),
    ("SIMPLE_MATRIX", "CBA", True, "Reverse horizontal"),
    ("SIMPLE_MATRIX", "IHG", True, "Reverse horizontal, last row"),
    ("SIMPLE_MATRIX", "CFI", True, "Vertical line, last column"),
    ("SIMPLE_MATRIX", "IFC", True, "Reverse vertical, last column"),
    ("SIMPLE_MATRIX", "ABEF", True, "Complex path"),
    ("SIMPLE_MATRIX", "ACEG", False, "Diagonal (not allowed)"),
    
    ("WORD_MATRIX", "HELLO", True, "Find HELLO"),
    ("WORD_MATRIX", "WORLD", True, "Find WORLD"),
    ("WORD_MATRIX", "PYTHON", True, "Find PYTHON"),
    ("WORD_MATRIX", "HEL", True, "Partial word"),
    ("WORD_MATRIX", "HELP", False, "Word not in matrix"),
    
    ("REPEAT_MATRIX", "AAB", True, "With repeated characters"),
    ("REPEAT_MATRIX", "ABA", True, "Alternating pattern"),
    ("REPEAT_MATRIX", "ABAB", True, "Longer alternating pattern"),
    
    ("LARGE_MATRIX", "QWERTY", True, "Full first row"),
    ("LARGE_MATRIX", "QAZMPL", True, "Full first column"),
    ("LARGE_MATRIX", "ASDF", True, "Partial second row"),
]

# Edge case matrices
EDGE_CASES = {
    "SINGLE_CHAR": [['A']],
    "SINGLE_ROW": [['A', 'B', 'C', 'D', 'E']],
    "SINGLE_COL": [['A'], ['B'], ['C'], ['D'], ['E']],
    "EMPTY": [],
    "EMPTY_ROW": [[]],
}

# Edge case test scenarios
EDGE_CASE_TESTS = [
    ("SINGLE_CHAR", "A", True, "Single character found"),
    ("SINGLE_CHAR", "B", False, "Single character not found"),
    ("SINGLE_ROW", "ABCDE", True, "Full row"),
    ("SINGLE_ROW", "EDCBA", True, "Full row reversed"),
    ("SINGLE_ROW", "ACE", False, "Non-adjacent characters"),
    ("SINGLE_COL", "ABCDE", True, "Full column"),
    ("SINGLE_COL", "EDCBA", True, "Full column reversed"),
    ("SINGLE_COL", "ACE", False, "Non-adjacent characters"),
    ("EMPTY", "A", False, "Empty matrix"),
    ("EMPTY_ROW", "A", False, "Empty row matrix"),
]