import os
import zipfile
import importlib
import csv
import argparse


def extract_zipped_homeworks(hw_name, extension="zip"):
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
            zip_ref = zipfile.ZipFile(zipped_dir_name + item)
            zip_ref.extractall(unzipped_dir_name +
                               "/" +
                               encrypt(item.split('_')[1].split('.')[0]))
            zip_ref.close()


def run_tests(hw_name):
    spec = importlib.util.spec_from_file_location(
        hw_name + "_tests",
        "./test_suites/" + hw_name + "_tests.py"
    )
    test_suite = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_suite)

    if os.path.exists("homeworks/" + hw_name + "/unzipped/"):
        parent_path = "./homeworks/" + hw_name + "/unzipped/"
        names = next(os.walk(parent_path))[1]
        grades = {name: 0 for name in names}
        for name in names:
            print("Running Test on: " + name)
            hw_path = parent_path + name + "/assignment.py"
            grades[name] = test_suite.run_suite_on_file(hw_path)
        with open("grades/" + hw_name + '_grades.csv', 'w') as f:
            w = csv.DictWriter(f, grades.keys())
            w.writeheader()
            w.writerow(grades)
        print(grades)
        return grades


def encrypt(mes):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    key = "l5029dvb81mokxqscygnhatzpu4ewi7f3jr6"
    keyIndices = [alphabet.index(k.lower()) for k in mes]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)


def decrypt(mes):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    key = "l5029dvb81mokxqscygnhatzpu4ewi7f3jr6"
    keyIndices = [key.index(k) for k in mes]
    return ''.join(alphabet[keyIndex] for keyIndex in keyIndices)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args()
    hw_name = args.name
    if not os.path.exists("homeworks/" + hw_name + "/unzipped/"):
        extract_zipped_homeworks(hw_name)
    run_tests("hw0")
