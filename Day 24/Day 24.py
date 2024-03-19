PLACEHOLDER = "[name]"

with open("Names/names.txt", mode="r") as names:
    names = names.readlines()
    

with open("Letters/unfinished_letter.txt", mode="r") as unf_letter:
    letter_contents = unf_letter.read()
    
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Completed Letters/letter_for_{stripped_name}.txt", mode="w") as finished_letter:
            finished_letter.write(new_letter)

        
       
