from collections import defaultdict
from devices import *
from typing import *

def add(device_list, device_type, name):
    if name in device_list.keys():
        return "Error: That name already exists"
    device_list[name] = Device(device_type, name)
    return "Successfully added " + name + "."


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def set_device_strength(device_list: DefaultDict[str, Device], name, strength: str):
    if not is_number(strength):
        return "Error: Invalid command syntax."
    elif int(strength) < 0:
        return "Error: Strength value cannot be negative."
    elif name in device_list.keys():
        device = device_list[name]
        if device.device_type == "REPEATER":
            return "Error: Strength cannot be defined for repeater."
        else:
            device.strength = int(strength)
            return "Successfully defined strength."
    else:
        return "Error: No device exists."


def connect(device_list: DefaultDict[str, Device], device1, device2):
    if device1 == device2:
        return "Error: Cannot connect device to itself."
    elif device1 in device_list.keys() and device2 in device_list.keys():
        n1 = device_list[device1]
        n2 = device_list[device2]
        if n2 in n1.adjacent or n1 in n2.adjacent:
            return "Error: Devices are already connected."
        else:
            n1.adjacent.append(n2)
            n2.adjacent.append(n1)
            return "Successfully Connected."
    else:
        return "Error: node not found"


b = 0
def route_1(went: DefaultDict, curr: Device, res: List, end: Device) -> None:
    global b
    if curr.name == end.name:
        print(*res, sep=" -> ")
        b = b + 1
    elif went[curr.name] != 1:
        went[curr.name] = 1
        for n in curr.adjacent:
            res.append(n.name)
            route_1(went,n,res,end)
            res.pop()
    else:
        pass


def route(start: Device, end: Device):
    global b
    s = b
    went = defaultdict(lambda: 0)
    res = []
    res.append(start.name)
    route_1(went,start, res, end)
    if s == b:
        print("Error: Route not found!")


def info_route(device_list: DefaultDict[str, Device], device1, device2):
    if device1 == device2:
        return device1 + " -> " + device1
    elif device1 in device_list.keys() and device2 in device_list.keys():
        n1 = device_list[device1]
        n2 = device_list[device2]
        if n1.device_type == "REPEATER" or n2.device_type == "REPEATER":
            return "Error: Route cannot be calculated with a repeater."
        else:
            route(n1, n2)
    else:
        return "Error: node not found."

