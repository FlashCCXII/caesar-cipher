from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
      shift = shift % 26
    def caesar(plain_text, shift_amount, choose_direction):   
        cipher_text = ""
        if direction == "decode":
            shift_amount *= -1
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
            else:
                cipher_text += letter
        print(f"The {choose_direction}d text is {cipher_text}")
        
    
    caesar(plain_text=text,shift_amount=shift,choose_direction=direction)
    decision = input("Would you like to restart the cipher program? Type 'yes' or 'no'.\n").lower()
    if decision != "yes":
        should_continue = False
        print("Goodbye!")