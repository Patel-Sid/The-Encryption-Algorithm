"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message2.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    # Open both the deck and files for reading
    deck_filename = open(DECK_FILENAME, "r")
    msg_filename = open(MSG_FILENAME, "r")
    # Saves the deck after reading it
    deck = cipher_functions.read_deck(deck_filename)
    # Saves the messages after reading it
    msg = cipher_functions.read_messages(msg_filename)
    # This will print the decrypted or encrypted message that is in the file
    print(cipher_functions.process_message(deck, msg, MODE))
    # This will make sure that we close the file after we have opened it
    deck_filename.close()
    msg_filename.close()

main()
