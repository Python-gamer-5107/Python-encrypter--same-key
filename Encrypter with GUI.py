from tkinter import *


characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

key = ['=', '^', '>', 'z', ']', 'q', '[', 'E', 'P', '?', 'W', "'", 'v', 'n', 'h', 'm', 'B', '1', '0', 'l', '(', 'b', 'w', 'R', 'o', '<', 'Q', 'p', '!', '%', 'Z', 'M', '4', '}', ',', '"', ')', ':', 'U', 'y', '\\', 'J', '7', '3', '6', 'X', '-', '$', '`', 'D', 'I', 't', 'O', 'a', '~', '2', 'A', '8', 'd', '+', 'i', '*', 'V', 'N', 'j', '9', 'K', '|', 'k', ';', '/', '5', '_', 'S', 'f', 'u', 'x', 'Y', 'C', 'H', 's', 'c', 'L', 'g', 'e', '&', '.', '@', '#', 'r', '{', 'F', 'T', 'G', ' ']

def Encrypting():
    org_message1 = Input.get()
    
    enc_message2 = ""
    
    for character in org_message1:
        letter_num = characters.index(character)
        enc_message1 = key[letter_num]
        enc_message2 += enc_message1
    
    enc_message3 = StringVar()
    enc_message3.set(enc_message2)
    
    Output.config(textvariable=enc_message3)

def Decrypting():

    enc_message = Input.get()
    
    org_message2 = ""
    
    for character in enc_message:
        letter_num = key.index(character)
        org_message1 = characters[letter_num]
        org_message2 += org_message1
    
    org_message3 = StringVar()
    org_message3.set(org_message2)
    
    Output.config(textvariable=org_message3)


window = Tk()
window.title("Encrypter")
window.geometry("300x200")
window.resizable(False, False)
window.config(bg="Black")

Input = Entry(window, font=100)
Input.pack(pady=20, side=TOP)

Frame = Frame(window, bg="Black")
Frame.pack(pady=10, padx=5, side=TOP)

Encrypt = Button(Frame, text="Encrypt", font=25, command=Encrypting)
Encrypt.pack(padx=10, side=LEFT)

Decrypt = Button(Frame, text="Decrypt", font=25, command=Decrypting)
Decrypt.pack(padx=10, side=RIGHT)

Output = Entry(window, font=100, state="readonly")
Output.pack(pady=20, side=BOTTOM)

window.mainloop()