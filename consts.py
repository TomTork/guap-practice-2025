__h = ['h', 'help', '--help']
__f = ['f', 'file', '--file']
__s = ['s', 'search', '--search']
__d = ['d', 'destination', '--destination']
__q = ['q', 'exit']
__help = f'''Commands:
          ({'/'.join(__h)}) — Show this message;
          ({'/'.join(__f)} <path-to-file>) — Set file for search;
          ({'/'.join(__s)}) — Word or sentence to search;
          ({'/'.join(__d)}) <(t/terminal)|(<path-to-file>)>) — Save the result in;
          (run) — Run the program;
          ({'/'.join(__q)}) — Exit the program;'''
__run = True

# == ERRORS ==
def unknown(command):
    return f'Unknown command {command}. Use: ——> help'


def invalid(command):
    return f'Invalid format from command {command}. Use ——> help'


def primary(error):
    return f'Error: {error}'

# == SUCCESS ==
__path_to_file = 'Path to file saved. Use ——> -F for watch path\nUse ——> -V for watch value'
__w_or_s = 'Sentence has been successfully saved. Use ——> -S for watch'
__destination = 'Destination path successfully saved. Use ——> -D for watch'