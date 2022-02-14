"""
Name: Gabriel Engberg
Date: 05-04-2021
Info:
A program that let you create a register over movies. 
"""
from inl_classes_GabrielEngberg import Menu
from random import randint


class Film:
    """
    A class that handles information about a movie
    """    
    def __init__(self, name:str, genre:list, year:str, 
                length:int, timestamp:int=int()):
        """[Constructor of the class Film]

        Args:
            name (str): [Name of the movie]
            genre (list): [A list of genres the movie belongs to]
            year (str): [What year the movie was released]
            length (int): [How long the movie is in minutes]
            timestamp (int, optional): [How long the movie has been watched].
                                        Defaults to int().
        """        
        self.name = name
        self.genre = genre
        self.year = year
        self.length = length
        self.timestamp = timestamp
        self.watched = False
    
    @property
    def name(self):
        return self.__name
    
    @property
    def genre(self):
        return self.__genre
    
    @property
    def length(self):
        return self.__length
    
    @property
    def year(self):
        return self.__year
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @name.setter
    def name(self, value):
        ### Error checking | Similar concept on all setters. ###
        # "if value:", checks if the arg is empty
        # Source: Docs Python 3, Truth Value Testing
        if not isinstance(value, str):
            if isinstance(value, (int, float) and value):
                self.__name = str(value)
            else:
                if not value:
                    raise ValueError("Value can't be empty")
                else:
                    raise TypeError("Invalid value, must be str, int/float")
        # Remove the spaces to make sure name isn't just spaces
        elif value.strip():
            self.__name = value
        else:
            raise ValueError("Name can't consist of spaces or empty!")
    
    @genre.setter
    def genre(self, value):
        if isinstance(value, list):
            # Iterate over the given lists values, if a value is not a string
            # or is empty a ValueError will be raised!
            for index, v in enumerate(value):
                if not isinstance(v, str):
                    raise ValueError(f"Value at index[{index}] is not a str!")
                elif not v.strip():
                    raise ValueError(f"Value at index[{index}] is empty!")
            else:
                self.__genre = value
        elif not value:
            raise ValueError("List can't be empty!")
        else:
            raise TypeError("Genre is expected to be a list of strings!")
    
    @length.setter
    def length(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self.__length = value
            else:
                raise ValueError("Invalid value, must be greater than 0")
    
    @year.setter
    def year(self, value):
        if isinstance(value, (int, float)):
            if value >= 1888:
                self.__year = value
            else:
                raise ValueError("Invalid value, first movie aired 1888!")
        
    @timestamp.setter
    def timestamp(self, value):
        if value:    
            if isinstance(value, (int, float)):
                if value > 0:
                    self.__timestamp = value
                    
                    # Checks if the movie has been watched till the end.
                    if self.timestamp >= self.length:
                        self.watched = True
                    elif 0 < self.timestamp < self.length:
                        # Temporary to know if the movie is being watched.
                        self.watched = None
                    else:
                        self.watched = False
                else:
                    raise ValueError("Invalid value, time must be positive")
            else:
                raise TypeError("Timestamp should be an int of minutes")
        else:
            self.__timestamp = int()
    
    def reg_time(self, value):
        """[Register time that has been watched to the movie]

        Args:
            value ([int, float]): [Takes in the amount of minutes watched]
        """        
        self.timestamp = value
    
    def get_info(self) -> dict:
        """[Gives information about the movie object.
            {"Name": self.name, ...}
            If the movie is being seen it will include the timestamp
            at index 4. 
            {"Name": self.name, .., .., .., "Current Time": self.timestamp}
            And if the movie is seen it will include a boolean at index 4]

        Returns:
            dict: [Returns a dictionary of all instances in the object]
        """        
        if self.timestamp and self.watched is None:
            return {"Name": self.name, "Genre": self.genre, 
                    "Length (minutes)": self.length, "Year": self.year, 
                    "Current Time (minutes)": self.timestamp}
        elif self.watched:
            return {"Name": self.name, "Genre": self.genre, 
                    "Length (minutes)": self.length, "Year": self.year,
                    "Watched": self.watched}
        else:
            return {"Name": self.name, "Genre": self.genre, 
                    "Length (minutes)": self.length, "Year": self.year}

def create_movie() -> list:
    """A function that creates a list of information for a movie.

    Returns:
        list: [A list consisting of name[0], year[1], genre[2], length[3]]
    """    
    
    # Create an empty array.
    temp = list()
    
    while True:
        print(">> Current movie: {}".format(temp))
        print(">> Please enter a movie name:")
        temp_input = input(">> ")
        
        if temp_input.strip():
            temp.append(temp_input)
            break
        else:
            print(">> Invalid value, can't be empty")
            input(">> Press enter to try again...")
            Menu().cls()
    
    # cls() clears the console 
    Menu().cls()
    
    # Makes an empty array at index 1, to stop IndexError.
    temp.append(list())
    while True:
        print(">> Current movie: {}".format(temp))
        print(">> Please enter one or more genres:")
        print(">> Input '#' when satisfied with new genres")
        print(">> Current genres: {}".format(temp[1]))
        print("-"*30)
        print(">> Input a genre:")
        temp_input = input(">> ")
        
        # Checks if user want to prompt out and list is not empty.
        if temp_input.strip() == "#" and temp[1]:
            Menu().cls()
            break
        elif temp_input.strip() and temp_input.strip() != "#":
            Menu().cls()
            temp[1].append(temp_input)
        else:
            print(">> Invalid value, can't be empty")
            input(">> Press enter to try again...")
            Menu().cls()
    
    while True:
        print(">> Current movie: {}".format(temp))
        print(">> Please enter the release year of the movie:")
        temp_input = input(">> ")
        if temp_input.isdigit():
            if int(temp_input) >= 1888:
                temp.append(int(temp_input))
                Menu().cls()
                break
            else:
                print(">> Invalid value, must be greater than 1888")
                input(">> Press enter to try again...")
                Menu().cls()
        else:
            Menu().cls()
            print(">> Please enter an integer")
    
    while True:
        print(">> Current movie: {}".format(temp))
        print(">> Please enter the length of the movie (minutes):")
        temp_input = input(">> ")
        if temp_input.isdigit():
            if int(temp_input) > 0:
                temp.append(int(temp_input))
                Menu().cls()
                break
            else:
                print(">> Invalid value, must be greater than 0")
                input(">> Press enter to try again...")
                Menu().cls()
        else:
            Menu().cls()
            print(">> Please enter an integer greater than 0")
    
    
    return temp

def search_movie(a_list:list, return_index=False) -> int:
    """[A custom function that searches for a movies different values.]

    Args:
        a_list (list): [The given list that will be searched]
        return_index (bool, optional): [Instead of printing matches it
                        returns the first matching index.]. Defaults to False.

    Returns:
        int: [If return_index is True, it will return the index as an integer
                -1 will be returned if user exits, -2 will be returned if 
                nothing is found. else if the return_index is False it returns
                void.]
    """    
    while True:
        Menu().cls()
        print("="*30)
        print(">> Search after a movie:")
        print("-"*30)
        print(">> Name")
        print(">> Release year")
        print(">> Genres")
        print(">> Time length")
        print("-"*30)
        print(">> #) Return")
        print("="*30)
        
        search = input(">> ")
        
        if not return_index:
            # Create a empty list to store the matches in if the bool is False
            matches = list()
        
        if search.strip() == "#":
            if return_index:
                return -1
            else:
                return
        # Linear algorithm that enumerates over the list each objects(obj)
        for index, obj in enumerate(a_list):
            # For each obj it calls get_info() and gets a dictionary returned.
            for v in obj.get_info().values():
                
                if isinstance(v, (str, int, float)):
                    if str(v).lower().strip() == search.lower().strip():
                        if return_index:
                            return index
                        else:
                            matches.append(("{}, {}".format(obj.name, 
                                                            obj.year)))
                
                # Takes care of the genres that are stored in a list
                elif isinstance(v, list):
                    for genre in obj.genre:
                        if search.lower().strip() == genre.lower().strip():
                            if return_index:
                                return index
                            else:
                                matches.append(("{}, {}".format(obj.name, 
                                                                obj.year)))
                                # To stop it from matching multiple times.
                                break
        else:
            if return_index:
                return -2
            else:
                Menu().cls()
                print("="*30)
                print(">> Total amount of matches:", len(matches))
                print("-"*30)
                for index, match in enumerate(matches, start=1):
                    print(">>", match)
                    if index < len(matches):
                        print("-"*30)
                if matches:
                    print("="*30)
                input(">> ")

# Creates an empty list for the movies and series
films, series = list(), list()

# Main menu, creation
m = Menu()
m.exit_option("#")
m_opt = ["Show all movies or series", 
        "Register watch time for a movie or series",
        "Search after a movie or series", "Add a movie or a series",
        "Edit a movie or series", "Choose a random movie or series to watch"]
for opt in m_opt: 
    m.add_option(opt)
# Deletes opt & m_opt from memory
del opt, m_opt

# Movie Or Series menu
mos = Menu()
mos.add_option("Movie")
mos.add_option("Series")
mos.exit_option("#", custom="Return")

# Movie Options menu
mo = Menu()
mo.add_option("Name")
mo.add_option("Genres")
mo.add_option("Year")
mo.add_option("Length")
mo.exit_option("#")

# 'Main program start' #

# Forces user to add at least one object to the list
if not films and not series:
    mos_input = mos.get_input(custom_print="Create register of _____:",
                                exit_opt_print=False)
    if mos_input == 1:
        v = create_movie()
        films.append(Film(v[0], v[1], v[2], v[3]))
    elif mos_input == 2:
        pass

while True:
    m_input = m.get_input(custom_print="Main menu")
    
    if m_input == 1:
        mos_input = mos.get_input(custom_print="Print all _____")
        
        if mos_input == 1:
            mos.cls()
            
            for index_1, obj_1 in enumerate(films, start=1):
                print(">> Movie id: {}".format(index_1))
                # Iterate over the dict returned when get_info() is called
                for key, value in obj_1.get_info().items():
                    
                    # Handles list of genres in the movie obj
                    if isinstance(value, list):
                        print(">> {})".format(key),end=" ")
                        for index, var in enumerate(value, start=1):
                            # Prints ',' until the last index
                            if index < len(value):
                                print(var, end=", ")
                            # Prints '\n' at the last genre
                            else:
                                print(var, end="\n")
                    # Handles rest of the values that are not a list
                    else:
                        print(">> {}) {}".format(key, value))
                if index < len(films):
                    print("")
            print("="*30)
            input(">> Press enter to return to the main menu...")
            
        elif mos_input == 2:
            for o in series:
                pass
    elif m_input == 2:
        while True:
            mos_input = mos.get_input(custom_print="Add timestamp to a _____")
            
            if mos_input == 1:
                while True:
                    index = search_movie(films, return_index=True)
                    
                    if index >= 0:
                        obj = films[index]
                    elif index == -2:
                        print(">> No matching results found!")
                        break
                    elif index == -1:
                        break
                    
                    # Index is returned as -1 if user exits
                    while -2 != index != -1:
                        print("="*30)
                        print(">> Please enter current time on the movie.")
                        time = input(">> ")
                        
                        if time.isdigit():
                            if int(time) > 0:
                                obj.timestamp = int(time)
                                mos.cls()
                                print(">> Timestamp changed...")
                                input(">> Press enter to return...")
                                break
                            else:
                                print(">> Invalid value, must be greater than"
                                        "0")
                        else:
                            print(">> Invalid value, must be a number")
                
            elif mos_input == 2:
                pass
            elif mos_input == -1:
                break    
    elif m_input == 3:
        while True:
            mos_input = mos.get_input(custom_print="Search for a _____")
            
            if mos_input == 1:
                # Calls a function that searches for a movie. Returns void
                search_movie(films)
            elif mos_input == 2:
                pass
            elif mos_input == -1:
                break
    elif m_input == 4:
        while True:
            mos_input = mos.get_input(custom_print="Add a new _____")
                        
            if mos_input == 1:
                # Calls a function that create and return a list of info.
                v = create_movie()
                # Appends the object with the list of information
                films.append(Film(v[0], v[1], v[2], v[3]))
                # Deletes v from memory
                del v
            elif mos_input == 2:
                pass
            elif mos_input == -1:
                break
    elif m_input == 5:
        while True:
            mos_input = mos.get_input(custom_print="Edit a _____")
            
            if mos_input == 1:
                while True:
                    index = search_movie(films, return_index=True)
                    
                    while True:
                        if index >= 0:
                            mo_input = mo.get_input(custom_print="Choose what "
                                                    "to edit")
                            
                            if mo_input == 1:
                                obj = films[index]
                                while True:
                                    print(">> Enter new name:")
                                    temp = input(">> ")
                                    mos.cls()
                                    while True:
                                        print(">>", temp)
                                        print("="*30)
                                        print(">> Are you satisfied with the new "
                                                "name: y/n")
                                        yn = input(">> ")
                                        if yn.strip().lower() == "y":
                                            obj.name = temp
                                            # To break out of the next loop
                                            yn = True
                                            break
                                        elif yn.strip().lower() == "n":
                                            yn = False
                                            break
                                    if isinstance(yn, bool) and yn is True:
                                        breaker = False
                                        break
                            
                            elif mo_input == 2:
                                obj = films[index]
                                temp_list = list()
                                
                                while True:
                                    mo.cls()
                                    print(">> Enter new genre(s):")
                                    print(">> When you are satisfied with genres "
                                            "input '#' to continue:")
                                    print(">> Current new list of genres "
                                            "{}".format(temp_list))
                                    print("-"*30)
                                    temp = input(">> ")
                                    if temp.strip() != "#" and temp.strip() != "":
                                        temp_list.append(temp)
                                    
                                    if temp.strip() == "#":
                                        if temp_list:
                                            obj.genre = temp_list
                                            break
                                        else:
                                            print(">> Genre list empty")
                                            input(">> ")
                                            mo.cls()
                            
                            elif mo_input == 3:
                                obj = films[index]
                                while True:
                                    print(">> Enter new release year:")
                                    temp = input(">> ")
                                    while True:
                                        print(">>", temp)
                                        print("="*30)
                                        print(">> Are you satisfied with the new "
                                                "release year: y/n")
                                        yn = input(">> ")
                                        if yn.strip().lower() == "y":
                                            if temp.isdigit():
                                                obj.year = int(temp)
                                                # To break out of the next loop
                                                yn = True
                                                break
                                            else:
                                                print(">> Invalid value, must be "
                                                        "a number")
                                        elif yn.strip().lower() == "n":
                                            yn = False
                                            break
                                    if isinstance(yn, bool) and yn is True:
                                        breaker = False
                                        break
                            
                            elif mo_input == 4:
                                obj = films[index]
                                while True:
                                    print(">> Enter new length in minutes:")
                                    temp = input(">> ")
                                    while True:
                                        print(">>", temp)
                                        print("="*30)
                                        print(">> Are you satisfied with the new "
                                                "length: y/n")
                                        yn = input(">> ")
                                        if yn.strip().lower() == "y":
                                            if temp.isdigit():
                                                obj.length = int(temp)
                                                # To break out of the next loop
                                                yn = True
                                                break
                                            else:
                                                print(">> Invalid value, must be "
                                                        "a number")
                                        elif yn.strip().lower() == "n":
                                            yn = False
                                            break
                                    if isinstance(yn, bool) and yn is True:
                                        breaker = False
                                        break
                        
                            elif mo_input == -1:
                                breaker = True
                                break
                        elif index == -1:
                            break
                        elif index == -2:
                            mo.cls()
                            print(">> No matching results was found")
                            input(">> ")
                            break
                    if breaker:
                        break
                
            elif mos_input == 2:
                pass
            elif mos_input == -1:
                break
    elif m_input == 6:
        while True:
            mos_input = mos.get_input(custom_print="Watch a random: _____")
            
            if mos_input == 1:
                # Picks a random index between 0 and the end of the list
                rand_int = randint(0, len(films)-1)
                print(">> Your random movie to watch is: \n>> {}, {}".format(
                    films[rand_int].name, films[rand_int].year))
                print("-"*30)
                input(">> Press enter to continue...")
            elif mos_input == 2:
                pass
            elif mos_input == -1:
                break
    elif m_input == -1:
        print(">> Quiting program...")
        break
