import re
import sys

def validate_hospital_pattern(input_string):
    """
    Validates if the input string matches the hospital pattern requirements.
    Example: Check if 'Doctor' or 'Nurse' is present, and handle 'I'm not a patient' logic.
    """
    # Define the pattern to check for roles
    role_pattern = r'(Doctor|Nurse)'
    
    # Check if the input indicates the person is not a patient
    not_patient_phrase = "I'm not a patient"
    
    if not_patient_phrase.lower() in input_string.lower():
        return f"Input: '{input_string}' states they are not a patient."
    
    # Check for valid roles
    if re.search(role_pattern, input_string, re.IGNORECASE):
        return f"Valid input: '{input_string}' matches the hospital role pattern."
    else:
        return f"Invalid input: '{input_string}' does not match any recognized roles."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hospital_pattern_extended.py <input_string>")
        sys.exit(1)

    input_string = sys.argv[1]
    result = validate_hospital_pattern(input_string)
    print(result)
