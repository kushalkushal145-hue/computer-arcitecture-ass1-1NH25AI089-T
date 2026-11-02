def format_8bit(val):
    """Formats an integer as an 8-bit binary string."""
    return f"{val & 0xFF:08b}"

def rotate_left_without_carry(binary_str, positions=2):
    """
    ROL (Rotate Left without Carry)
    The bits shifted out from the MSB re-enter at the LSB.
    """
    print("-" * 50)
    print("a) Rotate Left Without Carry (ROL)")
    print("-" * 50)
    print(f"Original 8-bit number : {binary_str}")
    
    val = int(binary_str, 2)
    
    # Step-by-step demonstration
    current_val = val
    for step in range(1, positions + 1):
        # Extract the MSB (bit 7)
        msb = (current_val & 0x80) >> 7
        # Shift left by 1 and mask to 8 bits, then add the MSB at the LSB position
        next_val = ((current_val << 1) & 0xFF) | msb
        
        print(f"Step {step}: Shift left. Bit moved out (MSB): {msb}. New value: {format_8bit(next_val)}")
        current_val = next_val
        
    print(f"Final 8-bit Result   : {format_8bit(current_val)}\n")
    return current_val

def rotate_left_with_carry(binary_str, positions=2, initial_carry=0):
    """
    RCL (Rotate Left with Carry)
    Treats the carry flag as a 9th bit.
    MSB goes to Carry, and old Carry goes to LSB.
    """
    print("-" * 50)
    print("b) Rotate Left With Carry (RCL)")
    print("-" * 50)
    print(f"Original 8-bit number : {binary_str}")
    print(f"Initial Carry Flag    : {initial_carry}")
    
    val = int(binary_str, 2)
    current_val = val
    carry = initial_carry
    
    # Step-by-step demonstration
    for step in range(1, positions + 1):
        # The bit that will move into the carry flag is the current MSB (bit 7)
        next_carry = (current_val & 0x80) >> 7
        # Shift left by 1, mask to 8 bits, and bring in the old carry flag at the LSB
        next_val = ((current_val << 1) & 0xFF) | carry
        
        print(f"Step {step}: Old Carry [{carry}] -> LSB. MSB [{next_carry}] -> New Carry. Value: {format_8bit(next_val)}")
        
        current_val = next_val
        carry = next_carry
        
    print(f"Final 8-bit Result   : {format_8bit(current_val)}")
    print(f"Final Carry Flag      : {carry}\n")
    return current_val, carry

# --- Program Execution and Verification ---
if __name__ == "__main__":
    input_binary = "10110110"
    
    # Execute ROL
    rol_res = rotate_left_without_carry(input_binary, positions=2)
    
    # Execute RCL (Assuming an initial carry flag of 0)
    rcl_res, final_cf = rotate_left_with_carry(input_binary, positions=2, initial_carry=0)
    
    # Manual Calculation Verification Layout
    print("=" * 50)
    print("MANUAL VERIFICATION")
    print("=" * 50)
    print("Original Number: 1 0 1 1 0 1 1 0")
    print("\na) ROL by 2 manual steps:")
    print("   • Start : 10110110")
    print("   • Step 1: 01101101 (Leftmost '1' wraps around to the right end)")
    print("   • Step 2: 11011010 (Leftmost '0' wraps around to the right end)")
    print(f"   • Match Verified: {format_8bit(rol_res) == '11011010'}")
    
    print("\nb) RCL by 2 manual steps (Initial CF = 0):")
    print("   • Start : [CF:0] 10110110")
    print("   • Step 1: MSB '1' goes to CF. Old CF '0' goes to LSB -> [CF:1] 01101100")
    print("   • Step 2: MSB '0' goes to CF. Old CF '1' goes to LSB -> [CF:0] 11011001")
    print(f"   • Match Verified: {format_8bit(rcl_res) == '11011001' and final_cf == 0}")