import sys

def test_logic():
    print("Running system checks...")
    
    # Let's pretend we expect 2 + 2 to equal 5 (A logical error)
    expected_result = 4
    actual_result = 2 + 2
    
    if actual_result != expected_result:
        print(f"CRITICAL ERROR: Math is broken! Expected {expected_result} but got {actual_result}")
        # This command tells GitHub the program failed (Exit Code 1)
        sys.exit(1) 
    
    print("Test Passed!")

if __name__ == "__main__":
    test_logic()