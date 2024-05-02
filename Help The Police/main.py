import pickle
import sys

people = 'Enter the path'
numbers1= 'Enter the path'
numbers2='Enter the path'
numbers3='Enter the path'

def main():
    argument = sys.argv[1]
    files = []
    choice = 1
    while choice != 2:
        display_menu()
        print()
        choice = int(input('Enter choice: '))
        if choice == 1:
            file_path = input('Enter a filename (include full path): ')
            try:
                open(file_path)
            except:
                print('Error: There was a problem with at least one of the files.')
                return
            print()
            files.append(file_path)

        if choice == 2:
            if not files:
                print('Error: There was a problem with at least one of the files.')
                return
            final_set = cross_reference(files)
            suspects = map_numbers_to_names(final_set, argument)
            display_suspects(suspects)


def display_menu():
    print('1. Add file')
    print('2. Calculate')

def cross_reference(files):
    interaction_set = None
    counter = 1
    for file in files:
        file_path = open(file, 'r')
        set_name = f'number_set_{counter}'
        locals()[set_name] = set()
        current_set = locals()[set_name]
        counter = counter + 1

        for line in file_path:
            current_set.add(line.strip())

        file_path.close()

        if interaction_set is None:
            interaction_set = current_set
        else:
            interaction_set = interaction_set.intersection(current_set)
    return interaction_set

def map_numbers_to_names(numbers,filename):
    names = []
    input_file = open(filename, 'rb')
    people_details = pickle.load(input_file)
    input_file.close()
    for number in numbers:
        temporary = str(number)
        found_user = False
        for key, value in people_details.items():
            if temporary == key:
                names.append(value)
                found_user = True
                break
        if not found_user:
            unknown_user = 'Unknown (' + temporary + ')'
            names.append(unknown_user)
    return names


def display_suspects(names):
    print('The following persons was present on all crime scenes:')
    print('------------------------------------------------------')
    if not names:
        print('No matches')
    else:
        for name in names:
            print(name)

if __name__ == '__main__':
    main()