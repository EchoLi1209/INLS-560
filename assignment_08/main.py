import sys

# make program repeat
while True:

# get user input for files
    file_variable = input('''
    What file would you like to search for?:
    a) Kpop-songs file
    b) Jpop-songs file
    x) to Exit
    ''').strip().lower()

    # process user input
    if file_variable == 'x':
        sys.exit()
    elif file_variable == 'a':
         file_variable = 'Kpop-songs.csv'
    elif file_variable == 'b':
         file_variable = 'Jpop-songs.csv'
    else:
        print('Invalid options. Please enter a, b, or x.')
        continue

    # enter a search term
    search_variable = input(f'Enter the search term for {file_variable} file:')
    search_variable = search_variable.title() # make it so that user can enter lower-case term

    def find(file_variable, search_variable):
        with open(file_variable , 'r',encoding='utf-8') as file:
            content = file.read()
        
        if search_variable in content:

            print(f'Your search item {search_variable} exists in the {file_variable} file!')
            see_entries = input('Would you like to see the entries?(y or n)?')
            
            if see_entries.lower() == 'y':
                print(f'Here are all of the entries with the term {search_variable}:')
                with open(file_variable,'r',encoding='utf-8') as file:
                    for line in file:
                        if search_variable in line:
                            print(line.strip())
            
            elif see_entries.lower == 'n':
                print('Goodbye!')
                sys.exit()
            
            else:
                print('Invalid option. Please enter y or n.')
        
        else:
            print(f'{search_variable} does not exist in {file_variable}.')
        
    find(file_variable, search_variable)



