import os
from pathlib import Path
import re
import getpass
user = getpass.getuser()

def write_mime_types(file_obj):
    global mime_type
    mime_type = list(filter(None, mime_type[len('MimeType='):].split(';')))
    for i in mime_type:
        file_obj.write(i+'=LibreOffice.desktop;\n')

def read_mime_types(file_obj):
    global mime_type
    for i in file_obj.read().split('\n'):
        if(bgns_MimeType_ends_smc.search(i)):
            mime_type = bgns_MimeType_ends_smc.findall(i)[0]

def work_with_files():
    if my_file.is_file():
        rd_file = open(my_file, 'r')
        wrt_file = open(my_file, 'a')
        if '[Added Associations]' not in list(filter(None, rd_file.read().split('\n'))):
            wrt_file.write('[Added Associations]\n')
        rd_file.close()
    else:
        wrt_file = open(my_file, 'w')
        wrt_file.write('[Added Associations]\n')

    for i in desktop_files:
        rd_file = open(i)
        read_mime_types(rd_file)
        write_mime_types(wrt_file)
        rd_file.close()
    wrt_file.close()

if __name__ == '__main__':
    bgns_MimeType_ends_smc = re.compile(r'^MimeType=.*;$')
    mime_type = ''
    desktop_files = [f for f in os.listdir('.') if re.match(r'^libre.*\.desktop$', f)]
    print(desktop_files)
    my_file = Path(f'/home/{user}/.config/mimeapps.list')
    work_with_files()
