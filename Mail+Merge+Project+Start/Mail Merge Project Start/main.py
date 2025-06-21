
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_format = letter.read()
    for name in names:
        name = name.strip()
        new_letter = letter_format.replace("[name]",name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.docx", mode = "w") as letters:
            letters.write(new_letter)

