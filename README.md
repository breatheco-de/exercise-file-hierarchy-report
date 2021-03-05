# Working with the Computer File System

Another data-structure very commonly used in the world of coding are TREE's, for example:

1. The computer file system is a Tree.
2. The DOM (Document Object Model) is a Tree.

In this case, we will use the Tree Hierarchy concept to scan and browse through a group of files in a computer.

# 💻 Installation


```
## 💻 Installation

a) You can either run this project on Gitpod: gitpod.io#<https://github.com/breatheco-de/exercise-file-hierarchy-report.git>

and run the following on its command line:

``py
$ pipenv run install
$ pipenv run python app.py
```

b) or clone this repository on your local computer:

1. Clone this repository: 

```sh
$ git clone https://github.com/breatheco-de/exercise-file-hierarchy-report.git
```

2. Install the dependecy packages by typing: 

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

# 📝 Instructions

Give the set of files under the `data-files` folder, please write a program that creates a JSON file called report.json that outputs the following repot:

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
| file_extentions_found | a non-repeated list of the file extentions found inside the tree |
| total_folders_found | total amount of folders found, files don't count |
| Links found | How many URL's were found starting with http or https |
| broken_links_found | How many of the links were broken (you have to do a GET request and check for 404) |

## 💡 Hint

1. Start by looking `python get files in folder` on google.
2. This query also helps: `python file is directory` to check if a file is a directory or not.
3. To google how to find links inside the file content: `python find all links in string`
4. Get extension from file name: `python get file extension`
