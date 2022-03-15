def greet(name):
    print('Hello ' + name)


def name_input():
    name1 = (input('Please provide a name: '))
    return name1


greet(name_input())

def language_input():
    language = str(input("Choose the from the following : English, Telugu, Hindi, Spanish \n"))
    if language == "English":
        name2 = str(input('Please give your name in the chosen language \n'))
        print('Hello' + name2)
    elif language == 'Spanish':
        name2 = str(input('Como te llamas \n'))
        print('Hola ' + name2)
    elif language == 'Hindi':
        name2 = str(input('Aap ka naam kya hain \n'))
        print('Namaskar '+ name2)
    elif language == 'Telugu':
        name2 = str(input('Mee perenti \n'))
        print('Namaskaram '+ name2)
    else:
        print("Select language from the above four option given")

language_input()