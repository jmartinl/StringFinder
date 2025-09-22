"""
String Finder Algorithm

This module provides functionality to find strings in a 2D character matrix
using horizontal and vertical single-step moves only.

Author: jmartinl
Date: September 22, 2025
"""

def find_string_in_matrix(matrix, target_string):
    """
    Find a string in a 2D character matrix using horizontal and vertical moves.
    
    Args:
        matrix (list[list[str]]): 2D matrix of characters
        target_string (str): String to search for
        
    Returns:
        bool: True if string is found, False otherwise
        
    """
    # Use find_string_with_path to determine if the string exists
    path = find_string_with_path(matrix, target_string)
    return path is not None

def manhattan_distance(p1, p2):
    """
    Calculate the Manhattan distance between two points.
    
    Args:
        p1 (tuple[int, int]): First point (row, col)
        p2 (tuple[int, int]): Second point (row, col)
        
    Returns:
        int: Manhattan distance
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Get all positions of a character in a string
def get_char_positions_in_string(tgt_string, char):
    """
    Get all positions of a character in the target string.
    
    Args:
        tgt_string (str): Target string
        char (str): Character to find

    Returns:
        list[int]: List of indices where char is found
    """
    return [i for i, c in enumerate(tgt_string) if c == char]

def get_char_positions_in_matrix(matrix, char):
    """
    Get all positions of a character in the matrix.
    
    Args:
        matrix (list[list[str]]): 2D matrix of characters
        char (str): Character to find
        
    Returns:
        list[tuple[int, int]]: List of (row, col) positions where char is found
    """
    positions = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == char:
                positions.append((r, c))
    return positions

def find_string_with_path(matrix, target_string):
    """
    Find a string in a 2D character matrix and return the path.
    
    Args:
        matrix (list[list[str]]): 2D matrix of characters
        target_string (str): String to search for
        
    Returns:
        list[tuple[int, int]] or None: List of (row, col) coordinates forming the path,
                                      or None if string is not found
                                      
    """

    # Return None for empty matrix
    if not matrix or not matrix[0]:
        return None
    # Return empty path for empty string
    if not target_string:
        return []

    # First, get the positions of all characters in the target string
    char_positions = {char: get_char_positions_in_matrix(matrix, char) for char in set(target_string)}
    # If any character in the target string is not found or there are less occurrences than in the searched string, return None
    # And keep track of the character with the lowest amount of positions
    min_char = None
    min_count = len(matrix) * len(matrix[0]) + 1
    for char in target_string:
        if not char_positions.get(char) or len(char_positions[char]) < target_string.count(char):
            return None
        if len(char_positions[char]) < min_count:
            min_count = len(char_positions[char])
            min_char = char

    path = list(None for _ in target_string)
    # Start from each position of the character with the fewest occurrences
    start_positions = char_positions[min_char]
    for start in start_positions:
        # For every matrix start position iterate on its position in the target string
        for start_index in get_char_positions_in_string(target_string, min_char):
            path[start_index] = start
            # Check for every valid direction whether the predecessor character is reachable
            # If so, start an iterative approach until the first character is reached
            # In that approach, do not check positions already in the path
            visited = set()
            current = start
            idx = start_index
            while current and current not in visited and idx > 0:
                visited.add(current)
                # Get the valid moves from the current position
                for direction in get_valid_moves(matrix, current[0], current[1]):
                    if direction in char_positions.get(target_string[idx - 1], []):
                        path[start_index - 1] = direction
                        current = direction
                        idx -= 1
                        break
                else:
                    break
            # Do the same for the successor characters but first remove the start position from visited if existent
            if start in visited:
                visited.remove(start)
            current = start
            idx = start_index
            while current and current not in visited and idx < len(target_string) - 1:
                visited.add(current)
                for direction in get_valid_moves(matrix, current[0], current[1]):
                    if direction in char_positions.get(target_string[idx + 1], []):
                        path[idx + 1] = direction
                        current = direction
                        idx += 1
                        break
                else:
                    break
            # If the length of the path matches the length of the target string and there are no None values, return the path
            if len(path) == len(target_string) and all(pos is not None for pos in path):
                return path
    return None

def is_valid_position(matrix, row, col):
    """
    Check if a position is valid within the matrix bounds.
    
    Args:
        matrix (list[list[str]]): 2D matrix of characters
        row (int): Row index
        col (int): Column index
        
    Returns:
        bool: True if position is valid, False otherwise
    """
    if not matrix or not matrix[0]:
        return False
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def get_valid_moves(matrix, row, col):
    """
    Get valid horizontal and vertical moves from current position.
    
    Args:
        matrix (list[list[str]]): 2D matrix of characters
        row (int): Current row
        col (int): Current column
        
    Returns:
        list[tuple[int, int]]: List of valid (row, col) positions
    """
    moves = []
    # Horizontal and vertical directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_position(matrix, new_row, new_col):
            moves.append((new_row, new_col))
    
    return moves


if __name__ == "__main__":
    # Example usage - you can test your implementation here
    sample_matrix = [
        ['H', 'E', 'L', 'L', 'O'],
        ['W', 'O', 'R', 'L', 'D'],
        ['P', 'Y', 'T', 'H', 'O'],
        ['N', 'A', 'L', 'G', 'N']
    ]
    
    print("Sample matrix:")
    for row in sample_matrix:
        print(' '.join(row))
    
    # Test your implementation
    result = find_string_with_path(sample_matrix, "HELLO")
    print(f"Found 'HELLO': {result}")