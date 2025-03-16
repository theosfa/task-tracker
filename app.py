#!/usr/bin/env python3

import argparse
from datetime import date
import json
from pathlib import Path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser(description=f"Simple {bcolors.HEADER}Todo CLI{bcolors.ENDC} list app", prog="Todo CLI")

parser.add_argument(
    "-a",
    # "--add", 
    metavar="<str>",  
    type=str, 
    help="Add <str> as task"
    )
parser.add_argument(
    "-u",
    # "--update",  
    metavar=("<id>", "<str>"),
    nargs=2,
    help="Update task with <id> with <str> as task description"
    )
parser.add_argument(
    "-d",
    # "--delete", 
    metavar="<id>",  
    type=int, 
    help="Delete task with <id>"
    )
parser.add_argument(
    "-m",
    # "--move, 
    metavar=("<d, t ,p>", "<id>"),
    nargs=2, 
    type=str,
    help="Manage tasks -m d <id> means done, -m t <id> means todo, -m p <id> means in progress"
    )
parser.add_argument(
    "-l",
    # "--list", 
    metavar="<d, t ,p>",
    nargs="?", 
    required=False,
    type=str,
    const="a",
    # default="a",
    choices=["a", "d", "t", "p"],
    help="List tasks -l means all, -ld means done, -lt means todo, -lp means inprogress",
    )


args = parser.parse_args()

def addData(add : str, id : int) -> json:
    data = {
        "id" : id,
        "description" : add,
        "status" : "todo",
        "createdAt" : todayDate(),
        "updatedAt" : todayDate(),
    }
    return data


def todayDate() -> str:
    return str(date.today())

status = {
    "d" : "done",
    "t" : "todo",
    "p" : "in progress"
}

status_color = {
    "done" : bcolors.OKGREEN,
    "todo" : bcolors.WARNING,
    "in progress" : bcolors.OKBLUE
}

filename = Path('todo.json')
if not filename.exists():
    with open(filename, "w") as file:
        file.write("[]")
        
f = open(filename)
data = json.load(f)
f.close()

if args.a :
    id = data[-1]['id'] + 1
    data.append(addData(args.a, id))
    with open(filename, "w") as f:
        json.dump(data, f)
    print(f"{bcolors.HEADER}TodoCLI:{bcolors.ENDC} Task added successfully ({bcolors.WARNING}ID : {id}){bcolors.ENDC}")
    
if args.d:
    id = args.d
    no_such = 0
    for i, el in enumerate(data):
        if el["id"] == (id):
            data.pop(i)
            no_such = 1
    with open(filename, "w") as f:
        json.dump(data, f)
    if no_such == 1:
        print(f"{bcolors.HEADER}TodoCLI:{bcolors.ENDC} Task deleted successfully ({bcolors.WARNING}ID : {id}){bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Task not found.{bcolors.ENDC}")
        
if args.u:
    id = int(args.u[0])
    text = args.u[1]
    no_such = 0
    for i, el in enumerate(data):
        if el["id"] == id:
            data[i]["description"] = text
            no_such = 1
    with open(filename, "w") as f:
        json.dump(data, f)
    if no_such == 1:
        print(f"{bcolors.HEADER}TodoCLI:{bcolors.ENDC} Task updated successfully ({bcolors.WARNING}ID : {id}{bcolors.ENDC},{bcolors.OKCYAN} TEXT : {text} {bcolors.ENDC})")
    else:
        print(f"{bcolors.FAIL}Task not found.{bcolors.ENDC}")

if args.m:
    new_status = args.m[0]
    id = int(args.m[1])
    no_such = 0
    for i, el in enumerate(data):
        if el["id"] == id:
            data[i].update({"status" : status[new_status]})
            no_such = 1
    with open(filename, "w") as f:
        json.dump(data, f)
    if no_such == 1:
        print(f"{bcolors.HEADER}TodoCLI:{bcolors.ENDC} Task moved successfully ({bcolors.WARNING}ID : {id}{bcolors.ENDC},{bcolors.OKCYAN} NEW STATUS : {status[new_status]} {bcolors.ENDC})")
    else:
        print(f"{bcolors.FAIL}Task not found.{bcolors.ENDC}")

if args.l:
    type_list = args.l
    prints = 0
    if type_list != "a":
        print(f"{status_color[status[type_list]]}{status[type_list]}:{bcolors.ENDC}")
    else:
        print(f"{bcolors.HEADER}All tasks{bcolors.ENDC}")
    for el in data:
        if type_list != "a" and status[type_list] == el["status"]:
            prints += 1 
            print(f"{bcolors.FAIL}ID:{el["id"]}{bcolors.ENDC}\t{bcolors.BOLD}{el["description"]}{bcolors.ENDC}\t{el["status"]}")
        elif type_list == "a":
            prints += 1
            print(f"{bcolors.FAIL}ID:{el["id"]}{bcolors.ENDC}\t{bcolors.BOLD}{el["description"]}{bcolors.ENDC}\t{status_color[el["status"]]}{el["status"]}{bcolors.ENDC}")
    if prints == 0:
        print(f"{bcolors.FAIL}No tasks found.{bcolors.ENDC}")
