# #100days of code - day 24 - Mail file generator

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", "r") as template_file:
    invitation = template_file.read()

with open("./Input/Names/invited_names.txt", "r") as file_names:
    list_of_invited = file_names.readlines()

    for x in range(0, len(list_of_invited)):
        list_of_invited[x] = list_of_invited[x].replace("\n", "")  # można by zrobić to też z wykorzystaniem strip()

        invitation_file_name = "letter_for_" + list_of_invited[x]
        with open(f"./Output/ReadyToSend/{invitation_file_name}.txt", "w") as invitation_file:
            invitation_file.write(invitation.replace(PLACEHOLDER, list_of_invited[x]))
