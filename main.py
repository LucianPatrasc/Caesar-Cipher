logo = ''' adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 '''
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decripteaza":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:  # Dacă litera nu e în alfabet, o lăsăm neschimbată
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f'Acesta este rezultatul {encode_or_decode} : {output_text}')

sa_continuam = True

# Bucla principală
while sa_continuam:
    direction = input("Scrie 'cripteaza' sa criptezi, scrie 'decripteaza' sa decriptezi:\n").lower()
    text = input("Scrie mesajul:\n").lower()
    shift = int(input("Scrie numarul pentru muta cifrele:\n"))

    # Apelăm funcția caesar
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Întrebăm utilizatorul dacă vrea să continue
    restart = input("Scrie 'da' daca vrei sa continui, altfel scrie 'nu'. \n").lower()
    if restart == "nu":
        sa_continuam = False
        print("La revedere!")