# SBC_Sistema-Expert
# Text Editor
## Table of Contents
  - [Overview](#overview)
  - [Installation](#installation)
  - [Dependecies](#dependecies)
  - [Input files](#input-files)
  - [Usage](#usage)
  - [Example](#example)
  - [Group members](#group-members)
  - [References](#references)

## Overview 
This Python and Prolog Go program simulates an expert system that monitors and integrates functions for effective building climate management, ensuring optimal temperature, air quality, energy efficiency, and rapid detection of security and infrastructure issues.

The Python project additionally offers visualization capabilities to inspect the final state of the building. 


## Installation
Project can be downloaded from the attached folder or by clonning our GitHub repository:


```bash
git clone https://github.com/gpol2003/SBC_Sistema-Expert.git
```
## Dependencies
### Python
+ **json**: to read input file filled with initial condictions
## Usage

### Python
To execute the python code you have several ways:

#### From Linux terminal
```bash
cd Python
python main.py
```

## Input files
In order to set the initial conditions of de building you have to add a json file to de Pyton/data folder (there are some test files).

### Format
The json file must have the following format:
```bash
{
    "day": <day> (string),
    "time": <time> (int),
    "temperature": <temperature> (int/float),
    "building": {
        "floors": [
        {
            "name": <floor_id>,
            "rooms": [
                {
                    "name": <room_id>,
                    "busy": <occuppied> (boolean),
                    "temperature":<temperature> (int/float),
                    "windows": [
                        {
                            "name": <window_id>,
                            "open": <oppened> (boolean)
                        },
                        <another_window>,
                        ...
                    ]
                },
                <another_room>,
                ...

            ]
        },
        <another_floor>,
        ...
        ]
    }
  }
```

### File example
```json
{
    "day": "Monday",
    "time": 10,
    "temperature": 23,
    "building": {
        "floors": [
        {
            "name": "floor1",
            "rooms": [
                {
                    "name": "room1",
                    "busy": true,
                    "temperature": 14,
                    "windows": [
                        {
                            "name": "window1",
                            "open": true
                        },
                        {
                            "name": "window2",
                            "open": false
                        }
                    ]
                },
                {
                    "name": "room2",
                    "busy": true,
                    "temperature": 25,
                    "windows": [
                    ]
                }

            ]
        }, 
        {
            "name": "floor2",
            "rooms": [
                {
                    "name": "room3",
                    "busy": false,
                    "temperature": 15,
                    "windows": [

                    ]
                }
            ]
        }
        ]
    }
  }
```
## Example

## Group members
Andrea Ballester Griful - andrea.baallester@students.salle.url.edu

Joan Tarragó Pina - j.tarrago@salle.url.edu

Pol Guarch Bosom - pol.guarch@salle.url.edu

## References
- [How to open files in Python](https://codedamn.com/news/python/check-if-a-file-exists-using-python)
- [Working with json files in Python](https://www.w3schools.com/python/python_json.asp)

