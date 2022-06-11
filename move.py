import os
import shutil
import time


def check_dir(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def cut_file_name(file_name: str) -> str:
    for i in range(len(file_name)-1, 0, -1):
        if file_name[i] == '.':
            return file_name[i+1:len(file_name)].lower()
    return " "


def current_milli_time() -> str:
    return str(round(time.time() * 1000))


def move(file_from, file_to, type_: str) -> None:
    try:
        shutil.move(file_from, file_to + f'/{type_}')
    except Exception as ex:
        print(ex)


def check_twin_file(final_path_file, src_dir, file_, type_: str) -> bool:
    if os.path.exists(final_path_file):
        src_file_path_twin = os.path.join(src_dir, (current_milli_time() + '____' + file_))
        os.rename(f'{src_dir}\\{file_}', src_file_path_twin)
        move(src_file_path_twin, root_end_dir, type_)
        return True
    else:
        return False


def move_file(file_, src_dir, type_: str) -> None:
    global root_end_dir
    check_dir(root_end_dir + f'/{type_}')

    src_file = os.path.join(src_dir, file_)
    final_path_file = os.path.join(root_end_dir + f'/{type_}', file_)

    if not check_twin_file(final_path_file, src_dir, file_, type_):
        move(src_file, root_end_dir, type_)
    return


def check_dirs(start_dir: str) -> None:
    global type_of_files
    for src_dir, dirs, files in os.walk(start_dir):
        for file_ in files:
            file_end = cut_file_name(file_)
            if file_end in type_of_files:
                move_file(file_, src_dir, file_end)
        if dirs:
            for dir_ in dirs:
                check_dirs(f'{start_dir}\\{dir_}')


root_start_dir = 'E:\\Code\\Python\\check_all_img\\check' #flash_drive or path to dir
root_end_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + '\\files'
type_of_files = ['png', 'jpg', 'jpeg', 'jfif', 'gif', 'webp',
                 'mp3', 'wma', 'wav',
                 'm4a', 'mp4', 'avi', 'mov', 'webm',
                 'torrent', 'zip', 'rar', '7z', 'gz', 'apk', 'pkpass',
                 'fb2', 'pdf', 'epub', 'djvu',
                 'txt', 'docx', 'doc', 'xlsx', 'xls', 'csv', 'pptx', 'ods', 'odt', 'rtf',
                 'ai', 'js', 'c', 'cpp', 'py', 'json', 'php',
                 'exe', 'm3u8', ]


def main() -> None:
    check_dir(root_end_dir)
    check_dirs(root_start_dir)


if __name__ == '__main__':
    main()
