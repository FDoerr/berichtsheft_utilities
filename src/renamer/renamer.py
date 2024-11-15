import os
import shutil
from datetime import datetime

'''
rename reports from: "Berichtsheft ddMMYY_ddMMYY" or "Notizen Berichtsheft ddMMYY_ddMMYY" to "KWUU_YY_MM_dd_Berichtsheft" or "KWUU_YY_MM_dd_Notizen_Berichtsheft" U is the calenderweek
string format codes: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
source_folder_path: str = 'unprocessed_reports'
target_folder_path: str = 'processed_reports'

def get_file_names():
    #validate file names
    file_names: list[str] = os.listdir(source_folder_path)
    return file_names


def rename_files(file_names):
    for file_name in file_names:
        new_name = construct_new_name(file_name)
        print(new_name)
        #shutil.copyfile(f'{source_folder_path}/{file_name}', f'{target_folder_path}/{new_name}')


def construct_new_name(file_name: str):
    identifier: str =file_name[:-18].replace(' ','_') # e.g. Notizen Berichtsheft  or Berichtsheft    
    
    start_date: str = file_name[-17:-11]
    new_start_date_str = convert_date(start_date, True)

    end_date: str = file_name[-10:-4] 
    new_end_date_str= convert_date(end_date)

    new_name = f'{new_start_date_str}-{new_end_date_str}_{identifier}'
    return new_name
    


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
        print('Unexpected Name')   


if __name__=='__main__':    
    file_names: list[str] = get_file_names()
    rename_files(file_names)