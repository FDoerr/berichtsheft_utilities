import os
import shutil
import datetime

'''
rename reports from: "Berichtsheft ddMMYY_ddMMYY" or "Notizen Berichtsheft ddMMYY_ddMMYY" to "KWUU_YY_MM_dd_Berichtsheft" or "KWUU_YY_MM_dd_Notizen_Berichtsheft" U is the calenderweek
string format codes: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
source_folder_path:str = 'unprocessed_reports'
target_folder_path:str = 'processed_reports'

def get_file_names():
    file_names: list[str] = os.listdir(source_folder_path)
    return file_names


def rename_files(file_names):
    for file_name in file_names:
        new_name = construct_new_name(file_name)
        print(new_name)
        #shutil.copyfile(f'{source_folder_path}/{file_name}', f'{target_folder_path}/{new_name}')


def construct_new_name(file_name:str):
    identifier =file_name[:-18] # e.g. NOtizen Berichtsheft  or Berichtsheft
    start_date: str = file_name[-17:-11]
    end_date: str = file_name[-10:-4]
    print(f'{identifier=}')
    print(f'{start_date=}')
    print(f'{end_date=}')    
    ...
    #extract date
    #convert date
    #return new_name


if __name__=='__main__':    
    file_names: list[str] = get_file_names()
    rename_files(file_names)