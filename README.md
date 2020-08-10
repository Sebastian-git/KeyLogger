# KeyLogger

### Introduction
This Python created keylogger saves key strokes after a configerable amount of time and sends them to a specified email. 

### Usage

After opening the file, the program begins tracking key strokes and automatically sends the data in the background. Make sure to edit these variables before running your program.

Be sure to input your email and password into the raw code before running
``` python
GMAIL = ""
PASSWORD = ""
```

Edit the SAVINGDELAY variable before running to specify how long to wait before sending each email
```python
SAVINGDELAY = 10
```

The STOPCOMBO variable are the keys you have to hold to stop the program from running in the background (default is alt+down arrow)
```python
STOPCOMBO = {keyboard.Key.alt_l, keyboard.Key.down}
```


### Launch

Python 3.6.3

### Status: 

In progress

#### [back to the top](#flashcards)
