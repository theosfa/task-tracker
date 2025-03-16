[Link to the task](https://roadmap.sh/projects/task-tracker)
# How to run
## Linux / MacOS
Download from git
```bash
# to run as executable
$ chmod +x app.py
$ ./app.py -h

#to run using python
$ python3 app.py -h 
```
## Windows
```bash
# to run using python
$ python app.py -h
```

After running this on your machine you will help menu :
```bash
$ python3 app.py -h
usage: Todo CLI [-h] [-a <str>] [-u <id> <str>] [-d <id>] [-m <d, t ,p> <id>] [-l [<d, t ,p>]]

Simple Todo CLI list app

options:
  -h, --help         show this help message and exit
  -a <str>           Add <str> as task
  -u <id> <str>      Update task with <id> with <str> as task description
  -d <id>            Delete task with <id>
  -m <d, t ,p> <id>  Manage tasks -m d <id> means done, -m t <id> means todo, -m p <id> means in progress
  -l [<d, t ,p>]     List tasks -l means all, -ld means done, -lt means todo, -lp means inprogress
```

And now you can use this app following help from `help menu`