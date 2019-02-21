"""
A simple Python Program to find the Hash of a given File
Hash Supported:
* SHA-1

* SHA-256

* SHA-512

* MD5

* Author: Eleam Emmanuel Maduabuchi

* Date: 20th February 2019.

Thsi program takes two inputs, the hash type and file to hash
an it returns the correponding hash of the file based on the hash!.
"""

import hashlib
import os


def check_valid_hashing_input(hash_to_use):
    """
        Checks if the Input is a recognised hashing type used in the program
    [Hash_to_use is a parameter passed in the command line and used to
    specify the kind of hash to use]

    Arguments:
        hash_to_use {string} -- [the has type to use, sha1,
         sha256, sha512, md5]
    """
    status = True
    while status:
        if not hash_to_use:
            hash_to_use = input("Enter a valid supported Hash: ")
        else:
            if hash_to_use == "sha1" or hash_to_use == "md5" or \
             hash_to_use == "sha256" or hash_to_use == "sha512":
                status = False
            else:
                print_report()
                hash_to_use = input("Enter a valid supported Hash: ")
    return hash_to_use


def hash_corresponding_file(hash_type, filename):
    """"
        This function returns the SHA-1 hash
        of the file passed into it

        hash_type is the specified has for creating the file hash
        filename is the file to be hashed

    Arguments:
        hash_type {String} -- the hash specified to be used
        filename {string} -- The file to be hashed

    Returns:
        string -- Returns the hash string in hex
    """

    # make a hash object
    if hash_type == "sha1":
        h = hashlib.sha1()
    elif hash_type == "md5":
        h = hashlib.md5()
    elif hash_type == "sha256":
        h = hashlib.sha256()
    elif hash_type == "sha512":
        h = hashlib.sha512()

    file_check = True
    while file_check:
        if filename == "":
            print("i am here")
            print("File to be hashed cannot be empty!\n")
            filename = input("Enter a file with the correct path to check"
                             "the Hash: ")
        else:
            if os.path.isfile(filename):
                file_check = False
            elif os.path.isdir(filename):
                print("Directories or Folders are not supported!\n")
                filename = input("Enter a file with the correct path to check"
                                 "the Hash: ")
            else:
                print("File name is either wrong or doesnt exist in the"
                      "specified folder!\n")
                filename = input("Enter a file with the correct path to"
                                 "check the Hash: ")

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def print_report():
    print("Input not supported, enter a valid Hash\n\
                  * sha1\n\
                  * md5\n\
                  * sha256\n\
                  * sha512\n")


if __name__ == '__main__':
    print("Welcome to a File Hashing Implementation in Python.\n\
      Hashing currently supported:\n\
      * sha1\n\
      * md5\n\
      * sha256\n\
      * sha512\n")
    input_for_hash_to_use = input("Enter a valid supported Hash: ")
    hash_to_use = check_valid_hashing_input(input_for_hash_to_use)
    file_name_to_hash = input("Enter a file with the correct path to check"
                              "the Hash: ")
    message = hash_corresponding_file(hash_to_use, file_name_to_hash)
    print("The valid '{}' Hash is {}".format(hash_to_use, message))
