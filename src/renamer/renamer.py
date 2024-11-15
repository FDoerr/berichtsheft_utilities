import os
import shutil
from datetime import datetime
import re #RegEx


'''
rename reports from: "Berichtsheft ddmmyy_ddmmyy.pdf" or "Notizen Berichtsheft ddmmyy_ddmmyy.txt" to "YYYY-KWUU_ddmm-ddmm_Notizen_Berichtsheft.txt" or "YYYY-KWUU_ddmm-ddmm_Berichtsheft.pdf" U is the calenderweek
string format codes: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
source_folder_path: str = 'unprocessed_reports'
target_folder_path: str = 'processed_reports'

def get_file_names() -> list[str]:
    #validate file names
    file_names: list[str] = os.listdir(source_folder_path)
    return file_names


def rename_files(file_names: list[str]) -> None:

    for file_name in file_names:
        try:
            new_name: str = construct_new_name(file_name)
            print(f'{file_name} -> {new_name}')
            shutil.copyfile(f'{source_folder_path}/{file_name}', f'{target_folder_path}/{new_name}')
        except ValueError as e:
            print(f'{file_name} {e}')
            continue


def construct_new_name(file_name: str) -> str:  

    identifier: str = file_name[:-18].replace(' ','_') # e.g. Notizen Berichtsheft  or Berichtsheft    
    
    start_date: str = file_name[-17:-11]
    new_start_date_str: str | None = convert_date(start_date, True)

    end_date: str = file_name[-10:-4] 
    new_end_date_str: str | None= convert_date(end_date)
    
    file_extension: str =  fetch_file_extension(file_name)      

    new_name: str = f'{new_start_date_str}-{new_end_date_str}_{identifier}{file_extension}'
    return new_name
    

def fetch_file_extension(file_name):
    pattern:re.Pattern = r"(\.\w+)$" # parenthesis group expressions, \. is "."  \w "word"-character, + one or more of the preceding token, $ end of string
    result = re.search(pattern, file_name)
    file_extension = result.group(1)
    return file_extension


def convert_date(old_date_str: str, is_start_date: bool|None = None) -> str | None:
    try:
        old_date_format: str = '%d%m%y'

        if is_start_date:
            new_date_format: str = '%Y-KW%U_%d%m'
        else: 
            new_date_format: str = '%d%m'
        
        old_date: datetime = datetime.strptime(old_date_str, old_date_format)
        new_date_str = datetime.strftime(old_date, new_date_format)
        return(new_date_str)
    except:
        raise ValueError('unexpected Name')


if __name__=='__main__':    
    file_names: list[str] = get_file_names()
    rename_files(file_names)