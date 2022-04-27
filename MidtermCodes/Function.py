def functionOne(Name, MathGrade, EnglishGrade, ScienceGrade):
    Name = str(Name)
    answer = MathGrade+EnglishGrade+ScienceGrade
    average = answer / 3

    print(f'{Name}: Math = {MathGrade}, English = {EnglishGrade}, Science = {ScienceGrade}, Average = {average}')

functionOne('Ben',85,85,85)
functionOne('Joshua',90,90,90)
functionOne('Solanor',95,93,92)
