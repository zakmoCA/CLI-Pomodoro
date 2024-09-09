# [My App Repo (GitHub)](https://github.com/zakmoCA/ZakeriyaMohamed_T1A3)
# [My Project Management (Trello)](https://trello.com/invite/b/0EUM1gBZ/ATTIe34c9fe163d3046c50de67b75f7ade7735039F3D/t1a3)

# Table of Contents

1. [Sources](#sources)
2. [Style Guide](#style-guide)
3. [Implementation Plan](#implementation-plan)
    1. [Outline](#outline)
    2. [Project Management](#project-management)
    3. [Priorities and Deadlines](#priorities-and-deadlines)
4. [App Features](#app-features) 
    1. [Set Cycle Length](#set-cycle-length)
    2. [Set Work/Break Times](#set-work-and-break-times-for-pomodoro-timer)
    3. [Assign Tasks](#assign-pomodoro-to-specific-tasks)
    4. [Write to CSV](#write-pomodoro-data-to-file)
    5. [Alerts](#alert-when-workbreak-times-are-over)
5. [Features and Checklist Items](#features-and-checklist-items)
    1. [Feature 1: Set Cycle Length](#feature-1-set-cycle-length)
    2. [Feature 2: Set Work And Break Times](#feature-2-set-work-and-break-times)
    3. [Feature 3: Set Task Name](#feature-3-set-task)
    4. [Feature 4: Write To CSV](#feature-4-write-to-csv)
    5. [Feature 5: Alerts](#feature-5-alerts-for-start-of-work-and-break-times)
6. [Tests](#tests) 
    1. [Timer Functionality Test Checklist](#timer-functionality-test-checklist)
    2. [Writing To CSV Test Checklist](#writing-to-csv-test-checklist)
    3. [Dependencies](#dependencies)
    4. [Timer Functionality Test](#timer-functionality-test)
    5. [File Writing Test (CSV)](#writing-to-csv-test)
7. [Help Documentation](#help-documentation)
    1. [System And Hardware Requirements](#system-and-hardware-requirements)
    2. [Dependencies](#dependencies)
    3. [Installaiton Steps](#installation-steps)


# Sources


[Python 'datetime' module](https://docs.python.org/3/library/datetime.html)

[Python 'time' module](https://docs.python.org/3/library/time.html)

[Python 'os' module](https://docs.python.org/3/library/os.html)

[Python chime library](https://pypi.org/project/chime/)

[Python 'unittest' framework](https://docs.python.org/3/library/unittest.html)

[Python unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

[Understanding patching and mocking](https://medium.com/geekculture/right-way-to-test-mock-and-patch-in-python-b02138fc5040)

[Python divmod function](https://www.programiz.com/python-programming/methods/built-in/divmod)




# Style Guide

The style guide I will be following for this project is PEP 8.

# Implementation Plan

## Outline

My Pomodoro applicaiton should perform the basic functions of a pomodoro timer albeit in the command line, the user should be able to:
- Enter a task name for each pomodoro
- Set work and break time durations
- Provide a timer countdown of the pomodoro work/break periods
- Give an alert when work and break periods are over

## Project Management

### Initial Outline
My Initial project outline was done on Asana but I then transitioned to Trello. Below you will see a high level overview of the key components of involved in completing the command line application and assignment. 

![Initial Outline in Asana](/docs/Day1-Asana.png)

### End of First Day

#### Day 1 Trello Board

![Project Board end of Day 1](/docs/end-of-day-1.png)

Once starting the assignment, I transitioned to Trello and developed a more granular implementation plan, complete with checklists for the appropriate items (features/tests), along with deadlines for the key deliverables. By the end of day 1, all the core functionality and testing of the application was complete, although I was yet to expand upon the core functionality to the extent I would want the finished product to have. I believed some of this would come to me as I worked on the application, and indeed feature 4 did as a result.


### End of Second Day

#### Day 2 Trello Board

![Project Board end of Day 2](/docs/end-of-day2.png)

My initial projections for deadlines were not met due to both illness and scope creep. This began to teach me the importance of discipline in sticking to requirements and not expanding scope ad-hoc once clear requirements have been decided. 


### Final Day

### Final day

![Project Board end of day 3](/docs/end-of-day3.png)

By the end of day 3 I updated my README for all the relevant important information, along with beginning to wrap up my README. What was completed;
- All features
- Bash script
- Updated tests to reflect new features
- Began and completed project presentation slides and video 

### End of Final Day

![Project Board end of final day](/docs/final-day-board.png)


## Priorities and Deadlines
In terms of deadlines and priorities, my highest priority tasks were in order;
1. Develop Implementation Plan
2. Write first feature
3. Test first feature
4. Write second and third features/tests

Doing the above things allows me to complete the core functionality of my command-line app, and meet the minimum requirements for the assignment. There would be space after which to decide if I wanted to implement further features and tests. It also involved the most technical and cognitive overhead out of all the deliverables, which is why I prioritised their completion, before the rest of the application and documentation requirements.

Tasks which were of greatest priority were performed first, with orange tags being added to those tags in Trello to denote urgency. The most important features and tasks where also due earliest, so as to ensure as much time as possible could be allocated to them should difficulties arise.

# App Features

## Set Cycle Length

A Pomodoro 'cycle' involves a number of pomodoros before one takes their 'long break'. If the cycle is 4 pomodoros, there will be 3 pomodoros (work periods) whose length the user has defined, each followed by a short break, whose length the user has also defined. After the 4th pomodoro, the user will take their 'long break', after which that cycles is set to be completed. In this application, the completion of a cycle marks the end of the program, if the user wants to run more pomodoros, they would need to restart the program. I plan on extending this functionality of the program to include an option for 'number of cycles', for users who use Pomodoro timers for extensive periods.

## Set Work And Break Times For Pomodoro Timer

The Pomodoro technique is a popular time management technique. It involves picking a task, and setting a 'pomodoro' timer and working on the task, the timer is traditionally for 25 minutes, followed by a 5 minute break. The end of the work and break periods are signified by a sound as is the case with timers, and pomodoro applications typically also provide alerts. My application prompts the user to enter their desired work time and break time in minutes, and then starts the timer.

## Assign Pomodoro to specific tasks

The application prompts the user to enter a 'task' for their pomodoro. This task name can then be used for statistics purposes in the data visualisation aspect of the application ie. how many pomodoros did I complete for task x this week?

## Write Pomodoro data to file

The pomodoro's task name, start time, end time, and duration are written to a CSV file, along with the respective headers.

## Alert when work/break times are over

A distinct sound alert is played using the `chime` library at the start of a work, and either break periods to alert the user should they not be viewing their terminal.

# Features and Checklist Items
## General Outline

The checklists for all the features were very high level and therefore generally the same for all features, starting from simply deciding on the feature to designing, coding, testing, and documenting the feature.

The general process was to sequentially work down the checklist, writing a very basic test first, then coding the feature, and improving test etc. Some features did not follow Test Driven Development principles however, and functionality was tested for the first time after implementing the feature.
### Feature 1: Set Cycle Length

The checklist for the Set Cycle Length feature is below.
![Feature 1 - Set Cycle Length](/docs/set-cycle-length.png)

Set cycle length's general structure is;
- Get user input
- Handle non/inappropriate input
- Store user input as appropriate data type

The design of this feature involved taking a high level view of what processes were involved, the step by step process of which is described above. This was achieved by:
- Ensuring user had to input something, and that something must be a digit
- Converting the user input to type int
- Using control flow to ensure program continues running until appropriate input is obtained
- Alerting the user with an error message if there is non-digit input or if user proceeds (hits enter) without entering input

The functionality for this feature is contained in the pomodoro_length.py module.

### Feature 2: Set Work and Break Times

The checklist for the Set Timer feature is below.
![Feature 2 - Set Timer](/docs/set-pomodoro-timer-plan.png)

The first feature was the timer functionality. It would involve:
- Getting user input for determining the length of the work and break times
- Displaying the timer 
- Handling exceptions

The design of this feature involved a high level overview of what processes would be needed, and then a step by step;
- User input 
- Way to display user input as a countdown timer

Step by step this would require:
1. Getting appropriate user input, by ensuring the user entered only digits
2. Converting this user input to integer type
3. Using either control flow or exception handling to ensure the program (feature) runs until appropriate input has been attained

The functionality for this feature is provided by the run_pomodoro.py and pomodoro_length.py modules, although it is executed by the start function in start_pomodoro.py. 

### Feature 3: Set Task

The checklist for the Set Task feature is below.
![Feature 3 - Set Task](/docs/set-task-plan.png)

The second feature allows the user to allocate the pomodoro to a 'task'. This is achieved by getting user input for the task name. 
Potential inappropriate user input is handled using a while loop:
- User is asked to enter task name
- Program exits while loop and asks user for timer settings
- If no user input is recorded the program continues running and user is told that they they must enter a task name, and prompted again

The 'task' is then appended to the 'tasks' list as a dictionary, which holds the task name (string) and pomodoro data (list of dictionaries) with the keys 'name' and 'pomodoros' respectively. If the task name entered for a pomodoro already exists in our list, the pomodoro data is appended to that task's list of 'pomodoros', else a new task dictionary is created with the current tasks name and pomodoro data.


### Feature 4: Write To CSV

The checklist for the Write To CSV feature is below.
![Feature 4 - Write To CSV](/docs/write-csv-plan.png)

The third feature of this application involves writing the data for each pomodoro to a CSV file, allowing this information to be stored and accessed later, or manipulated using data visualisation tools. This feature required:
- Access to the file system to check for the existence of the data file, and also create the file if it doesn't already exist
- Ability to append new data to the file, without erasing or modifying the existing data
- Handling exceptions, Python's built-in 'csv' and 'open' libraries were used to achieve this

A high level overview of the steps this would require:
1. Checking (once pomodoro finishes) if the CSV file ('pomodoros.csv') already exists in the current directory using os.path.isfile() function
2. Opening the file in append mode if it doesn't exist vs creating it if it does exist
3. If file is new, writing the headers 'Task Name', 'Start Time', 'End Time', and 'Duration'
4. Writing the pomodoro data corresponding to the above headers to the file
5. Close the file once finished 

Like other command-line programs, the user can also abort this program using 'Ctrl/Cmd' + 'C'. We still want to record the pomodoro data should this occur, so the start function which executes the application is wrapped in a try/except block, with the exception being a KeyboardInterrupt.
- When the start function first runs the user is asked to enter timer settings
- It then enters a 'try' block where the pomodoro cycle commences, continuously monitoring for a KeyboardInterrupt exception
- Should the user enter 'Ctrl/Cmd' + 'C', the program enters the 'except' block which handles our file writing before the program ends

This allows us to integrate the KeyboardInterrupt into our application by ensuring the pomodoro data is still recorded should the user want to abort the program.


# Tests

## Timer Functionality Test Checklist
![Test 1: Timer Funcitonality Checklist](/docs/first-test.png)





## Writing To CSV Test Checklist
![Test 2: File Writing Checklist](/docs/second-test.png)


## Test Dependencies

Below are the dependencies for running the tests for this application. Python's unittest library was used, along with it's class 'mock', and 'patch' and 'mock_open' functions.

![Test Dependencies](/docs/test-dependencies.png)


## Timer Functionality Test
![Timer Functionality Test](/docs/timer-functionality-test.png)

The first test checks all the components which provide our pomodoro timer functionality, by checking that it is correctly handling input. Python's mock class and patch functions from the unittest library were used to simulate user input for the purposes of the test:
- Mock input data is defined with the patch function by using the side_effect parameter
- Our cycle length, work and break times are imported from our pomodoro_length function
- The patch function is used to mock the input function by returning the side effects in order
- The test asserts the expected values for each of these variables 

## Writing To CSV Test
![Writing To CSV Test](/docs/file-write-test.png)

The second test checks that the start() function correctly writes our data to the CSV file.
- Multiple mock objects are passed as function parameters including mocking of input, the run_pomodoro function, and a non existent file
- The input is mocked like in our first test using the side_effect parameter
- run_pomodoro is configured to return none which simulates the functions behaviour
- isfile_mock is set to return False, this simulates a non-existent csv file, which should be the case for our very first pomodoro
- The start function is called, and the test retrieves the calls made to the write method, simulaitng the file operaitons
- The arguments passed the write method are captured with the call_args variable, which is a tuple containing the positional and keyword arguments respectively
- The 'write' method only takes positional args, so will need to access the first element but for 2 different calls, the first (writes headers), and the second (writes pomodoro data)
- The test then checks that the first call writes our headers, and that the second call writes the pomodoro data by comparing it to what the resulting string should look like. differences in unix based systems vs windows with regards to line endings are accounted for by checking if either hold true
- This is done by checking that the second call to the write methods first argument is a string that starts with our task name and ends with a newline character

Due to the dynamic nature of the data being written the csv file (timestamps), I don't believe there is a simple way to assert that our CSV data matches exactly what we would anticipate. However the above test virtually guarantees that our data is being written correctly by checking the structure and format of the written data.


# Help Documentation

This was an assessment I built during my Coder Academy course fullstack web-development course in 2023. It is based on 
the [Pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique), a time-management technique which breaks work 
into intervals (usually of 25 minutes) seperated by short breaks, and a long break after a set number of intervals.

## Installation Steps

### Python Version
This application requires a Python 3 version of 3.11.3 and higher. This can be checked by entering the following command in your terminal (command-line):

    python3 --version

If you don't have Python 3.11.3 installed, it can be installed at the official [Python website](https://www.python.org/downloads/)
You can also install it in the terminal as follows:

#### macOS
Open up Homebrew in your terminal and enter the following command:

    brew install python

#### Ubuntu

    sudo apt-get install python3.11

#### Windows
Visit official [Python website](https://www.python.org/downloads/)

If you have Python version 3.11.3 or higher already installed, in your terminal, navigate to the 
directory you would like to clone this repo into.

Inside this directory, run the following command in order to clone the GitHub Pomodro Application.

    git clone https://github.com/zakmoCA/CLI-Pomodoro.git

Once the repository has been cloned locally to your machine, navigate to the repo's root.

    cd CLI-Pomodoro

Now that you are in the root directory, enter the following command, it will add the appropriate execute persmissions.

    chmod +x setup.sh

Finally, to run the application, enter the following command.

    ./setup.sh











