# Test runner script for manual testing of the string finder algorithm

import sys
import os

# Add parent directory to path to import string_finder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from string_finder import find_string_in_matrix, find_string_with_path
from sample_matrices import *

def print_matrix(matrix, title="Matrix"):
    """Print a matrix in a readable format."""
    print(f"\n{title}:")
    if not matrix:
        print("  (empty)")
        return
    
    for row in matrix:
        print("  " + " ".join(row))

def run_test_case(matrix_name, search_string, expected, description):
    """Run a single test case."""
    try:
        matrix = globals()[matrix_name]
        result = find_string_in_matrix(matrix, search_string)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status}: {description}")
        print(f"  Search: '{search_string}' in {matrix_name}")
        print(f"  Expected: {expected}, Got: {result}")
        
        if result and search_string:  # Try to get path if found
            path = find_string_with_path(matrix, search_string)
            if path:
                print(f"  Path: {path}")
        print()
        
        return result == expected
    except Exception as e:
        print(f"✗ ERROR: {description}")
        print(f"  Exception: {e}")
        print()
        return False

def run_all_tests():
    """Run all test cases."""
    print("=" * 60)
    print("STRING FINDER ALGORITHM TEST RUNNER")
    print("=" * 60)
    
    # Display sample matrices
    print("\nSAMPLE MATRICES:")
    print("-" * 40)
    print_matrix(SIMPLE_MATRIX, "SIMPLE_MATRIX (3x3)")
    print_matrix(WORD_MATRIX, "WORD_MATRIX (4x5)")
    print_matrix(REPEAT_MATRIX, "REPEAT_MATRIX (4x4)")
    
    # Run main test cases
    print("\nMAIN TEST CASES:")
    print("-" * 40)
    passed = 0
    total = 0
    
    for matrix_name, search_string, expected, description in TEST_CASES:
        if run_test_case(matrix_name, search_string, expected, description):
            passed += 1
        total += 1
    
    # Run edge cases
    print("\nEDGE CASE TESTS:")
    print("-" * 40)
    
    for matrix_name, search_string, expected, description in EDGE_CASE_TESTS:
        if run_test_case(matrix_name, search_string, expected, description):
            passed += 1
        total += 1
    
    # Summary
    print("=" * 60)
    print(f"TEST SUMMARY: {passed}/{total} tests passed")
    if passed == total:
        print("🎉 All tests passed! Your algorithm is working correctly.")
    else:
        print(f"❌ {total - passed} tests failed. Check your implementation.")
    print("=" * 60)

def interactive_test():
    """Interactive testing mode."""
    print("\nINTERACTIVE TESTING MODE")
    print("-" * 40)
    print("Available matrices: SIMPLE_MATRIX, WORD_MATRIX, REPEAT_MATRIX, LARGE_MATRIX")
    print("Type 'quit' to exit, 'show <matrix>' to display a matrix")
    
    while True:
        try:
            user_input = input("\nEnter command: ").strip()
            
            if user_input.lower() == 'quit':
                break
            
            if user_input.lower().startswith('show '):
                matrix_name = user_input[5:].strip().upper()
                if matrix_name in globals():
                    print_matrix(globals()[matrix_name], matrix_name)
                else:
                    print(f"Matrix '{matrix_name}' not found")
                continue
            
            # Parse test input: "matrix_name search_string"
            parts = user_input.split()
            if len(parts) != 2:
                print("Usage: <matrix_name> <search_string>")
                print("Example: SIMPLE_MATRIX ABC")
                continue
            
            matrix_name, search_string = parts
            matrix_name = matrix_name.upper()
            
            if matrix_name not in globals():
                print(f"Matrix '{matrix_name}' not found")
                continue
            
            matrix = globals()[matrix_name]
            print_matrix(matrix, matrix_name)
            
            result = find_string_in_matrix(matrix, search_string)
            print(f"\nSearching for '{search_string}': {'Found' if result else 'Not found'}")
            
            if result:
                path = find_string_with_path(matrix, search_string)
                if path:
                    print(f"Path: {path}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_test()
    else:
        run_all_tests()
        print("\nTo run in interactive mode: python test_runner.py --interactive")