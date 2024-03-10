# Backup utils

I wanted something personnal to manage my backups and did not find anything that suited me well, so I decided to create this tool. Here are the features I want initially:

TODOs:
- [ ] Need to save info in the databases and merge info to save on the databases at every important step
- [ ] CLI arguments to already start with a drive added
- [ ] Be able to know if a directory has changed, save previous state in metadata file
- [ ] Set up a master drive and slave drives for each folder I want to backup, and keep that stored in the backup general metadata.
- [ ] Store latest backup sync date in backup metadata.
- [ ] Manage what do I do if I split a folder into two
- [ ] Be able to delete drives?
- [ ] Keep information about the whole folder structure in the metadata for all drives.
- [ ] Keep information about folder sizes in the folder structure in the metadata for all drives.
- [ ] Depending on the importance you give to the data, automatically determine how to backup the data and the user just connects the drives and the tool does the rest.

## Start with command line tool
Which runs interactively, clears the screen each time and shows which are the available options.
Utilities
Screen, commands, output: that's what I should see
- [X] --list-drives list known drives
- [X] --add-drive, adds drive to the list of known drives
- [X] --add-folder, adds folder to the list of known folders
- [X] --list-folders, list known folders (Do TODOs to finish this)
- [ ] --set-master sets a master drive to a top level folder which does not have a master drive
- [ ] --set-slave sets a slave drive to a top level folder (needs to veriry conflict with master drive or if was already set)
- [ ] --check-update-needed, checks if a top level folder needs to be updated on some drive (verify if there was no wrong update as well)
- [ ] --update, updates a top level folder on a drive

## What can I currently do?
- Add drives, but they do not update each other
- Add folders, but they do not update each other

## Comparison tool
- [ ] 1st just compare if the files are the same
- [ ] Be able to see if I moved or renamed files
- [ ] Generalize this to the greatest group in some kind of visulization
- [ ] Compare the files only locally in their respective folders for fast comparison?
