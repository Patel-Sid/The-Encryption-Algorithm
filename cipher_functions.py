# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    '''(str) ---> str
    REQ: Length of message must be greater than 0
    REQ: Message must contain only one line
    This function will take a message and convert every character to uppercase
    while removing everything that is not alphabetical
    >>> clean_message("Hello there, have a nice day.")
    'HELLOTHEREHAVEANICEDAY'
    >>>clean_message("$$$$$$,!,@@@@@@")
    ''
    >>>clean_message("       ")
    ''
    >>>clean_message(" This is partofthe system, don't! question! just! folo!")
    'THISISPARTOFTHESYSTEMDONTQUESTIONJUSTFOLO'
    '''
    # This will loop through the message to check if each of character is a
    # alphabet then it will add it using the .join method
    only_alpha = ''.join(i for i in message if i.isalpha())
    # This will remove all the spaces before, between and after the message
    msg_spaces_removed = only_alpha.replace(" ", "")
    # Converts every single character to uppercase
    all_upper = msg_spaces_removed.upper()

    return all_upper


def encrypt_letter(any_char, value):
    '''(str, int) ---> int
    REQ: The length of the character must be equal to 1
    REQ: Only single alphabetical character is accepted for the first parameter
    REQ: The value must be greater than 0 and less than 27
    This function will convert any character entered to upper case then it will
    apply the keystream value entered to the character to encrpyt the character
    and return the encrypted character
    >>> encrypt_letter("A", 1)
    'B'
    >>> encrypt_letter("Z", 25)
    'Y'
    >>> encrypt_letter("z", 25)
    'Y'
    >>> encrypt_letter("B",26)
    'B'
    '''
    # This will first convert the entered character to upper case then get it's
    # ordinal value and subtract it so that the range of alphabets (A-Z) is
    # from (0 to 25)
    number = ord(clean_message(any_char)) - 65
    # This will generate the keystream value by adding the value entered by
    # user and the number previously generated
    keystream_value = number + value
    # If the keystream_value is greater than 25 than subtract 26 from it then
    # generate the encrypted letter
    if keystream_value > 25:
        encrypted_letter = chr((keystream_value - 26) + 65)
    # Otherwise directly generate the encrypted letter
    else:
        encrypted_letter = chr(keystream_value + 65)
    return encrypted_letter


def decrypt_letter(any_char, value):
    '''(str, int) ---> int
    REQ: The length of the character must be equal to 1
    REQ: Only single uppercase alphabetical character is accepted for the first
    paramter
    REQ: The value must be greater than 0 and less than 27
    This function will apply the keystream value entered to the character to
    decrpyt the character and return the original character
    >>> decrypt_letter("B", 1)
    'A'
    >>> decrypt_letter("Y", 25)
    'Z'
    >>> decrypt_letter("Z", 26)
    'Z'
    >>> decrypt_letter("a",26)
    '''
    # This will first check if the character entered is an uppercase, otherwise
    # it won't return the decrypted character
    if any_char.isupper():
        # Get the ordinal value and subtract it so that the range of alphabets
        # (A-Z) is from (0 to 25)
        number = ord(any_char) - 65
        # Generate the keystream value by subtarcting the value entered by
        # user from the number previously generated
        keystream_value = number - value
        # If the keystream value is negative then add 26 to it then generate
        # the decrypted letter
        if keystream_value < 0:
            decrypted_letter = chr((keystream_value + 26) + 65)
            return decrypted_letter
        # Otherwise directly generate the decrypted letter
        else:
            decrypted_letter = chr(keystream_value + 65)
            return decrypted_letter


def swap_cards(deck_of_cards, index):
    '''(list of int, int) -> NoneType
    REQ: The length of the deck of cards must be greater than 1
    REQ: The index must be less than length of deck of cards
    This function will swap the card at the index with the card that follow it.
    Since we treat the deck as circular, if any particular card is at the
    bottom of the deck then swap that card with the top card
    >>> a =[1,8,2,7,15]
    >>> swap_cards(a, 1)
    >>> a
    [1, 2, 8, 7, 15]
    >>> swap_cards(a, 4)
    >>> a
    [15, 2, 8, 7, 1]
    >>> swap_cards(a, 2)
    >>> a
    [15, 2, 7, 8, 1]
    >>> swap_cards(a, 0)
    >>> a
    [2, 15, 7, 8, 1]
    '''
    # If the given index is on the bottom of the deck then remove the last
    # and the first cards and swap their places
    if index == (len(deck_of_cards) - 1):
        last_value = deck_of_cards.pop(index)
        first_value = deck_of_cards.pop(0)
        deck_of_cards.insert(0, last_value)
        deck_of_cards.insert(index, first_value)
    # For all other index values remove card at the index and swap with the
    # following card
    else:
        swap_value = deck_of_cards.pop(index)
        deck_of_cards.insert(index + 1, swap_value)


def move_joker_1(deck_of_cards):
    '''(list of int) -> NoneType
    REQ: JOKER1 must exist in the deck of cards
    REQ: The length of deck of cards must be greater than 1
    This function will find JOKER1 and swap its value with the following card
    treating the deck as circular so if JOKER1 is at the bottom, it swaps
    with the top card
    >>> a = [7,11,9,13,27]
    >>> move_joker_1(a)
    >>> a
    [27, 11, 9, 13, 7]
    >>> move_joker_1(a)
    >>> a
    [11, 27, 9, 13, 7]
    >>> move_joker_1(a)
    >>> a
    [11, 9, 27, 13, 7]
    '''
    # This checks for JOKER1 in the deck of cards and will only execute the
    # code if JOKER1 is in the deck of cards
    if JOKER1 in deck_of_cards:
        # This will find the index value of the JOKER1
        index_of_joker1 = deck_of_cards.index(JOKER1)
        # This will call the swap_cards function to swap the JOKER1 with the
        # next value
        swap_cards(deck_of_cards, index_of_joker1)


def move_joker_2(deck_of_cards):
    '''(list of int) -> NoneType
    REQ: JOKER2 must exist in the deck of cards
    REQ: The length of deck of cards must be greater than 1
    This function will find JOKER2 and move it two cards down, treating the
    deck as circular.
    >>> a = [9,11,26,13,28]
    >>> move_joker_2(a)
    >>> a
    [11, 28, 26, 13, 9]
    >>> move_joker_2(a)
    >>> a
    [11, 26, 13, 28, 9]
    >>> move_joker_2(a)
    >>> a
    [28, 26, 13, 9, 11]
    >>> a = [9,28]
    >>> move_joker_2(a)
    >>> a
    [9, 28]
    '''
    # This checks for JOKER2 in the deck of cards and will only execute the
    # code if JOKER2 is in the deck of cards
    if JOKER2 in deck_of_cards:
        # Find the index of JOKER2 and swap it with the following card
        index_of_joker2 = deck_of_cards.index(JOKER2)
        swap_cards(deck_of_cards, index_of_joker2)
        # Since swap_cards returns NoneType we have to save the swapped
        # deck to a variable
        first_swap = deck_of_cards
        # Find the new index of JOKER2 and swap it again, completing our two
        # swaps and moving it two cards down
        new_index = deck_of_cards.index(JOKER2)
        swap_cards(first_swap, new_index)


def triple_cut(deck_of_cards):
    '''(list of int) -> NoneType
    REQ: The length of deck of cards must be greater than 1
    REQ: Both the jokers must exist in the deck of cards
    Find two jokers and do a triple cut. A triple cut moves everything above
    the first joker to the bottom of the deck, and everything below the second
    joker goes to the top
    >>> a = [8,17,15,9,11,27,28]
    >>> triple_cut(a)
    >>> a
    [27, 28, 8, 17, 15, 9, 11]
    >>> a = [8,17,15,9,27,11,28]
    >>> triple_cut(a)
    >>> a
    [27, 11, 28, 8, 17, 15, 9]
    >>> a = [8,17,15,9,27,11,28,2,4]
    >>> triple_cut(a)
    >>> a
    [2, 4, 27, 11, 28, 8, 17, 15, 9]
    >>> a = [8,17,15,9,27,28,11,2,4]
    >>> triple_cut(a)
    >>> a
    [11, 2, 4, 27, 28, 8, 17, 15, 9]
    >>> a = [27,17,15,9,11,8,28]
    >>> triple_cut(a)
    [27, 17, 15, 9, 11, 8, 28]
    >>> a = [27,28]
    >>> triple_cut(a)
    >>> a
    [27, 28]
    '''
    # Find the index of JOKER1
    index_of_joker1 = deck_of_cards.index(JOKER1)
    # Find the index of JOKER2
    index_of_joker2 = deck_of_cards.index(JOKER2)
    # If JOKER1 comes before JOKER2 in the deck
    if index_of_joker1 < index_of_joker2:
        # Remove all the cards before JOKER1 and add them after JOKER2
        count = 0
        while count < index_of_joker1:
            removed = deck_of_cards.pop(0)
            deck_of_cards.insert(index_of_joker2, removed)
            count += 1
        # Remove all the cards after JOKER2 and add them before JOKER1 to
        # complete triple cut
        count = len(deck_of_cards)-1
        while index_of_joker2 < count:
            removed = deck_of_cards.pop()
            deck_of_cards.insert(0, removed)
            count -= 1
    # If JOKER2 comes before JOKER1 in the deck
    else:
        # Remove all the cards before JOKER2 and add them after JOKER1
        count = 0
        while count < index_of_joker2:
            removed = deck_of_cards.pop(0)
            deck_of_cards.insert(index_of_joker1, removed)
            count += 1
        # Remove all the cards after JOKER1 and add them before JOKER2 to
        # complete triple cut
        count = len(deck_of_cards)-1
        while index_of_joker1 < count:
            removed = deck_of_cards.pop()
            deck_of_cards.insert(0, removed)
            count -= 1


def insert_top_to_bottom(deck_of_cards):
    '''(list of int) -> NoneType
    REQ: The length of deck of cards must be greater than 0
    REQ: The length of deck of cards must be greater than or equal to the
    bottom card at the deck
    This function will analyze the bottom card of the deck, and move that many
    cards from the top of the deck to the bottom, inserting them just
    above the bottom card.
    >>> a = [1,2]
    >>> insert_top_to_bottom(a)
    >>> a
    [1, 2]
    >>> a = [1]
    >>> insert_top_to_bottom(a)
    >>> a
    [1]
    a = [11,26,23,6,8,7,9,7]
    >>> insert_top_to_bottom(a)
    >> a
    [11, 26, 23, 6, 8, 7, 9, 7]
    >>> a = [11,26,23,6,8,7,9,6]
    >>> insert_top_to_bottom(a)
    >>> a
    [9, 11, 26, 23, 6, 8, 7, 6]
    >>> a = [9,11,26,23,6,8,7,28]
    >>> insert_top_to_bottom(a)
    >>> a
    [9, 11, 26, 23, 6, 8, 7, 28]
    '''
    # Find the value of the card at the bottom of the deck
    last_value = deck_of_cards[len(deck_of_cards) - 1]
    # If the last card has value greater than or equal to the length of the
    # deck then don't change the deck
    if last_value >= (len(deck_of_cards)):
        pass
    # If last card is JOKER2 then use JOKER1 as number of cards
    elif last_value == JOKER2:
        last_value = JOKER1
        # Loop through the deck and move cards from the top of the deck to
        # just above the bottom card
        count = 0
        while count < (last_value):
            removed = deck_of_cards.pop(0)
            deck_of_cards.insert(len(deck_of_cards) - 1, removed)
            count += 1
    # If last card is not JOKER2
    else:
        # Loop through the deck and move cards from the top of the deck to
        # just above the bottom card
        count = 0
        while count < (last_value):
            removed = deck_of_cards.pop(0)
            deck_of_cards.insert(len(deck_of_cards) - 1, removed)
            count += 1


def get_card_at_top_index(deck_of_cards):
    '''(list of int) -> int
    REQ: The length of deck of cards must be greater than 0
    REQ: The value of the top card must be less than length of deck of cards
    This function will look at the top card and use that value as an index
    to return the card in the deck at that index. However, if the top card
    is JOKER2 then it will use JOKER1 as the index.
    >>> a = [3,5,9]
    get_card_at_top_index(a)
    >>> a = [28,27,3]
    get_card_at_top_index(a)
    >>> a = [28, 4, 7, 10, 13, 16, 19, 22, 25, 27, 3, 6, 9, 12, 15, 18, 21, 24,
    1, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_card_at_top_index(a)
    26
    '''
    # Get the value of the card at the top of the deck
    top_card = deck_of_cards[0]
    # If the top card is JOKER2 then use JOKER1 as the index to return the card
    # at index JOKER1
    if top_card == JOKER2:
        # If JOKER1 has value greater than or equal
        if JOKER1 >= (len(deck_of_cards)):
            return None
        card = deck_of_cards[JOKER1]
        return card
    # If the top card had value greater than or equal to the length of deck of
    # cards then return no value, as we can't get the value of card which
    # is out of index
    elif top_card >= (len(deck_of_cards)):
        return None
    # If top card is not JOKER2 then use that value as an index to return
    # the card at that index
    else:
        card = deck_of_cards[top_card]
        return card


def get_next_value(deck_of_cards):
    '''(list of int) -> int
    REQ: The length of deck of cards must be greater than 0
    This function will do all the five steps and complete a round by returning
    the next potential keystream value
    >>> a = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_value(a)
    11
    >>> get_next_value(a)
    9
    >>> get_next_value(a)
    23
    >>> get_next_value(a)
    7
    >>> get_next_value(a)
    10
    '''
    # Complete Step 1 by calling move_joker_1
    move_joker_1(deck_of_cards)
    # Complete Step 2 by calling move_joker_2
    move_joker_2(deck_of_cards)
    # Complete Step 3 by calling triple_cut
    triple_cut(deck_of_cards)
    # Complete Step 4 by calling insert_top_to_bottom
    insert_top_to_bottom(deck_of_cards)
    # Complete the final Step 5 by calling get_card_at_top_index
    value = get_card_at_top_index(deck_of_cards)
    return value


def get_next_keystream_value(deck_of_cards):
    '''(list of int) -> int
    REQ: The length of deck of cards must be greater than 0
    This function will complete round one of the algorithm and return any
    keystream value between 1 and 26
    >>> a = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(a)
    11
    >>> get_next_keystream_value(a)
    9
    >>> get_next_keystream_value(a)
    23
    >>> get_next_keystream_value(a)
    7
    >>> get_next_keystream_value(a)
    10
    >>> get_next_keystream_value(a)
    25
    >>> get_next_keystream_value(a)
    11
    >>> get_next_keystream_value(a)
    11
    >>> get_next_keystream_value(a)
    7
    >>> get_next_keystream_value(a)
    8
    >>> get_next_keystream_value(a)
    9
    >>> get_next_keystream_value(a)
    11
    >>> get_next_keystream_value(a)
    11
    '''
    # Get the next keystream value by calling get_next_value
    keystream_value = get_next_value(deck_of_cards)
    # We assume that we found JOKER1 or JOKER2 then we check to make sure if
    # we actually did find the jokers
    value_is_joker = True
    # If we indeed found any one of the jokers then keep looping till we
    # get a keystream value between 1 and 26
    while value_is_joker:
        if keystream_value == JOKER1 or keystream_value == JOKER2:
            keystream_value = get_next_value(deck_of_cards)
            return keystream_value
        # Otherwise if we didn't find the jokers initially then return the
        # next keystream value
        else:
            value_is_joker = False
            return keystream_value


def process_message(deck_of_cards, message, encrypt_decrypt):
    '''(list of int, str, str) -> str
    REQ: The length of deck of cards must be greater than 0
    REQ: The length of the message must be greater than 0
    REQ: The third parameter must be either equal to 'e' or 'd'
    This function will first determine if the message needs to be encrypted if
    'e' is entered or decrypted if 'd' entered. It will then generate a
    a new message that will either be encrypted or decrypted depending on
    what the user wants
    >>> a = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(a, "Hello!, How are you?", 'e')
    'SNISYGZHHZNJZU'
    >>> gg = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(a, "SNISYGZHHZNJZU", 'd')
    'HELLOHOWAREYOU'
    '''
    # First of all call clean_message to make sure we only have alphabets
    # that are uppercase
    message = clean_message(message)
    # Initialize an empty string
    changed_message = ""
    # Loop through every single letter in the message
    for letter in message:
        # Generate a keystream value by calling get_next_keystream_value
        keystream_value = get_next_keystream_value(deck_of_cards)
        # If the user would like to encrypt the message then call the function
        # encrypt_letter
        if encrypt_decrypt == 'e':
            changed_message += encrypt_letter(letter, keystream_value)
        # Otherwise if the user wants to decrypt the message then call
        # decrypt_letter
        elif encrypt_decrypt == 'd':
            changed_message += decrypt_letter(letter, keystream_value)
    return changed_message


def process_messages(deck_of_cards, list_of_messages, encrypt_decrypt):
    '''(list of int, list of str, str) -> list of str
    REQ: The length of deck of cards must be greater than 0
    REQ: The length of the list of messages must be greater than 0
    REQ: The third parameter must be either equal to 'e' or 'd'
    This function will first determine if the message needs to be encrypted if
    'e' is entered or decrypted if 'd' entered. It will then generate the
    list of messages that will either be encrypted or decrypted depending on
    what the user wants
    >>> a = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_messages(a, ["Hello!, How are you?", "I'm fine thanks", "Have
    a nice day"], 'e')
    ['SNISYGZHHZNJZU', 'GROCEWCXTKTP', 'FUHXZNYUGRHW']
    >>> a = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21, 24,
    27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_messages(a, ['SNISYGZHHZNJZU', 'GROCEWCXTKTP', 'FUHXZNYUGRHW']
    , 'd')
    ['HELLOHOWAREYOU', 'IMFINETHANKS', 'HAVEANICEDAY']
    '''
    # Initialize an empty list
    changed_list_of_msg = []
    # Loop through every single word in our list of string
    for word in list_of_messages:
        # Call the function, process_message in order to encrypt or decrypt
        # the list of string
        changed_word = process_message(deck_of_cards, word, encrypt_decrypt)
        # Append the encrypted or decrypted list of messages to our empty list
        changed_list_of_msg.append(changed_word)
    return changed_list_of_msg


def read_messages(any_file):
    '''(file open for reading) -> list of str
    REQ: Length of the file must be greater than 0
    REQ: One line can only contain a single message
    This function will read the contents of the file and return a list of
    string
    '''
    list_of_words = []
    # Read all the lines in the file
    all_lines = any_file.readlines()
    # For each line in the file
    for line in all_lines:
        # Strip each message removing trailing spaces before and after the
        # message
        message = line.strip()
        # Add each message to the empty list that we initialized at the start
        list_of_words.append(message)
    return list_of_words


def read_deck(any_file):
    '''(file open for reading) -> list of int
    REQ: The file must have at least one line which contains only integers
    REQ: Length of the file must be greater than 0
    This function will read the contents of the file and return a list of
    integers
    '''
    list_of_cards = []
    # Read all the lines in the file
    all_lines = any_file.readlines()
    # For each line in the file
    for index in all_lines:
        # Seperate each integer as a string and add it to our empty list
        list_of_cards += index.split()
    # Now we have all the cards in a list except each of them are of type(str)
    list_of_int = list_of_cards
    # Now loop through each card and convert it to integer from string
    for count in range(len(list_of_int)):
        list_of_int[count] = int(list_of_int[count])
    return list_of_int