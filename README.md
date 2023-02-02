<!--hide-->
# Working with the Computer File System
<!--endhide-->

Another data-structure very commonly used in the world of coding are TREE's, for example:

1. The computer file system is a Tree.
2. The DOM (Document Object Model) is a Tree.

In this case, we will use the Tree Hierarchy concept to scan and browse through a group of files in a computer.

## 🌱  How to start this project

Do not clone this repository.

1. The first step to start coding is cloning the [python boilerplate](https://github.com/4GeeksAcademy/flask-rest-hello) on your local computer or opening it using gitpod.

a) If using Gitpod (recommended) you can clone the boilerplate by [clicking here](https://github.com/4GeeksAcademy/flask-rest-hello).

b) If working locally type the following command from your command line: 
```sh
https://github.com/4GeeksAcademy/flask-rest-hello
```

2. Install the dependency packages by typing: 

```sh
$ pipenv install --python 3
```

3. Get inside your virtual environment by typing: 

```sh
$ pipenv shell
```

4. You can run the project by typing: 

```sh
$ python src/app.py
```
5. You can also run the tests for the project: 

```sh
$ python src/test.py
```


💡 **Important: Remember to create a new repository, update the remote (`git remote set-url origin <your new url>`), and upload the code to your new repository using `add`, `commit`, and `push`.**

# 📝 Instructions

Given the set of files under the `data-files` folder, please write a program that creates a JSON file called report.json that outputs the following report:

```json
{
    "levels": 3,
    "total_files_found": 5,
    "files_found": ["file_one.csv", "file_two.json"],
    "file_extentions_found": ["csv", "json"],
    "total_folders_found": 3,
    "folders_found": ["folder_one","folder_tow"],
    "links_found": 12,
    "broken_links_found": 4,
}
```

Report explanation:

| Property  | Description |
| --------  | ----------- |
| levels    | Number of connections between the top node and the lowest node |
| total_files_found | how many files were found, folders don't count |
| files_found | the name of each of the files found, without folders |
| file_extentions_found | a non-repeated list of the file extensions found inside the tree |
| total_folders_found | total amount of folders found, files don't count |
| Links found | How many URL's were found starting with http or https |
| broken_links_found | How many of the links were broken (you have to do a GET request and check for 404) |

## 💡 Hint

1. Start by looking `python get files in folder` on google.
2. This query also helps: `python file is a directory` to check if a file is a directory or not.
3. To google how to find links inside the file content: `python find all links in the string`
4. Get extension from file name: `python get file extension`
