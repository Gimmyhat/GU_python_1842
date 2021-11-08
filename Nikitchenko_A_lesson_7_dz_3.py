import os
import shutil

root_dir = 'my_project'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('html'):
            str_dir = os.path.join(root_dir, 'templates', os.path.split(root)[-1])
            try:
                if not os.path.exists(str_dir):
                    os.makedirs(str_dir)
                shutil.copy(os.path.join(root, file), str_dir)
            except Exception as e:
                print(e)


