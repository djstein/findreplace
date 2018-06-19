import os
import glob
import shutil

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

def findreplace(base_dir=ROOT_DIR, find_val='', new_val=''):    
    if '~' in base_dir:
        base_dir = os.path.expanduser(base_dir)
    print(base_dir)
    if find_val and new_val:
        for root, dirs, files in os.walk(base_dir):
            # import pdb
            # pdb.set_trace()
            for filename in files:
                path = os.path.join(base_dir, root, filename)
                new_path = ''
                if find_val in root:
                    new_path = path.replace(find_val, new_val)
                    os.makedirs(os.path.dirname(new_path), exist_ok=True)
                print(path, new_path)
                if os.path.isfile(path):
                    with open(path, 'r') as file :
                        data = file.read()

                    replace_data = data.replace(find_val, new_val)

                    if replace_data:
                        file_path = new_path if new_path else path
                        with open(file_path, 'w') as file:
                            file.write(replace_data)
                        if new_path:
                            shutil.rmtree(os.path.dirname(path))
                    
                    if not os.access(path, os.W_OK):
                        st = os.stat(path)
                        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
                        os.chmod(path, new_permissions)
