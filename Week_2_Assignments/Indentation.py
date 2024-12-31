#Recommended

if condition:
    do_something()

#Not Recommended

if condition:
    do_something()
    do_something_else()

#Indentation Must not be more than two 

#python
if condition1:
    if condition2:
        handle_case()

#Not Recommended:

if condition1:
    if condition2:
        if condition3:
            if condition4:
                handle_case()