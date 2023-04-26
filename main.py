with open("./Input/Names/invited_names.txt",mode="r") as invited_names:
    names=invited_names.readlines()

names=[i.split('\n', 1)[0] for i in names]

with open("./Input/Letters/starting_letter.txt","r") as starting_letter:
    contents=starting_letter.read()

for i in names:
    with open(f"./Output/ReadyToSend/{i}.txt",mode="w") as output_file:
        output_file.write(contents.replace('[name]',i)) 



