import os
import subprocess
import zipfile


def extract_zipped_homeworks(hw_name="hw0", extension="zip"):
    zipped_dir_name = "homeworks/" + hw_name + "/zipped/"
    unzipped_dir_name = "homeworks/" + hw_name + "/unzipped/"
    if not os.path.exists(zipped_dir_name):
        print("Homework directory does not exist.")
        return
    if not os.path.exists(unzipped_dir_name):
        os.makedirs(unzipped_dir_name)
    for item in os.listdir(zipped_dir_name):
        print(item)
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(zipped_dir_name + item)
            zip_ref.extractall(unzipped_dir_name + "/" + item.split('_')[1])
            zip_ref.close()


def run_tests(arg):
    pass

extract_zipped_homeworks()
