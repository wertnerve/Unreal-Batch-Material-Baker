import os
import logging
import shutil

class BatchRenamer:
    def __init__(self, 
                 filepath          = None,
                 copy_files        = False,
                 filetypes         = None,
                 strings_to_find   = None,
                 string_to_replace = '',
                 prefix            = None,
                 suffix            = None):
        self.filepath          = filepath
        self.copy_files        = copy_files
        self.filetypes         = filetypes
        self.strings_to_find   = strings_to_find
        self.string_to_replace = string_to_replace
        self.prefix            = prefix
        self.suffix            = suffix

        self.initialize_logger()


    def initialize_logger(self, print_to_screen = False):
        """
        Creates a logger

        Args:
            print_to_screen: for printing to screen as well as file
        """

        ###############
        # Basic Setup #
        ###############
        app_title = 'Test'
        version_number = '1.0.0'
        # get the path the script was run from, storing with forward slashes
        source_path = os.path.dirname(os.path.realpath(__file__))
        # create a log filepath
        logfile_name = f'{app_title}.log'
        logfile = os.path.join(source_path, logfile_name)

        # tell the user where the log file is
        print(f'Logfile is {logfile}')

        # more initialization
        self.logger = logging.getLogger(f'{app_title} Logger')
        self.logger.setLevel(logging.INFO)
        
        ###############################
        # Formatter and Handler Setup #
        ###############################
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.INFO)
        # formatting information we want (time, self.logger name, version, etc.)
        formatter = logging.Formatter(f'%(asctime)s - %(name)s {version_number} - '
                                    '%(levelname)s - %(message)s')
        # setting the log file format
        file_handler.setFormatter(formatter)
        # clean up old handlers
        self.logger.handlers.clear()

        # add handler
        self.logger.addHandler(file_handler)

        # allowing to print to screen
        if print_to_screen:
            # create a new "stream handler" for logging/printing to screen
            console = logging.StreamHandler()
            self.logger.addHandler(console)
            # setting the print log format
            console.setFormatter(formatter)

        self.logger.info('Logger Initiated')


    def get_renamed_file_path(self, existing_name, string_to_find, string_to_replace, 
                            prefix, suffix):
        """
        Returns the target file path given an existing file name and 
        string operations

        Args:
            existing_name: the existing file's name
            string_to_find: a string to find and replace in the existing filename
            string_to_replace: the string you'd like to replace it with
            prefix: a string to insert at the beginning of the file path
            suffix: a string to append to the end of the file path
        """

        self.logger.info(f"gen_renamed_file_path called. Locating {string_to_find} in {existing_name} and replacing with {string_to_replace}")
        file_name = os.path.basename(existing_name)


  
        if string_to_find in existing_name:
        
            replaced_file_name = file_name.replace(string_to_find, string_to_replace) #add a try except and an if here
            new_file_name = prefix+replaced_file_name+suffix
            self.logger.info(f"File_name {file_name } contains {string_to_find}. New File Name: {new_file_name}")

        else:
         
             new_file_name = prefix+file_name+suffix
    
        self.logger.info(f"New File name after adding suffix/replacing string: {new_file_name}")
        renamed_file_path = existing_name.replace(file_name, new_file_name)
        self.logger.info(f"Returning Replaced file_name : {renamed_file_path}")
        return renamed_file_path

    def get_files_with_extension(self, folder_path, extension):
        """
        Returns a collection of files in a given folder with an extension that 
        matches the provided extension

        Args:
            folder_path: The path of the folder whose files you'd like to search
            extension: The extension of files you'd like to include in the return
        """

        '''
        REMINDERS

        This function should only take in strings and return an array
        No file renaming/copying/moving should happen here

        Make sure to catch and handle errors if the folder doesn't exist!
        '''
        self.logger.info(f"Get_Files_With_Extension function called. Locating {extension} files in {folder_path}")
        files_with_extension = []
        try:
             self.logger.info(f"Checking files in {folder_path}, total files detected: {len(os.listdir(folder_path))}")
             for file in os.listdir(folder_path):
            
                 _, file_extension = os.path.splitext(file) #using _ as a placeholder since we dont need to look at the file name, just the extension
                 #logger.info(f"Current file: {_}, Current Extension: {file_extension}")
                 if str(extension) == str(file_extension[1:]):

                    self.logger.info(f'{file} contains extension {extension} - appending to list of returned files')
                    files_with_extension.append(file)

             self.logger.info(f'{folder_path} has been scanned, returning {len(files_with_extension)} files with {extension} extension')
             return files_with_extension
        
        except Exception as error:

            self.logger.error(f'Error encountered in get_files_with_extension: {error} \n Returning empty list')
            return files_with_extension

    def rename_file(self, existing_name, new_name, copy=False):
        """
        Renames a file if it exists
        By default, should move the file from its original path to its new path--
        removing the old file
        If copy is set to True, duplicate the file to the new path

        Args:
            existing_name: full filepath a file that should already exist
            new_name: full filepath for new name
            copy_mode: copy instead of rename
        """

        try:

            folder_path = os.path.join(os.getcwd(), 'testing_files')

            self.logger.info(f"Rename_File Called. Replacing {existing_name} with {new_name}")

    # Construct full paths
            existing_file_path = os.path.join(folder_path, existing_name)
            new_file_path = os.path.join(folder_path, new_name)
            if os.path.isfile(existing_file_path):
                shutil.copy(existing_file_path, new_file_path)
                if not copy:
                    self.logger.info(f"Copy is set to False, removing {existing_name}")
                    os.remove(existing_file_path)
            else: self.logger.info(f"{existing_file_path} does not exist. Exiting Rename File Function.")

        except Exception as e:
         
             self.logger.info(f"Error in Rename File Function: {e}")


    def rename_files_in_folder(self, folder_path, extension, string_to_find,
                            string_to_replace, prefix, suffix, copy=False):
        """
        Renames all files in a folder with a given extension
        This should operate only on files with the provided extension
        Every instance of string_to_find in the filepath should be replaced
        with string_to_replace
        Prefix should be added to the front of the file name
        Suffix should be added to the end of the file name

        Args:
            folder_path: the path to the folder the renamed files are in
            extension: the extension of the files you'd like renamed
            string_to_find: the string in the filename you'd like to replace
            string_to_replace: the string you'd like to replace it with
            prefix: a string to insert at the beginning of the file path
            suffix: a string to append to the end of the file path
            copy: whether to rename/move the file or duplicate/copy it
        """
        self.logger.info(f'Renaming files with extension {extension} in {folder_path} containing following string(s) :{string_to_find}')
     
        try:

            files_to_rename = self.get_files_with_extension(folder_path, extension)

            for file in files_to_rename:

                if string_to_find == '':
                     self.logger.info("No replacement string detected. Adding suffix to file name")
                     new_file_path = self.get_renamed_file_path(file, '','',prefix, suffix)
                     self.rename_file(file, new_file_path, copy) 

                elif type(string_to_find == tuple()):
                     self.logger.info("Tuple detected instead of string in string_to_find argument- parsing tuple for matching substring")
                     for string in string_to_find:
                          
                        test_string = str(string)
                        #  logger.info(f"Searching for {test_string} in {file}")
                        if test_string in file:
                        #    logger.info(f'{file} contains extension {extension} and {string} - creating new file path')
                              new_file_path = self.get_renamed_file_path(file, string, string_to_replace, prefix, suffix)
                              self.rename_file(file, new_file_path, copy) 
                          

                else:
                     #if string_to_find in file:
                        #logger.info(f'{file} contains extension {extension} and {string_to_find} - creating new file path')
                        new_file_path = self.get_renamed_file_path(file, string_to_find, string_to_replace, prefix, suffix)
                        self.rename_file(file, new_file_path, copy) 
                
                
                
        except Exception as error:

            self.logger.error(f'Error encountered in rename_files_in_folder: {error}')
            
        self.logger.info("Renaming Complete.")