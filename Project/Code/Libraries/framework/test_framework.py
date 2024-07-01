# ------------------------------------------
# Build in modules
# ------------------------------------------
import os
import datetime
import logging
import time

# ------------------------------------------
# 3rd party modules (installation needed)
# ------------------------------------------
import pandas as pd

# ------------------------------------------
# custom modules
# ------------------------------------------
None


class FrameWork():
    '''
    Start logging
    Calc process time
    Read Config File
    '''

    # Initialize instance
    def __init__(self) -> None:
        self.config_dict = {}
        # Start time
        self.start_time = time.time()
        # Read config file
        self.read_config_file()
        #self.upgrade_config_file()

    # CONSTANTS
    LOGGING_MARKER = "FRAMEWORK:"
    INPUT_FOLDER_PATH = "Data/Input"
    INPUT_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', INPUT_FOLDER_PATH))
    OUTPUT_FOLDER_PATH = "Data/Output"
    OUTPUT_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', OUTPUT_FOLDER_PATH))
    CONFIG_FILE_PATH = r"Config/Config.xlsx"
    CONFIG_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', CONFIG_FILE_PATH))
    LOGS_FOLDER_PATH = r"Logs_Folder"
    LOGS_FOLDER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..', LOGS_FOLDER_PATH))

    def read_config_file(self) -> None:
        """
        Read config Excel file and create dictionary.
        Dictionary is accesible from FrameWork instance
        """
        # Read Config File
        df_config = pd.read_excel(self.CONFIG_FILE_PATH)
        # Assign values to dictionary
        for row in df_config.itertuples():
            self.config_dict[row.Asset] = row.Value


    def upgrade_config_file(self) -> None:
        """
        # Add calculation to config values specific for this project
        """
        # Add constant values to dictionary
        self.config_dict["OUTPUT_FOLDER_PATH"] = self.OUTPUT_FOLDER_PATH
        self.config_dict["INPUT_FOLDER_PATH"] = self.INPUT_FOLDER_PATH
        self.config_dict["input_file_path"] = os.path.abspath(
            os.path.join(self.INPUT_FOLDER_PATH, self.config_dict["input_file_name"]))
        self.config_dict["email_body_file_path"] = os.path.abspath(
            os.path.join(self.INPUT_FOLDER_PATH, self.config_dict["email_body_file_name"]))

    def start_logging(self) -> None:
        """
        Start logging session
        """
        # Calc log file name
        log_file_name = "Log_" + datetime.datetime.today().strftime("%d%m%Y_%H%M%S") + ".txt"
        # Calc Year and Month folder
        sub_folders = f"{datetime.datetime.today().strftime('%Y')}/{datetime.datetime.today().strftime('%m')}"
        # Calc full folder path, Main log folder + Year & month
        full_log_folder_path = os.path.join(self.LOGS_FOLDER_PATH, sub_folders)
        # Create folder if not exist
        if not os.path.exists(full_log_folder_path):
            os.makedirs(full_log_folder_path)
        # Calc full path to log file
        filename = os.path.join(full_log_folder_path, log_file_name)
        # Start logging
        logging.basicConfig(filename=filename,
                            level=logging.INFO,
                            format='%(levelname)s: %(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S',
                            force=True)


    def get_process_time(self) -> str:
        """
        Notify the user about end of work.
        Log end of work information in Log file
        Return the time of process duration
        """
        self.end_time = time.time()
        script_time = self.end_time - self.start_time
        mon, sec = divmod(script_time, 60)
        hr, mon = divmod(mon, 60)
        process_duration = '%d:%02d:%02d' % (hr, mon, sec)
        print(f"\n Process finished. Time: {process_duration}\n")
        logging.info(f"{self.LOGGING_MARKER} Time - {process_duration}")
        return process_duration



#Test config
if True:

    # Create instance of FrameWork
    framework_instance = FrameWork()
    # Read config file
    config_dict = framework_instance.config_dict

    print(config_dict["email_body_file_path"])
    print("Check")


