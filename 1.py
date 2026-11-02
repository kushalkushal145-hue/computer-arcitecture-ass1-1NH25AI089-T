def to_twos_complement_8bit(val):
    """Converts an integer to its 8-bit 2's complement binary string representation."""
    # Ensure value fits inside signed 8-bit bounds [-128, 127]
    if not (-128 <= val <= 127):
        raise ValueError(f"Value {val} out of 8-bit signed integer range.")
    
    # Mask to 8 bits to simulate 2's complement hardware representation
    binary_val = val & 0xFF
    return f"{binary_val:08b}"

def from_twos_complement_8bit(bin_str):
    """Converts an 8-bit 2's complement binary string back to a signed decimal integer."""
    val = int(bin_str, 2)
    # If the sign bit (MSB) is 1, it's a negative number
    if val & 0x80:
        val -= 256
    return val

def binary_add_8bit(bin_a, bin_b):
    """Performs 8-bit binary addition and checks for signed arithmetic overflow."""
    # Convert binary strings to integers for simulation
    int_a = int(bin_a, 2)
    int_b = int(bin_b, 2)
    
    # Add them together
    raw_sum = int_a + int_b
    
    # Mask to 8 bits for the actual binary result
    result_bin = (raw_sum) & 0xFF
    result_str = f"{result_bin:08b}"
    
    # Check for signed overflow:
    # Overflow occurs if adding two numbers of the same sign yields a result with a different sign.
    sign_a = bin_a[0]
    sign_b = bin_b[0]
    sign_res = result_str[0]
    
    overflow = (sign_a == sign_b) and (sign_a != sign_res)
    
    return result_str, overflow

def solve_expression(name, operand1, operand2, operation="-"):
    """Simulates the arithmetic operation and prints formatted results."""
    print("=" * 50)
    print(f"Expression {name}: {operand1} {operation} ({operand2})")
    print("=" * 50)

    
    # In 2's complement, subtraction (A - B) is performed as addition: A + (-B)
    if operation == "-":
        effective_op2 = -operand2
    else:
        effective_op2 = operand2
        
    bin_a = to_twos_complement_8bit(operand1)
    bin_b_mod = to_twos_complement_8bit(effective_op2)
    
    print(f"Operand 1 ({operand1:3}): {bin_a}")
    print(f"Operand 2 ({effective_op2:3}): {bin_b_mod}  (Converted for addition)")
    print("-" * 30)
    
    result_bin, overflow = binary_add_8bit(bin_a, bin_b_mod)
    result_dec = from_twos_complement_8bit(result_bin)
    
    print(f"Binary Result : {result_bin}")
    print(f"Decimal Result: {result_dec}")
    print(f"Overflow Status: {'OVERFLOW DETECTED!' if overflow else 'No Overflow'}\n")

# Run Verification Cases
if __name__ == "__main__":
    # Case a) 45 - (+19) -> 45 + (-19)
    solve_expression("a", 45, 19, "-")
    
    # Case b) (-35) - (-12) -> -35 + (+12)
    solve_expression("b", -35, -12, "-")