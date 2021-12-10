"""
Name: Gabriel Engberg
Date: 23/4-2021
Info: A program that let you create a register from premade components. 
Custom functions from another file?
Writes the register to a runable py file...
Use GUI for easier use.
"""

from os import path as os_path
from inl_classes_GabrielEngberg import *
# from codeblocks import *

class _IO_Handling:    
    def __init__(self, path:str):
        self.path = path
    
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, value):
        if isinstance(value, str):
            if value:
                if not value.endswith(".py"):
                    # Add .py extension, even if it endswith .txt, .exe...
                    value += ".py"
                self.__path = value
            else:
                raise ValueError("Value is empty")
        else:
            raise TypeError("Path is not a string")
    
    @property
    def contents(self):
        self.__update_contents()
        return self.__contents

    def __update_contents(self):
        # Checks if the file exists and if not it creates a empty file
        # and immediately close it.
        if not os_path.isfile(self.path):
            open(self.path, "a").close()
        
        # Opens the file in read and store all lines in self._contents
        with open(self.path, "r+")as fr:
            self.__contents = fr.readlines()
        
        if DEBUG: # Additional info for when debbuging code..
            raw_print = [l.replace("\n", "\\n") for l in self.__contents]
            for line in raw_print:
                print(line)
    
    def write_to_file_(self, content:str, line:int, indent:int):
        """Writes code to a file by calling read_from_fie_ and changing
        the given list of all lines from the file.

        Args:
            content ([str]): [What content to write to the file]
            line ([int]): [Where it should be written]
            indent ([int]): [Is it a indent of an iteration or selection 
            (amount of indents)]
        """
        stripped_content = self.pretty_print()
        cls()
        
        # Gets the longest line from all the lines
        max_length = 0
        for line in stripped_content:
            if len(line) > max_length:
                max_length = len(line)
        
        # print_example = "|<Line_Number>| <Code On Line>"
        
        # 
        # spacing = 
        # |<Line_Number>| <Code On Line> ""*spacing |Indent|
        
        # print("|{}| {}".format(line_prefix+str(index), line.replace("\n", "")))
    
        # print_example = "|<Line_Number>| <Code On Line>"
        
        # spacing = 
        
        # print(print_example, " "*spacing, )
    
        # input()

        # print_lc = "|<Line_Number>| <Code On Line>"
        # print_example = print_lc + " "*spacing + "|Indent|"
        
        # print(print_example)
        # print("-"*(spacing-len(print_lc)))
        # line_number = int()
        # len(str(max(line_number)))
        
        # code_on_line = str()
        # max(len(code_on_line))
        
        # len(str(max(indent)))

        # """
        # >>> |<Line_Number>| <Code On Line>      |<Indent>|
        # >>> -------------------------------------------
        # >>> | 0| from config import lin_search	|0|
        # """

        # >>> |<Line_Number>| <Code On Line> |<Indent>|
        # >>> -------------------------------------------
        # >>> | 0| from config import lin_search |0|
        # >>> | 1|						         |0|
        # >>> | 2| while True:				     |1|
        # >>> | 3|     #do stuff				 |1|
        # >>> | 4|     #					     |1|
        # >>> | 5|     #					     |1|
        # >>> | 6|     #do#				    	 |1|
        # >>> | 7|     #print#			    	 |1|
        # >>> | 8|     #print#			    	 |1|
        # >>> |09|     #print##			    	 |1|
        # >>> |10|     #print#			    	 |1|
        # >>> |11|     #for i in range(#  ):	 |1|
        # >>> |12|         #print#			     |2|
        # >>> |13|		#print			         |2|
        # >>> |14|     #newline##			     |1|
        # >>> |15|     ...	  			    	 |1|
        # >>> |16| while True:			    	 |0|
        # >>> |17|     ... 				    	 |1|
        # >>> |18| 	  break				         |1|

        ln_max = len(str(len(stripped_content)))
        
        col_max = int()
        
        for l in stripped_content:
            if len(str(l)) > col_max:
                col_max = len(str(l))
        
        line_indents = list()
        for line in stripped_content:
            # Strips the spaces to the left in the beginning of the line.
            # Until a character that isn't a space.
            # Then you calculate the difference from original line and the list.
            line_indents.append((len(line)-len(line.lstrip()))//4)
        
        max_indent_char = len(str(max(line_indents)))
        
        
        print_lc = "|<Line_Number>| <Code On Line>"
        if max_length - len(print_lc) > 0:
            spacing = max_length - len(print_lc)
        else:
            spacing = 4     
        
        print_example = print_lc + " "*spacing + "|Indent|"
        print(print_example)
        for index, line in enumerate(stripped_content):
            cur_ln = " "*(ln_max-len(str(index)))+str(index)
            if max_indent_char-line_indents[index] > 0:
                ind_spac = max_indent_char-line_indents[index]
            else:
                ind_spac = 1
            cur_ind = " "*ind_spac+str(line_indents[index])
            spacing = max_length - len(str(line))
            print(f"|{cur_ln}| {line} " + " "*spacing + f"|{cur_ind}|")
        
        print(max_length)
        print(spacing)
        input()
    def pretty_print(self) -> list:
        self.pretty = self.contents 
        # # Iter over all lines in self._contents and replace "\n" to ""
        for index, line in enumerate(self.pretty):
            if line.endswith("\n"):
                self.pretty[index] = line.replace("\n", "")
                            
        return self.pretty
        

def main():
    x = _IO_Handling("example.py")
    mm = Menu()
    mm.add_option("Write to file")
    mm.add_option("Read file contents")
    mm.exit_option("#")
    
    while True:
        choice = mm.get_input()
        
        if choice == 1:
            x.write_to_file_(content="", line=0, indent=0)
        
        elif choice == 2:
            for line in x.pretty_print():
                print(line)
            
            input()
        elif choice == -1:
            break


if __name__ == '__main__':
    DEBUG = False
    main()