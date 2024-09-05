# "abcdefghijklmnopqrstuvwxyz"
# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# TASK 1:
# Function to decrypt a given message by a certain offset
def decode_message(message, offset):
  # Declaring constant variables for readability
  # Obtain the ASCII value for 'z'
  LAST_ALPHABET_ASCII = ord('z')
  # Range of characters in the alphabet
  ALPHABET_RANGE = 26
  # This variable will serve as a placeholder for the decoded message
  decoded_message = ""
  # Loop through each character in the message string
  for character in message:
    # Checking if the current character is part of the alphabet
    if character.isalpha():
      # Obtaining the ASCII value for the current character
      char_ascii = ord(character)
      # Decode by applying the offset value to the current character
      char_ascii += offset
      # Check if the decoded character goes beyond the alphabet range
      if char_ascii > LAST_ALPHABET_ASCII:
        # This will loop the character back to the beginning of the range
        char_ascii -= ALPHABET_RANGE
      # Convert the ASCII value to its character counterpart
      decoded_char = chr(char_ascii)
      # Add the character to the placeholder
      decoded_message += decoded_char
    # This will handle the characters that are not part of the alphabet
    else:
      decoded_message += character
  return(decoded_message);

message1 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!\n"
print(decode_message(message1, 10))

# TASK 2:
# Function to encrypt a given message by a certain offset
def encode_message(message, offset):
  # Declaring constant variables for readability
  # Obtain the ASCII value for 'a'
  FIRST_ALPHABET_ASCII = ord('a')
  # Range of characters in the alphabet
  ALPHABET_RANGE = 26
  # This variable will serve as a placeholder for the encoded message
  encoded_message = ""
  # Loop through each character in the message string
  for character in message:
    # Checking if the current character is part of the alphabet
    if character.isalpha():
      # Obtaining the ASCII value for the current character
      char_ascii = ord(character)
      # Encode by applying the offset value to the current character
      char_ascii -= offset
      # Check if the encoded character goes less than the alphabet range
      if char_ascii < FIRST_ALPHABET_ASCII:
        # This will loop the character back to the end of the range
        char_ascii += ALPHABET_RANGE
      # Convert the ASCII value to its character counterpart
      encoded_char = chr(char_ascii)
      # Add the character to the placeholder
      encoded_message += encoded_char
    # This will handle the characters that are not part of the alphabet
    else:
      encoded_message += character
  return(encoded_message);

my_message1 = "hey, this works great!\n"
print(encode_message(my_message1, 10))

# TASK 3:
message2 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.\n"
message3 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!\n"

print(decode_message(message2, 10))
print(decode_message(message3, 14))

# TASK 4:
message4 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.\n"

print(decode_message(message4, 7))