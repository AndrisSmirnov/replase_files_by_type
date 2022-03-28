import os
import shutil
import time

def current_milli_time() -> str :
    return str(round(time.time() * 1000))

def move_pic() -> None:
    return

def move_vid() -> None:
    return

root_src_dir = 'D:\\' #flash_drive
root_end_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\files'

if not os.path.exists(root_end_dir):
    os.makedirs(root_end_dir)

for src_dir, dirs, files in os.walk(root_src_dir):
    for file_ in files:
        if file_.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            src_file = os.path.join(src_dir, file_)
            final_file = os.path.join(root_end_dir, file_)

            # print(f"src_dir\t\t{src_dir}\ndirs\t\t{dirs}\nfiles\t\t{files}\nfile_\t\t{file_}\nsrc_file\t{src_file}\n")

            if os.path.exists(final_file):
                src_file_twin = os.path.join(src_dir, (current_milli_time() + '____' + file_))
                os.rename(src_file, src_file_twin)
                shutil.move(src_file_twin, root_end_dir)
                continue

            try:
                shutil.move(src_file, root_end_dir)
            except Exception as exception:
                print(exception)
                pass