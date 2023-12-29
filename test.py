from exiftool import ExifToolHelper as et
import os


incorrect_extensions_files = []
missed_files = []
targetable_files = []
total = 0


LABELS = ['QuickTime:MediaCreateDate']


def is_correct_file_extension(file_name):
	return file_name.endswith(".MP4") or file_name.endswith(".mp4") or file_name.endswith(".mov") or file_name.endswith(".MOV")



for file_name in os.listdir("./videos/"):
	total += 1
	if is_correct_file_extension(file_name):
		# print(file_name)
		metadata_dict = et().get_metadata(f"videos/{file_name}")[0]

		for label in LABELS:
			if label in metadata_dict:
				targetable_files.append(file_name)
				# print(f"    >>> {label}: {metadata_dict[label]}")
			else:
				missed_files.append(file_name)
	else:
		incorrect_extensions_files.append(file_name)



print(f">>> {len(incorrect_extensions_files)}/{total} incorrect extensions")
print(f">>> {len(missed_files)}/{total} missed files")
print(f">>> {len(targetable_files)}/{total} target files")



