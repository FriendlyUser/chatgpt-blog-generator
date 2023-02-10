import os

def main():
    dir_list =  os.listdir('.')
    for full_file_name in dir_list:
        base_name, extension = os.path.splitext(full_file_name)
        if extension == '.pdf': # then .pdf file --> convert to image!
            cmd_str = ' '.join(['convert',
                                '-density 400',
                                full_file_name,
                                '-flatten',
                                base_name + '.png'])
            print(cmd_str)  # echo command to terminal
            os.system(cmd_str)  # execute command

if __name__ == '__main__':
    main()
