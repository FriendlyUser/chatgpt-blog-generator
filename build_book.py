import glob
import subprocess
import time
# glob all files in books/react
for file in glob.glob("books/react/*.yml"):
    # open the file
    # convert window path to unix path
    file = file.replace("\\", "/")
    # call subprocess python make_post.py --file file
    result = subprocess.call(["python", "make_post.py", "--file", file])
    # print the result
    print(result)
    time.sleep(5)