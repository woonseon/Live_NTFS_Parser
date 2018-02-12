#-*- coding: utf-8 -*-

import pytsk3, sys

class Extract_File:

    def __init__(self, volume):
        self.volume='\\\\.\\'+str(volume)
        self.img=pytsk3.Img_Info(self.volume)
        self.fs=pytsk3.FS_Info(self.img)
    
    def open_directory(self, dir_path):
        data = []

        dir_path = str(dir_path)
        
        count = 0
        dir_path = dir_path.replace("\\", "/")
        self.directory = self.fs.open_dir(path=dir_path)
        for f in self.directory:
            try:
                file_name = f.info.name.name
                filepath = dir_path  + "\\" + file_name.decode('utf-8')

                # if os.path.isdir(filepath): t = "Directory"
                # else: t = "File"
                t = "N/A"

                d = {
                    "type" : t,
                    "filename" : file_name.decode('utf-8'),
                    "size" : f.info.meta.size,
                    "path" : dir_path,
                    "mtime" : f.info.meta.mtime,
                    "atime" : f.info.meta.atime,
                    "ctime" : f.info.meta.ctime
                }

                data.append(d)
                count += 1
            except:
                pass
        return data