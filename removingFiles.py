# importing the required modules
import os
import shutil
import time

# main function
def main():

	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# u can specify the path of the directory to delete
	path = "/PATH_TO_DELETE"

	# specify the days
	days = 30

	# converting days to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# iterating over each and every folder and file in the path
		# gets the list of files and folders present in the path, including subfolders
		# os.walk(path) - it will return a generator containing folders, files, and subfolders.
		for root_folder, folders, files in os.walk(path):
				#If the result is greater than the desired days of the user, then check whether it is a file
				#or folder. If it is a file, use the os.remove(path) else use the shutil.rmtree() method.
				# comparing the days eg. if the files are more than 30 days old 
			if seconds >= get_file_or_folder_age(root_folder):
				# if creation time of the root folder is greater than the specific time/days 
				# remove the root folder
				
				remove_folder(root_folder)
				deleted_folders_count += 1 # incrementing count

				# breaking after removing the root_folder
				break

			else:

				# checking folder from the folders in the root_folder
				for folder in folders:
					#Get the path of the file or folder by joining both the current path and file/folder name 
					# using the method os.path.join().
					# folder path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the days 
					if seconds >= get_file_or_folder_age(folder_path):

						# invoking the remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the days
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 # incrementing count

		else:

			# if the path is not a directory
			# comparing with the days
			if seconds >= get_file_or_folder_age(path):

				# invoking the file
				
				remove_file(path)
				deleted_files_count += 1 # incrementing count

	else:
		#If the path doesn’t exist, print not found message.
		# file/folder is not found
		# f in print (formatted string) -it is a way to format your string that is more readable and fast.
		print(f'"{path}" is not found')
		deleted_files_count += 1 # incrementing count

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):
	
	# Delete an entire directory tree along with folders and file recursively using shutil.rmtree() method
	# Python’s not operator allows you to invert the truth value of Boolean expressions 
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file by os.remove(path)
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


# The method ctime() converts a time expressed in seconds 
# since the epoch to a string representing local time. 
# If secs is not provided or None, the current time as returned by time() is used
def get_file_or_folder_age(path):
	# Get the ctime from the os.stat(path) method using the attribute st_ctime.
	# getting ctime of the file/folder
	# time will be in seconds
	# ctime  is creation time of folder
	#  eg. time.ctime() : Tue Feb 17 10:00:18 2009
	# st_ctime: It represents the time of creation time on Windows. It is expressed in seconds.
	ctime = os.stat(path).st_ctime # this will give teh creation time of the path mentioned

	# returning the creation time
	return ctime


if __name__ == '__main__':
	main()


# A formatted string literal or f-string in print()is a string literal 
# that is prefixed with 'f' or 'F'. These strings may contain replacement
#  fields, which are expressions delimited by curly braces {}. 
# While other string literals always have a constant value, 
# formatted strings are really expressions evaluated at run time.
# eg >>> name = "Fred"
#    >>> print(f"He said his name is {name})."
#	output - "He said his name is Fred."