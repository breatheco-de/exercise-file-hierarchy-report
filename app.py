from os import listdir
import os, requests, re

def is_broken(url):
    # return true or false depending if the link is broken
    pass

def get_file_links(file_path):
    links = []
    # given a file path, get file content and then get the links inside the content
    # return an array of url
    return links

def list_files(path):
    report = {
        "levels": 0,
        "total_files_found": 0,
        "total_folders_found": 0,
        "broken_links_found": 0,
        "links_found": 0,
        "files_found": [],
        "file_extentions_found": [],
    }
    # this function must loop all the files and directories and update the report 
    # variable accordingly
    return report

print(list_files('./data-files'))