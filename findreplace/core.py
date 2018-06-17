from os import path
import glob

ROOT_DIR = path.dirname(path.realpath(__file__))

def findreplace(base_dir='', find_val='', new_val=''):
    print(ROOT_DIR)
    if find_val and new_val:
        for file_name in glob.iglob(ROOT_DIR + '**/*', recursive=True):
            print(file_name)

            with open(file_name, 'r') as file :
                data = file.read()

            replace_data = data.replace(find_val, new_val)

            if replace_data:
                with open(file_name, 'w') as file:
                    file.write(replace_data)

def main():
    findreplace(ROOT_DIR, '', '')

if __name__ == '__main__':
    main()