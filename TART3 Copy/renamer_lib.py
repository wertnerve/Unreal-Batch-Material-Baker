import logger as logger
import os
import shutil






def get_logger(print_to_screen = False):
    """
    Uses the logger.py module to create a logger


    Args:
        print_to_screen: for printing to screen as well as file
    """


    return logger.initialize_logger(print_to_screen)




def get_renamed_file_path(logger, existing_name, string_to_find, string_to_replace,
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


    '''
    REMINDERS


    This function should only take in strings and return a string.  
    No file renaming/copying/moving should happen here


    Make sure to support string_to_find being an array of multiple strings!  
        Hint: you may need to check its type...
    '''


    logger.info(f"gen_renamed_file_path called. Locating {string_to_find} in {existing_name} and replacing with {string_to_replace}")
    file_name = os.path.basename(existing_name)




 
    if string_to_find in existing_name:
       
        replaced_file_name = file_name.replace(string_to_find, string_to_replace) #add a try except and an if here
        new_file_name = prefix+replaced_file_name+suffix
        logger.info(f"File_name {file_name } contains {string_to_find}. New File Name: {new_file_name}")
    else:
         
         new_file_name = prefix+file_name+suffix
   
    logger.info(f"New File name after adding suffix/replacing string: {new_file_name}")
    renamed_file_path = existing_name.replace(file_name, new_file_name)
    logger.info(f"Returning Replaced file_name : {renamed_file_path}")
    return renamed_file_path






def get_files_with_extension(logger, folder_path, extension):
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


    logger.info(f"Get_Files_With_Extension function called. Locating {extension} files in {folder_path}")
    files_with_extension = []
    try:
        logger.info(f"Checking files in {folder_path}, total files detected: {len(os.listdir(folder_path))}")
        for file in os.listdir(folder_path):
           
            _, file_extension = os.path.splitext(file) #using _ as a placeholder since we dont need to look at the file name, just the extension
            #logger.info(f"Current file: {_}, Current Extension: {file_extension}")
            if str(extension) == str(file_extension[1:]):


                logger.info(f'{file} contains extension {extension} - appending to list of returned files')
                files_with_extension.append(file)


        logger.info(f'{folder_path} has been scanned, returning {len(files_with_extension)} files with {extension} extension')
        return files_with_extension
       
    except Exception as error:


            logger.error(f'Error encountered in get_files_with_extension: {error} \n Returning empty list')
            return files_with_extension




def rename_file(logger, existing_name, new_name, copy=False):
    """
    Renames a file if it exists
    By default, should move the file from its original path to its new path--
    removing the old file
    If copy is set to True, duplicate the file to the new path


    Args:
        logger: logger instance
        existing_name: full filepath a file that should already exist
        new_name: full filepath for new name
        copy_mode: copy instead of rename
    """


    '''
    REMINDERS


    Copy files using shutil.copy
    make sure to import it at the top of the file
    '''
    #need shutil
   


   
      # Get the base folder path where files are located
    try:
         folder_path = os.path.join(os.getcwd(), 'testing_files')


         logger.info(f"Rename_File Called. Replacing {existing_name} with {new_name}")


    # Construct full paths
         existing_file_path = os.path.join(folder_path, existing_name)
         new_file_path = os.path.join(folder_path, new_name)
         if os.path.isfile(existing_file_path):
            shutil.copy(existing_file_path, new_file_path)
            if not copy:
                logger.info(f"Copy is set to False, removing {existing_name}")
                os.remove(existing_file_path)
         else: logger.info(f"{existing_file_path} does not exist. Exiting Rename File Function.")
    except Exception as e:
         
         logger.info(f"Error in Rename File Function: {e}")




def rename_files_in_folder(logger, folder_path, extension, string_to_find,
                           string_to_replace, prefix, suffix, copy=False):
    """
    Renames all files in a folder with a given extension
    This should operate only on files with the provided extension
    Every instance of string_to_find in the filepath should be replaced
    with string_to_replace
    Prefix should be added to the front of the file name
    Suffix should be added to the end of the file name


    Args:
        logger: logger instance
        folder_path: the path to the folder the renamed files are in
        extension: the extension of the files you'd like renamed
        string_to_find: the string in the filename you'd like to replace
        string_to_replace: the string you'd like to replace it with
        prefix: a string to insert at the beginning of the file path
        suffix: a string to append to the end of the file path
        copy: whether to rename/move the file or duplicate/copy it
    """


    '''
    REMINDERS
    #
    This function should:
        - Find all files in a folder that use a certain extension
            - Use get_files_with_extension for this
        - *For each* file...
            - Determine its new file path
                - Use get_renamed_file_path for this
            - Rename or copy the file to the new path
                - Use rename_file for this
        - Use the logger instance to document the process of the program
    '''
    logger.info(f'Rename_Files_in_folder Function Called. Renaming files with extension {extension} in {folder_path} containing following string(s) :{string_to_find}')
     
    try:
            files_to_rename = get_files_with_extension(logger, folder_path, extension)


            for file in files_to_rename:


                if string_to_find == '':
                     logger.info("No replacement string detected. Adding suffix to file name")
                     new_file_path = get_renamed_file_path(logger, file, '','',prefix, suffix)
                     rename_file(logger, file, new_file_path, copy)


                elif type(string_to_find == tuple()):
                     logger.info("Tuple detected instead of string in string_to_find argument- parsing tuple for matching substring")
                     for string in string_to_find:
                         
                        test_string = str(string)
                        #  logger.info(f"Searching for {test_string} in {file}")
                        if test_string in file:
                        #    logger.info(f'{file} contains extension {extension} and {string} - creating new file path')
                              new_file_path = get_renamed_file_path(logger,file, string, string_to_replace, prefix, suffix)
                              rename_file(logger, file, new_file_path, copy)
                         


                else:
                     #if string_to_find in file:
                        #logger.info(f'{file} contains extension {extension} and {string_to_find} - creating new file path')
                        new_file_path = get_renamed_file_path(logger, file, string_to_find, string_to_replace, prefix, suffix)
                        rename_file(logger, file, new_file_path, copy)
               
               
               
    except Exception as error:


            logger.error(f'Error encountered in rename_files_in_folder: {error}')
           
    logger.info("Renaming Complete.")


def main():
    # Logger
    logger = get_logger(True)
    logger.info('Logger Initiated')


    #   Here are some examples of different logger messages
    logger.warning('This would be a logger warning')
    logger.error('This would be a logger error!!')
    logger.critical('This would be a critical log')




if __name__ == '__main__':
    main()