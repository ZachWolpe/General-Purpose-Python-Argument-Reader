from sys_args import *

if __name__=='__main__':
    # argument handler --------------++
    arguments = [
        argument('arg1', 'a', True),
        argument('arg2', 'b', True, 'default 2'),
        argument('arg3', 'c', False, False)
    ]
    
    ah = argument_handlr(arguments)
    arg1    = ah.args_dict['arg1']
    arg2    = ah.args_dict['arg2']
    arg3    = ah.args_dict['arg3']

    # alternative: USE WITH CAUSTION AS STATIC ANALYSIS WILL FAIL.
    # argument_handlr.add_to_globals()
    ah.print_configuration()
    # argument handler --------------++