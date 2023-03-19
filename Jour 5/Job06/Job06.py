def notes_ecole(notes):
    notes_arrondies = []

    for note in notes:
        if note >= 40:
            
            multiple_de_5 = (note // 5 + 1) * 5

            if multiple_de_5 - note < 3:
                notes_arrondies.append(multiple_de_5)
            else:
                notes_arrondies.append(note)
        else:
            notes_arrondies.append(note)

    return notes_arrondies

notes = [30, 38, 42, 57, 72, 83, 82, 97]
notes_arrondies = notes_ecole(notes)
print("Notes arrondies:", notes_arrondies)
