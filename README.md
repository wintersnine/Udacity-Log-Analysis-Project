# Introduction

This Log Analysis project was made for the Udacity Full Stack Nanodegree course and will answer the following questions using PostgreSQL:

	1. Most popular three articles of all time
	2. Most popular article authors of all time
	3. Days on which more than 1% of requests lead to errors

## PreRequisites:

Python3 - Coded in version 3.5.x
Vagrant - Virtual environment builder and manager
VirtualBox - Open source virtualiztion software
Git - Version control system 

## Getting Started

This project uses a Unix-style terminal that needs to be on your computer. If you are using a Mac or Linux system, your regular terminal program will do. On Windows, it is recommended using the Git Bash terminal that comes with the Git software. If not already having done so, install the above listed software.

## Downloading the Data

You will also need the newsdata.zip file provided by Udacity. Unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

Note that the data can be found and downloaded using the following link: https://goo.gl/67o4vd

## Launching the Virtual Machine

Launch the Vagrant VM inside the Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
```
  $ vagrant up
```
This may take a few minutes depending on your internet connection. Once done, log into the database using the following command:
```
  $ vagrant ssh
```
Change directory to cd/vagrant and look around with the command: ls


## Setting-up the Database

To load the data to the database, type in the command:
  $ psql -d news -f newsdata.sql

To run the database type:
```
	$ psql -d news
```

## Running the script

Within the terminal type in and run: 
```
  $ python3 log.py
```

After the script runs, the results will reveal the output to the questions asked above.


## Credit 

- Credit to Udacity for proving the sql data and instructions on setting up the software and database (as well as providing the teaching material and comments after submission).

- Credit to program creek for understanding psycopg2 in more detail. 
