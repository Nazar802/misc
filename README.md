# duplicate
# This utility is not yet finalized! Use carefully! 

Command line utility used for finding and removing duplicate files.
Iterates through a directory and calculates files' checksums. If two or more files in the same subdirectory have similar checksums, the script then uses sha256 to confirm that the files are actually duplicate. If the hashes are also the same then those files (apart from original) are listed as duplicates. Then the user is asked if they want to delete those files.

Usage:
python duplicate_finder.py <directory>

  You also need mysql server running to be able to run duplicate_finder.
