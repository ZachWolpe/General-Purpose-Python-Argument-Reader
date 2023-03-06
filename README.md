# General Purpose Python Argument Reader
---

An interface to instantiate a custom argument parser into any python script - to transform any python script into a dynamic cli.


## Example

The implementation relies on specifying parsing a list of `<class> argument` objects to an `argument builder`. The object `<class> argument`. For example, in the main python script one might add $3$ arguments:

```
if __name__=='__main__':
    # argument handler --------------++
    arguments = [
        argument('arg1', 'a', True),
        argument('arg2', 'b', True, 'default 2'),
        argument('arg3', 'c', False, True)
    ]
    
    ah = argument_handlr(arguments)
    arg1    = ah.args_dict['arg1']
    arg2    = ah.args_dict['arg2']
    arg3    = ah.args_dict['arg3']

    # alternative: USE WITH CAUSTION AS STATIC ANALYSIS WILL FAIL.
    # argument_handlr.add_to_globals()
    # argument handler --------------++
```

The `<class> argument` objects require $4$ properties on initialisation:
  
  - argument long name
  - argument short name
  - whether or not the argument takes parameters (or is simply a boolean switch)
  - the default argument value
  


Thereafter the python script can be executed as a `cli`:

```
clear; python example.py \
        --arg1 "input argument 1 using long  name" \
        -b     "input argument 2 using short name" \
        -c    // set arg3==True
```


---
author:         zach wolpe
email:          zach.wolpe@medibio.com.au
date:           06.03.23
---
