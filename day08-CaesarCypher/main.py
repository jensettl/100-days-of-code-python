# Casesar Cypher

from logo import logo


def transform(text, shift_number, mode):
    output = ""
    if mode == "decode":
        shift_number *= -1
    shift_number %= 26
    for letter in text:
        output_char = ord(letter) + shift_number
        if output_char > 122:
            output_char -= 26
        elif output_char < 97:
            output_char += 26
        output += chr(output_char)
    return output


def main():
    should_repeat = True
    while should_repeat:
        # User input
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Enter a word:\n").lower().replace(" ", "")
        shift = int(input("Enter a shift number:\n"))

        # Transform text
        result = transform(text=text, shift_number=shift, mode=choice)
        print(f"Here's the {choice}d result: {result}")

        # Repeat programm
        repeat = input("Want to try again? Type 'yes' or 'no'.\n").lower()
        if repeat == "no":
            should_repeat = False
            print("Goodbye!")


if __name__ == "__main__":
    print(logo)
    main()
