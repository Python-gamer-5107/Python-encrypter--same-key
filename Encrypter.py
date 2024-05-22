en_list = ["encrypt", "en", "e"]
de_list = ["decrypt", "de", "de"]

answer2 = None

while (answer2 not in en_list) and (answer2 not in de_list):
    print("\nDo you want to encrypt or decrypt?")
    answer1 = input()
    answer2 = answer1.lower()

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

key = ['=', '^', '>', 'z', ']', 'q', '[', 'E', 'P', '?', 'W', "'", 'v', 'n', 'h', 'm', 'B', '1', '0', 'l', '(', 'b', 'w', 'R', 'o', '<', 'Q', 'p', '!', '%', 'Z', 'M', '4', '}', ',', '"', ')', ':', 'U', 'y', '\\', 'J', '7', '3', '6', 'X', '-', '$', '`', 'D', 'I', 't', 'O', 'a', '~', '2', 'A', '8', 'd', '+', 'i', '*', 'V', 'N', 'j', '9', 'K', '|', 'k', ';', '/', '5', '_', 'S', 'f', 'u', 'x', 'Y', 'C', 'H', 's', 'c', 'L', 'g', 'e', '&', '.', '@', '#', 'r', '{', 'F', 'T', 'G', ' ']

if answer2 in en_list:
    
    print("\nWhat message do you want to encrypt?")
    org_message2 = str(input())
    
    enc_message2 = ""
    
    for character in org_message2:
        letter_num = characters.index(character)
        enc_message1 = key[letter_num]
        enc_message2 += enc_message1

elif answer2 in de_list:
    
    print("\nWhat do you want to decrypt?")
    enc_message2 = str(input())
    
    org_message2 = ""
    
    for character in enc_message2:
        letter_num = key.index(character)
        org_message1 = characters[letter_num]
        org_message2 += org_message1

print()
print(f"Orginal message:   {org_message2}")
print(f"Encrypted message: {enc_message2}")    