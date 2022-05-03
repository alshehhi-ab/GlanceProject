
# datacontrol.py

# Class that controls the generation of files

import os
import pickle
from datetime import datetime, date, time

import sana


# 1 GENERATE FILES IF THEY DO NOT EXIST

# 2 READ AND WRITE FILES

# 3 Provide Control Functions
    # Import Calendar Files

class DataControl:

    def __init__(self):
        """ Constructor for Controller """
        self.main_dir = os.getcwd()        # Sets working directory

        # Check if data files directory (/Data) exists
        if os.path.exists(os.path.join(self.main_dir, "Data")):
            self.data_dir = os.path.join(self.main_dir, "Data")

        # Create a directory for data files if it does not exist
        else:
            os.mkdir(os.path.join(self.main_dir, "Data"))
            self.data_dir = os.path.join(self.main_dir, "Data")

        # Check for sana data files
        if os.path.exists(os.path.join(self.data_dir, "SanaData")):
            self.sana_dir = os.path.join(self.data_dir, "SanaData")

        # Create a directory for sana datafiles if they do not exist
        else:
            os.mkdir(os.path.join(self.data_dir, "SanaData"))
            self.sana_dir = os.path.join(self.data_dir, "SanaData")

        # Creates a list of all available SanaDataFiles
        self.lst_sanas = os.listdir(self.sana_dir)

    def read_sdf_path(self, filepath):
        """ Reads a given sanadata file, and returns a Sana Object
        :param filepath: path to sanadata file
        :return: Sana object (data of one calendar year)
        """

        with open(filepath, "rb") as f:
            sana_out = pickle.load(f)
        return sana_out

    def read_sdf(self, year_in):
        """ finds, reads, and returns a sanadata file from a provided year
        :param year_in: year number.
        :return: sana object of year
        """

        # generate proper path to year data file.
        fname = str(year_in) + ".dat"
        fpath = os.path.join(self.sana_dir, fname)

        # Return value from read_sdf_path
        return self.read_sdf_path(fpath)

    def write_sdf(self, sana_in):
        """ dumps calendar year (sana) into sana data file
        :param sana_in: sana object to be stored into file
        :return: None
        """

        # Generate filename:
        fname = sana_in.year_id + ".dat"

        # Find equivalent data path
        fpath = os.path.join(self.sana_dir, fname)

        # Pickle sana object into file
        with open(fpath, "wb") as f:
            pickle.dump(sana_in, f)

