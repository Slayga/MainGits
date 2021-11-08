imports = {"Menu": "import os", "clear_screen": "import os", 
           "linear_search": "from typing import Union"}


Menu = '''class Menu:    
    def __init__(self):
        """
        Inits the options menu
        """
        self.options = list()
        self.exit_opt = None
    
    def add_option(self, option):
        """
        Called to add a new option to the menu.
        
        Args: [option], [A option that will describe the choice]
        """
        self.options.append(option.capitalize())
    
    def clear_option(self):
        """Clears the menu options from memory.
        Used for example when calling a function with a menu creation
        inside it, use Menu().clear_option() before return to clear the array
        """        
        self.options = list()
    
    def exit_option(self, exit_opt:str, custom:str=None):
        """Called to add a custom exit option to the menu
        
        Args:
            exit_opt (str): [Adds a custom exit option to the menu]
            custom (str): [Adds a custom exit text to the menu]
        """        
        self.exit_opt = exit_opt
        
        if custom is not None:
            self.exit_text = custom
        else:
            self.exit_text = "Exit program"
        
    def cls(self):
        """Called to clear the console screen manually. 
        Gets called automatically by get_input()
        """        
        os.system("cls" if os.name == "nt" else "clear")
    
    def get_input(self, custom_print:str=None, cls:bool=True, 
                    exit_opt_print:bool=True):
        """
        Displays the menu with options numbered starting with 1. And prompts
        the user for input. Repeats until a valid option is supplied.
        Uses os system to clear console.
        
        Args:
            custom_print (str) [Prints a custom str before the options
                                , default is None]
            cls (bool): [If the console shall clear screen, default is True]
            exit_opt_print (bool): [Gives the user option to stop currently 
                            existing exit opt to  be disabled temporarily, 
                            without deleting it. If its true exit_opt will 
                            work, default is True]
            
        Returns: the number the user entered.
                    if custom exit option is provided, -1 is returned when its
                    entered
        """
        
        while True:
            # Clears the console.
            if cls:
                self.cls()
            # If a custom print shall be printed before the options.
            if custom_print is not None:
                print(">>", custom_print)
                print("-"*30)
            
            for index, opt in enumerate(self.options, start=1):
                print(">> {}) {}".format(index, opt))
            if self.exit_opt is not None and exit_opt_print:
                print(">> {}) {}".format(self.exit_opt, self.exit_text))
            
            userInput = input(">> ")
            
            if userInput.isdigit():
                userInput = int(userInput)
                if 1 <= userInput <= len(self.options):
                    if cls:
                        self.cls()
                    return userInput
            
            # If custom exit_opt is added
            elif (self.exit_opt is not None and not userInput.isdigit() 
                and exit_opt_print):
                if self.exit_opt == userInput:
                    return -1'''
INIT_Menu = '''MENU_VAR = Menu()'''
CALL_Menu = '''MENU_VAR.get_input()'''

clear_screen = '''def cls():
    """Calls system from os and clears the console screen, checks if os is 
    Windows or Linux as their clear message is different.
    
    Returns: void
    """
    # Checks if the os name is 'nt'(Windows)
    os.system("cls" if os.name == "nt" else "clear")
    '''
CALL_clear_screen = '''cls()'''

# def bin_search(list_, term, låg, hög) -> int:
#     mitt = (låg+hög)//2
#     if list_[mitt] == term:
#         return (mitt, term)
#     elif list_[mitt] > term:
#         return bin_search(list_, term, låg, mitt-1)
#     elif list_[mitt] < term:
#         return bin_search(list_, term, mitt+1, hög)
#     else:
#         return -1 

linear_search = '''def lin_search(array:Union[list, dict, tuple, str]
                , search:Union[str, int, float, bool]
                , strict_search:bool=False
                , case_sensitive:bool=False
                , key_and_value:bool=False
                , key_bool:bool=False, inverted:bool=False
                ) -> Union[int, list, dict]:
    
    """A linear search algorithm designed for broad uses.
    Accepts multiple types of iterables, but also search words can be of
    different types.(see arg: search, types)

    Args:
        array (Union[list, dict, tuple, str]): 
        [An iterable object that contains some type of value]
        
        search (Union[str, int, float, bool]): 
        [A search term, can be empty. 
        If type is bool, strict_search will be True automatically
        And array cant be string if search is a bool >> raises TypeError]
        
        -------Optional Arguments-------
        
        strict_search (bool, optional): 
        [Value must be exact match, if the array is a string and a strict 
        match is found a list of the index from 0 to end of the string will
        be returned]. 
        Defaults to False.
        
        case_sensitive (bool, optional): 
        [Makes the search case sensitive]. 
        Defaults to False.
        
        key_and_value (bool, optional): 
        [If array is dict, and bool is true, return matching keys and values].
        Defaults to False.
        
        key_bool (bool, optional): 
        [If array is dict, and bool is true, return matching keys
        , _bool is used to avoid naming interferences].
        Defaults to False.
        
        inverted (bool, optional): 
        [Inverts the search and returns all non matching values
        If strict_search is True a list will be returned!]. 
        Defaults to False.
    
    Returns:
        Union[int, list, dict]:
        [int: int of match, only when strict match is True
        list: int of match(ing) index(s) 
        dict: If (key_bool or key_and_value) is True key1 is 'Matching keys'.
        And if key_and_value is True key2 is 'Matching values'.
        If (key_bool or key_and_value) are False key1 is 'Matching values'.]
        And the values in the dictionary are integers.
    """ 
    # Make sure the array is iterable...
    if not hasattr(array, "__iter__"):
        raise TypeError("Give array has no attribute __iter__!")
    
    # Special case for bool, where you cant compare a strings iter with a bool
    if isinstance(search, bool):
        # Stops user from comparing a string with a bool
        if not isinstance(array, str):
            strict_search = True
        else:
            raise TypeError("Cant search for bool(s) in a string!")
    
    # Iter over all the values and make them lowercase if they are strings. 
    # This operation only lowercase strings in an iter and doesn't modify the
    # iter in any other way.
    if not case_sensitive:
        if isinstance(search, str):
            # Makes all letters lowercase, to avoid case-sensitive.
            search = search.lower()
            
            # Iter over all values and makes them lowercase.
            if isinstance(array, list):
                for index, value in enumerate(array):
                    if isinstance(value, str):
                        # Lowercase if the value is a string otherwise it 
                        # would conflict with integer and booleans.
                        array[index] = value.lower()
            
            # Iter over a dict and lowercase both keys and values.
            # To not get RuntimeError temporarily variables are made.
            elif isinstance(array, dict):
                dict_keys = list(array.keys())
                dict_values = list(array.values())
                
                for index, (key, value) in enumerate(zip(dict_keys
                                                        , dict_values)):
                    if isinstance(key, str):
                        dict_keys[index] = key.lower()
                    if isinstance(value, str):
                        dict_values[index] = value.lower()
                
                # Makes the new array with all strings lowercase.
                array = dict(zip(dict_keys, dict_values))
            
            # Lowercase the str
            elif isinstance(array, str):
                array = array.lower()
            
            elif isinstance(array, tuple):
                # Makes a mutable list, that will become immutable(tuple)
                new_tuple = list()
                for value in array:
                    if isinstance(value, str):
                        new_tuple.append(value.lower())
                    else:
                        new_tuple.append(value)
    
    if not isinstance(array, dict) and not strict_search:
        # Creates empty list to append matching indexes to.
        match = list()
    
    if isinstance(array, dict) and not strict_search:
        # Creates empty dict to add matching indexes to.
        match = dict()
        
        if not key_bool:
            # While key_bool is False. A key for matching values gets created.
            match["Matching Values"] = list()
            # Also a bool for value just being searched for. 
            # If key_and_value is True value_bool gets deleted
            value_bool = True
        
        if key_and_value or key_bool:
            match["Matching Keys"] = list()
            # Unasign value_bool to not make it conflict.
            value_bool = None
    
    if strict_search:
        if isinstance(array, str):
            # Strict search will return one int!
            # Unless the array is a str then a list for all indexes are 
            # returned
            match = list()
        else:
            # Assigns -1 to match which means no current strict match. 
            # Done to avoid 0 being returned which can be confuse with a 
            # match at index 0 but infact there were no matches found.
            match = -1
    
    # Linear search without strict matching. For list, tuples and strings
    if not isinstance(array, dict) and not strict_search:
        if not isinstance(array, str):
            for index, value in enumerate(array):
                # Make sure the value is iterable
                if hasattr(value, "__iter__"):
                    if isinstance(search, str):
                        if search in value:
                            match.append(index)
                else:
                    if search == value:
                        match.append(index)
        else:
            if search in array:
                index = array.index(search)-1
                for _ in range(len(search)):
                    index = index + 1
                    match.append(index)
    
    # Linear search without strict matching. For dicts
    elif isinstance(array, dict) and not strict_search:
        for index, (key, value) in enumerate(array.items()):
            if value_bool or key_and_value:
                # Make sure the value is iterable
                if hasattr(value, "__iter__"):
                    if search in value:
                        match["Matching Values"].append(index)
                    else:
                        if search == value:
                            match["Matching Values"].append(index)
            
            if key_and_value or key_bool:
                if hasattr(value, "__iter__"):
                    if search in key:
                        match["Matching Keys"].append(index)
                else:
                    if search == value:
                        match["Matching Keys"].append(index)
    
    # Linear search with strict matching. For all iter the function accepts.
    elif strict_search:
        if isinstance(array, str):
            if search == array:
                # Enumerates over all the characters
                for index, _ in enumerate(array):
                    match.append(index)
        
        elif not isinstance(array, dict):
            for index, value in enumerate(array):
                if search == value:
                    match = index
        
        elif isinstance(array, dict):
            for index, value in enumerate(array.values()):
                if search == value:
                    match = index
    
    if inverted:
        # If strict_search is True, 'match' will be an integer. Which is not 
        # iterable, so the match gets converted to a list
        if strict_search:
            match = [match]
        # Enumerate over the given array and compares with the matches
        # Then if the index from the array isn't in matches it gets appended 
        # to inverted matches
        if not isinstance(array, dict):
            temp_match = list()
            
            for i, _ in enumerate(array):
                if i not in match:
                    temp_match.append(i)
            match = temp_match
        
        elif isinstance(array, dict):
            temp_match = dict()
            
            if key_bool or key_and_value:
                temp_match["Matching Keys"] = list()
                for i, _ in enumerate(array.keys()):
                    if i not in match["Matching Keys"]:
                        temp_match["Matching Keys"].append(i)
            
            elif value_bool or key_and_value:
                temp_match["Matching Values"] = list()
                for i, _ in enumerate(array.values()):
                    if i not in match["Matching Values"]:
                        temp_match["Matching Values"].append(i)
            match = temp_match
    
    return match


    pass'''
CALL_linear_search = '''SEARCH_VAR = lin_search(array=register, 
                        search=input(">> Search in register: "))'''