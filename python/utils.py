"""
    utils.py

    Supplementary routines that are used across FTSpecViewer, such as
    the datetime module.
"""

from datetime import datetime
from PyQt5.QtCore import QDate
import h5py
import os
import socket
import ntpath
import ftclass
import numpy as np


def FTDateTime(datestring):
    # Takes the comment line from a QtFTM batch containing the date
    # and serializes a datetime object for use between QtFTM and the
    # Qt calendar widget
    datelist = datestring.split()[1:]         # Skip the comment flag
    datestring = " ".join(datelist)            # Reform the datestring
    return datetime.strptime(datestring, "%a %b %d %H:%M:%S %Y")


def Py2QtDateTime(datetime_obj):
    # Takes a python datetime object and serializes a QDate object.
    return QDate.fromString(datetime_obj.strftime("%Y-%m-%d"))


"""
    H5Py routines
    The data can be compressed and stored into a single HDF5 file, which
    ensures portability and hopefully means we can have copies of all of the
    FT data for offline processing, without encumbering our computers.

    File structure:

    db.h5
    +-- dr
    |   +--- dr_id    (group)
    +-- survey
    +-- scans         (group)
    |   +--- scan_id  (group)
    |        +--- FID (dataset)
    |        +--- FFT (dataset)
    +-- chirp
    +-- batch

    The parameters used for taking the data are stored as attributes to each
    respective group/dataset.

"""


def LoadDatabase(Database):
    """ Attempts to load a database with exception catching.
        If the database doesn't exist, raise an error.

        Returns the loaded database
    """
    try:
        DB = h5py.File(Database, "r+")
        return DB
    except IOError:
        print("Database does not exist.")


def AddDatabaseEntry(database, group, filepath):
    """ Used to add a file to a database. """
    scan_id = str(filepath.split("/")[-1].split(".")[0])
    if scan_id not in list(database[group].keys()) is True:
        entry_instance = database[group].create_group(str(scan_id))
        entry_instance.attrs["created"] = datetime.now().strftime(
            '%m/%d/%Y %H:%M:%S'
        )
        if group == "scan":
            # This case is for FIDs
            ft_obj = ftclass.FTData(filepath, fid=True)
            FID = entry_instance.create_dataset(
                "FID",
                data=ft_obj.fid,
                compression="gzip",
                compression_opts=9,
            )
            FFT = entry_instance.create_dataset(
                "FFT",
                data=ft_obj.spectrum,
                compression="gzip",
                compression_opts=9
            )
            for parameter in FTData.settings:
                FID.attrs[parameter] = FTData.settings[parameter]
        elif group == "surveys" is True:
            # For every other case
            ft_obj = ftclass.FTBatch(filepath, batch_type=group, peek=False)
            spectrum = entry_instance.create_dataset(
                "Spectrum",
                data=ft_obj.spectrum,
                compression="gzip",
                compression_opts=9
            )
            for parameter in FTBatch.settings:
                spectrum.attrs[parameter] = FTBatch.settings[paramter]
        elif group == "chirp":
            raise NotImplementedError("Chirp support not implemented yet.")
    database.attrs["modified"] = datetime.now().strftime('%m/%d/%Y %H:%M:%S')


def CreateDatabase(filepath):
    """ Function for initializing a HDF5 database for storing FTMW data. """
    with h5py.File(filepath, "w") as h5file:
        h5file.attrs["filename"] = filepath
        h5file.attrs["creation date"] = datetime.now().strftime(
            '%m/%d/%Y %H:%M:%S'
        )
        h5file.attrs["creator"] = socket.gethostname()
        h5file.attrs["HDF5 version"] = h5py.version.hdf5_version
        h5file.attrs["H5Py version"] = h5py.version.version

        for group in ["dr", "batch", "scans", "surveys", "chirp", "compilation"]:
            # Create all the "headers"
            h5file.create_group(group)
        h5file.close()


def CompressData(filedict, database_filepath, progress_obj=None):
    """
        Takes a Dictionary with the filepaths to scans/batchs organized as
        keys, and creates database entries for every one of them. This is
        designed to interface with the batch file reader, which already has
        all of this information.

        The check for whether or not the entry already exists is done within
        the AddDatabaseEntry function.
    """
    if os.path.isfile(database_filepath) is False:
        # If the database doesn't exist already, create it.
        CreateDatabase(database_filepath)
    totalitems = np.sum([len(filedict[group]) for group in filedict])
    counter = 0
    with h5py.File(database_filepath, "a") as h5file:
        for group in filedict:
            for entry in filedict[group]:
                AddDatabaseEntry(
                    h5file,
                    group,
                    entry
                )
                counter += 1
                if progress_obj is not None:
                    progress_obj.setValue(counter / totalitems * 100.)
        h5file.close()
