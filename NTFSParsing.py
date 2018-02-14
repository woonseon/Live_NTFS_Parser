#-*- coding: utf-8 -*-
import pytsk3, sys
from flask import render_template

class Extract_File:

    def __init__(self, volume):
        try:
            self.volume='\\\\.\\'+str(volume)
            self.img=pytsk3.Img_Info(self.volume)
            self.fs=pytsk3.FS_Info(self.img)
        except:
            return "none"
    
    def open_directory(self, dir_path):
        data = []

        dir_path = str(dir_path)
        
        count = 0
        dir_m_path = dir_path.replace("\\", "/")
        self.directory = self.fs.open_dir(path=dir_m_path)
        for f in self.directory:
            try:
                file_name = f.info.name.name
                filepath = dir_m_path  + "\\" + file_name.decode('utf-8')

                is_dir = str(f.info.meta.type)
                if is_dir == "TSK_FS_META_TYPE_DIR": t = "Directory"
                else: t = "File"

                d = {
                    "type" : t,
                    "filename" : file_name.decode('utf-8'),
                    "size" : f.info.meta.size,
                    "path" : self.volume.split(".\\")[1] + "\\" + dir_path,
                    "mtime" : f.info.meta.mtime,
                    "atime" : f.info.meta.atime,
                    "ctime" : f.info.meta.ctime,
                    "etime" : f.info.meta.crtime
                }

                data.append(d)
                count += 1
            except:
                pass
        return data