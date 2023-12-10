
should_end = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("Welcome to message Encoder or Decoder ")
choice = input("Enter  to be Encoded or Decoded ").lower()
# message =input("Enter a message to be Encoded ")
#shift = int(input("Enter the shift number "))

def Encoder(input_message,shift_number) : #Encoder Function
    end_message = ""
    for char in input_message :
        if char in alphabet:
           position = alphabet.index(char)
           new_position = position + shift_number
           end_message += alphabet[new_position]
        else:
            end_message += char
    
    print(f"Your Encoded message is : {end_message}")

def Decoder(input_message,shift_number) : #DEcoder Function
    end_message =""
    for char in input_message :
        if char in alphabet :
            position = alphabet.index(char)
            new_position = position - shift_number
            end_message += alphabet[new_position]
        else :
            end_message += char
    print(f"Your Encoded message is : {end_message}")

while not should_end :
    if choice =="encode" :
        message =input("Enter a message to be Encoded: ")
        shift = int(input("Enter the shift number: "))
        shift = shift % 26
        Encoder(input_message=message,shift_number=shift)
    elif choice =="decode":
        message =input("Enter a message to be Decoded: ")
        shift = int(input("Enter the shift number: "))
        shift = shift % 26
        Decoder(input_message=message,shift_number=shift)
    decision = input("Do you want to continue? Y/N").lower()
    if decision == "y" :
        should_end = True
    else :
        print("Good Bye!!")  
        should_end = False
