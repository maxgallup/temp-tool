from exiftool import ExifToolHelper as et
import os


incorrect_extensions_files = []
missed_files = []
targetable_files = []
created_dates = []

total = 0


LABELS = ['QuickTime:MediaCreateDate']

PATH = "../Home Videos/"


def is_correct_file_extension(file_name):
	return file_name.endswith(".MP4") or file_name.endswith(".mp4") or file_name.endswith(".mov") or file_name.endswith(".MOV") or file_name.endswith(".m4v") or file_name.endswith(".M4V")



for file_name in os.listdir(PATH):
	total += 1
	if is_correct_file_extension(file_name):
		metadata_dict = et().get_metadata(f"{PATH}{file_name}")[0]

		for label in LABELS:
			if label in metadata_dict:
				targetable_files.append(file_name)
				created_dates.append(metadata_dict[label])
			else:
				missed_files.append(file_name)
	else:
		incorrect_extensions_files.append(file_name)



print(f">>> {len(incorrect_extensions_files)}/{total} incorrect extensions")
for f in incorrect_extensions_files:
	print(f"    {f}")

print(f">>> {len(missed_files)}/{total} missed files")
for f in missed_files:
	print(f"    {f}")


print(f">>> {len(targetable_files)}/{total} target files")

for i, f in enumerate(targetable_files):

	new_name = created_dates[i].split(" ")[0].replace(":", "_")
	new_name += "_"
	new_name += targetable_files[i]

	
	os.rename(f"{PATH}{targetable_files[i]}", f"{PATH}{new_name}")


