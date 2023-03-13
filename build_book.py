import glob
import subprocess
import time
import os
import yaml
# glob all files in books/react
for file in glob.glob("books/latex/*.yml"):
    with open(file, "r") as f:
        data = yaml.load(f)
    print("parsing file: " + file)
    # ensure file does not have a title
    if "outputFile" in data:
        # ensure file does not have a title
        outputFile = data["outputFile"]
        if os.path.exists(outputFile):
            print("File exists, skipping")
            continue
    # open the file
    # convert window path to unix path
    file = file.replace("\\", "/")
    # parse yaml from file

    # call subprocess python make_post.py --file file
    result = subprocess.call(["python", "make_post.py", "--file", file])
    # print the result
    print(result)
    time.sleep(10)