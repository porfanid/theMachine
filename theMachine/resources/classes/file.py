class File(object):

    def __init__(self,folder,file,fast=True):
        import os
        filePath = os.getcwd()+"\\resources\\%s\\%s"  %  (folder,file)
        
        self.file_path=filePath
        
        list_of_lines=list()
        if fast:
            list_of_lines=read_file_1(filePath)
        else:
            list_of_lines=read_file_2(filePath)

        self.lines=list_of_lines

        self.number_of_lines=len(list_of_lines)

    def write(self, text, keep_previous=True):
        final_text=""
        if(keep_previous):
            final_text="\n".join(self.lines)
        f=open(self.file_path,"w")
        f.write(final_text)
        f.close()



def read_file_1(filepath):
    file=open(filepath)
    list_of_lines=file.readlines()
    file.close()
    return list_of_lines


def read_file_2(filePath):
    list_of_lines=list()
    with open(filePath) as file:
        for line in file:
            list_of_lines.append(line)
    return list_of_lines