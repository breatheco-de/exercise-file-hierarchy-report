from os import listdir
import os, requests, re

report = {
    "levels": 0,
    "total_files_found": 0,
    "total_folders_found": 0,
    "broken_links_found": 0,
    "links_found": 0,
    "files_found": [],
    "file_extentions_found": [],
}

def is_broken(url):
    resp = requests.get(url)
    if resp.status_code == 404:
        return True
    else:
        return False

def get_file_links(file_path):
    _file = open(file_path, "r")
    content = _file.read()
    _file.close()
    result = re.findall(r"(?P<url>https?://[a-zA-Z\.\-\/0-9]+)", content)
    return result

def list_files(path):
    report["levels"] += 1
    files = listdir(path)
    print(files)
    for f in files:
        if os.path.isdir(path+"/"+f):  
            report["total_folders_found"] += 1
            list_files(path+"/"+f)
        else:
            print("File found: "+f)
            report["total_files_found"] += 1
            report["files_found"].append(f)
            file_name, extension = os.path.splitext(f)
            report["file_extentions_found"].append(extension[1:])
            links = get_file_links(path+"/"+f)
            report["links_found"] += len(links)
            # for l in links:
            #     if is_broken(l):
            #         report["broken_links_found"] += 1


list_files('./data-files')
print(report)