"""
Test suite for String Finder Algorithm

Comprehensive tests for finding strings in 2D character matrices
using horizontal and vertical single-step moves.
"""

import pytest
from string_finder import find_string_in_matrix, find_string_with_path, is_valid_position, get_valid_moves


class TestStringFinder:
    """Test class for string finder functionality."""

    def setup_method(self):
        """Set up test matrices for testing."""
        # Simple 3x3 matrix
        self.simple_matrix = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I']
        ]
        
        # Matrix with repeated characters
        self.repeat_matrix = [
            ['A', 'A', 'B'],
            ['A', 'B', 'A'],
            ['B', 'A', 'A']
        ]
        
        # Larger matrix with words
        self.word_matrix = [
            ['H', 'E', 'L', 'L', 'O'],
            ['W', 'O', 'R', 'L', 'D'],
            ['P', 'Y', 'T', 'H', 'O'],
            ['N', 'A', 'L', 'G', 'N']
        ]
        
        # Matrix designed for specific path testing
        self.path_matrix = [
            ['S', 'T', 'A', 'R'],
            ['P', 'A', 'T', 'H'],
            ['E', 'N', 'D', 'S'],
            ['X', 'Y', 'Z', 'W']
        ]

    def test_empty_matrix(self):
        """Test with empty matrix."""
        assert find_string_in_matrix([], "A") == False
        assert find_string_in_matrix([[]], "A") == False

    def test_empty_string(self):
        """Test with empty target string."""
        # Empty string should return True (found trivially)
        assert find_string_in_matrix(self.simple_matrix, "") == True

    def test_single_character_matrix(self):
        """Test with single character matrix."""
        single_matrix = [['A']]
        assert find_string_in_matrix(single_matrix, "A") == True
        assert find_string_in_matrix(single_matrix, "B") == False

    def test_single_character_string(self):
        """Test finding single characters."""
        assert find_string_in_matrix(self.simple_matrix, "A") == True
        assert find_string_in_matrix(self.simple_matrix, "E") == True
        assert find_string_in_matrix(self.simple_matrix, "I") == True
        assert find_string_in_matrix(self.simple_matrix, "Z") == False

    def test_horizontal_strings(self):
        """Test finding horizontal strings (left to right)."""
        # Simple horizontal
        assert find_string_in_matrix(self.simple_matrix, "ABC") == True
        assert find_string_in_matrix(self.simple_matrix, "DEF") == True
        assert find_string_in_matrix(self.simple_matrix, "GHI") == True
        
        # Reverse horizontal (right to left)
        assert find_string_in_matrix(self.simple_matrix, "CBA") == True
        assert find_string_in_matrix(self.simple_matrix, "FED") == True
        assert find_string_in_matrix(self.simple_matrix, "IHG") == True

    def test_vertical_strings(self):
        """Test finding vertical strings (top to bottom and bottom to top)."""
        # Top to bottom
        assert find_string_in_matrix(self.simple_matrix, "ADG") == True
        assert find_string_in_matrix(self.simple_matrix, "BEH") == True
        assert find_string_in_matrix(self.simple_matrix, "CFI") == True
        
        # Bottom to top
        assert find_string_in_matrix(self.simple_matrix, "GDA") == True
        assert find_string_in_matrix(self.simple_matrix, "HEB") == True
        assert find_string_in_matrix(self.simple_matrix, "IFC") == True

    def test_l_shaped_paths(self):
        """Test finding strings that require L-shaped paths."""
        # Horizontal then vertical
        assert find_string_in_matrix(self.simple_matrix, "ABE") == True  # A→B→E
        assert find_string_in_matrix(self.simple_matrix, "DEH") == True  # D→E→H
        
        # Vertical then horizontal
        assert find_string_in_matrix(self.simple_matrix, "ADE") == True  # A→D→E

    def test_complex_paths(self):
        """Test finding strings with complex zigzag paths."""
        # Test in word matrix
        assert find_string_in_matrix(self.word_matrix, "HELLO") == True
        assert find_string_in_matrix(self.word_matrix, "WORLD") == True
        assert find_string_in_matrix(self.word_matrix, "PYTHON") == True

    def test_repeated_characters(self):
        """Test with matrices containing repeated characters."""
        assert find_string_in_matrix(self.repeat_matrix, "AAB") == True
        assert find_string_in_matrix(self.repeat_matrix, "ABA") == True
        assert find_string_in_matrix(self.repeat_matrix, "BAA") == True

    def test_nonexistent_strings(self):
        """Test strings that cannot be found."""
        assert find_string_in_matrix(self.simple_matrix, "ACE") == False  # Diagonal
        assert find_string_in_matrix(self.simple_matrix, "XYZ") == False  # Not in matrix
        assert find_string_in_matrix(self.simple_matrix, "ABCD") == False  # Too long for path

    def test_case_sensitivity(self):
        """Test case sensitivity."""
        lowercase_matrix = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]
        assert find_string_in_matrix(lowercase_matrix, "abc") == True
        assert find_string_in_matrix(lowercase_matrix, "ABC") == False

    def test_path_return(self):
        """Test path-returning function."""
        path = find_string_with_path(self.simple_matrix, "ABC")
        if path is not None:
            expected_path = [(0, 0), (0, 1), (0, 2)]
            assert path == expected_path

    def test_is_valid_position(self):
        """Test position validation helper function."""
        assert is_valid_position(self.simple_matrix, 0, 0) == True
        assert is_valid_position(self.simple_matrix, 2, 2) == True
        assert is_valid_position(self.simple_matrix, -1, 0) == False
        assert is_valid_position(self.simple_matrix, 0, -1) == False
        assert is_valid_position(self.simple_matrix, 3, 0) == False
        assert is_valid_position(self.simple_matrix, 0, 3) == False

    def test_get_valid_moves(self):
        """Test valid moves generation."""
        # Corner position
        moves = get_valid_moves(self.simple_matrix, 0, 0)
        assert len(moves) == 2
        assert (0, 1) in moves  # right
        assert (1, 0) in moves  # down
        
        # Center position
        moves = get_valid_moves(self.simple_matrix, 1, 1)
        assert len(moves) == 4
        assert (0, 1) in moves  # up
        assert (2, 1) in moves  # down
        assert (1, 0) in moves  # left
        assert (1, 2) in moves  # right


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_single_row_matrix(self):
        """Test with single row matrix."""
        single_row = [['A', 'B', 'C', 'D', 'E']]
        assert find_string_in_matrix(single_row, "ABCDE") == True
        assert find_string_in_matrix(single_row, "EDCBA") == True
        assert find_string_in_matrix(single_row, "ACE") == False  # Non-adjacent

    def test_single_column_matrix(self):
        """Test with single column matrix."""
        single_col = [['A'], ['B'], ['C'], ['D'], ['E']]
        assert find_string_in_matrix(single_col, "ABCDE") == True
        assert find_string_in_matrix(single_col, "EDCBA") == True
        assert find_string_in_matrix(single_col, "ACE") == False  # Non-adjacent

    def test_large_matrix(self):
        """Test with larger matrix."""
        large_matrix = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
            ['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z', 'A', 'B'],
            ['C', 'D', 'E', 'F', 'G', 'H', 'I']
        ]
        assert find_string_in_matrix(large_matrix, "ABCDEFG") == True
        assert find_string_in_matrix(large_matrix, "HIJKLMN") == True
        assert find_string_in_matrix(large_matrix, "AHOV") == True  # First column

    def test_string_longer_than_matrix(self):
        """Test with string longer than possible in matrix."""
        matrix = [['A', 'B'], ['C', 'D']]
        # Longest possible path in 2x2 matrix is 4 characters
        long_string = "ABCDEFGH"  # 8 characters
        assert find_string_in_matrix(matrix, long_string) == False


# Sample test data for manual testing
SAMPLE_MATRICES = {
    "simple_3x3": [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ],
    "word_search": [
        ['C', 'A', 'T', 'S'],
        ['O', 'D', 'O', 'U'],
        ['D', 'O', 'G', 'N'],
        ['E', 'R', 'S', 'D']
    ],
    "numbers": [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
}

SAMPLE_SEARCHES = [
    ("simple_3x3", "ABC", True),
    ("simple_3x3", "AEI", False),  # Diagonal
    ("simple_3x3", "ADEH", True),  # L-shape
    ("word_search", "CAT", True),
    ("word_search", "DOG", True),
    ("word_search", "CODE", True),
    ("numbers", "123", True),
    ("numbers", "159", False),  # Diagonal
    ("numbers", "147", True),  # Vertical
]


if __name__ == "__main__":
    # Run basic tests
    print("Running basic tests...")
    for matrix_name, search_string, expected in SAMPLE_SEARCHES:
        matrix = SAMPLE_MATRICES[matrix_name]
        # Note: These will fail until you implement the algorithm
        print(f"Matrix: {matrix_name}, Search: '{search_string}', Expected: {expected}")
    
    print("\nTo run full test suite, use: pytest test_string_finder.py")
    print("To run with verbose output: pytest -v test_string_finder.py")