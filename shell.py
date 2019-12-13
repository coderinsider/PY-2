import os
from os import path
import shutil
from shutil import make_archive
def main():
	# Make a duplicate of an existing file
	if path.exists('readme.txt'):
		# Get the path to the file in the current directory
		src = path.realpath('readme.txt')

		# let's make a backup copy by appending "Bak" to the name
		#dst = src + ".back"

		# Copy over the premissions, modification times, and other info 
		# shutil.copy(src, dst)
		# shutil.copystat(src, dst)

		# rename the original file
		#os.rename('readme.txt', 'newfile.txt')
		# now put things into a ZIP archive
		root_dir, tail = path.split(src)
		shutil.make_archive("archive", "zip", root_dir)
		# more fine-grained control over ZIP files

if __name__ == "__main__":
	main()