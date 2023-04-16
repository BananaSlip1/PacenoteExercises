# PacenoteRepeat
Just a simple program that prompts the use (audio) with rally pacenotes then lets the user repeat (type) the pacenotes back. Made it to help train pacenote recall.

# Background
If you're like me, I find that I lose track of pacenotes while sim rallying for different reasons (correcting for bad entries, irl distractions, etc.), so I figured I could use some pacenote hearing/remembering practice. I threw together this  basic Python program that will call out random pacenotes (1-6 L/R; Flat, Square, Hairpin L/R) and prompts you to repeat (type) the last N pacenotes. N can be any number. I find I really start to suffer at N = 3...cuz I is a dumb. There are some bugs, but it works for what I want to practice: Hear pacenote, make decision(s), recall pacenote, hear next pacenote, repeat.

I originally set out to make a n-back game with pacenotes, but found that that wasn't really doing it for me (hence while you'll see some commented out "time" related imports and code.

I made the idiot mistake of not using something like ChatGPT to write the code, and I'm no coding guru, so there's certainly a ton of room for improvement.

# Reasons it might not work for you
The only reasons I can think this won't work for you:
- Different python versions (this was written in Python 3)
- Don't have the imports installed (a quick google can show you how to import any of the ones I used - which are at the top of the script).
- Audio file path issues. The python module "playsound" is used to...play sounds. I used a file path relative to the location of my script. If you want to do that, just extract the audio files into a directory called "Audio" in the directory of the python script. e.g. if your script is on your desktop - C:\User\prof\Desktop, then the audio files just need be in - C:\User\prof\Desktop\Audio. And it _should_ work.

# Usage
## Starting it
I wrote this in Visual Studio so I have a couple extra metadata files, but with just the raw python file (and the appropriate audio file setup) all you'll need to do is run a command prompt or terminal then run it like you would any other python script -> "python RallyRepeat.py" (if you're located in the same directory - otherwise it'll have to be the full path to the script). It _doesn't_ work to double click the file like it's an exe.

## Menu
Immediatly you'll see a small menu. From the top down:

Setting and Score
- "N is set to: 1"                    this just tells you what the "N" or recall length is set to. It's set to 1 at start up.
- "Total correct this session: 0"     shows you how many corrects you've had in a given session, a session begins when the program does and ends when the program is closed.
- "Total incorrects this session: 0"  same as above, but for incorrects - this is off by 1 sometimes cuz it'll count a quit as an incorrect submission.
- "Total rounds: 0"                   shows how many rounds you've completed (rounds are multiples of N - i.e. if you have N set to 3, it'll take three prompts for it to count as 1 round.

Menu/Options
- "(S)tart"       Type S or s to start the session with the current displayed N
- "Change (N)"    Type n or N to change the N value
- "(C)lear score" Type C or c to clear the score/rounds
- "(Q)uit"        Type q or Q to quit

## In game
The game is pretty simple to play. You'll hear a single pacenote, your job is to type the previous N notes, each seperated by a space. For example, while N is set to 1, all you need to do is type in the last heard pacenote - easy. If N is set to 2, then you have to type in the last 2 pacenotes you heard (there is a bug here, until the number of pacenotes read equal your N, it'll say you got it wrong no matter what your input is).

The inputs I chose are pretty simple, for any numbered turn, just type the number and the first letter of the direction. E.g. if the pacenote is "1 Left", the corresponding input is "1l" or "1L" - it's case insensitive. For Flat, Square, and Hairpin, just type the initial then the direction: "Flat right" -> fr.

When N is greater than 1, make sure you put spaces between your entires, e.g. if I want to input "1 Left, 2 Right" type: "1l 2r"

To quit, just type "q" and it'll take you back to the menu.

# Known bugs
It works to a standard good enough for me, so I'm not really planning on editting the code much in the immediate future, but here are some known bugs:
- No intelligent input handling, i.e. the program expects users to type the appropriate inputs. It won't explode if you don't, but there aren't any cute "That isn't a valid input" messages or anything like that.
- As mentioned above, the game will tell you that your input is incorrect when N is greater than 1 until the number of read pacenotes equals your N. E.g. if I have N set to 3, I _cannot_ be correct until the third note is read, but should be find after that.
- Because I wrote this in Visual Studio, I had to use a very manual "print("\n" * 20)" to _clear_ the screen. Outside of Visual Studio, changing the code in the clear funciton to "os.system('cls')" (windows) or "os.system('clear')" (\*nix) will clear the screen in a much more pretty way (if you want to do this, make sure to import os).

# Modify input/audios
## Changing Audio
Changing audio cuts shouldn't be much of a challenge. I made mine using my mic, i.e. you can do the same low budget thing if you want them in a different language or want the UK style notes, etc. All you'll need are the auido files as mp3 files, and you'll have to change the code to match the file names/paths to the audio (under the valToSound function). See "How it works" to better understand how the code works to help make that decision.

The provided set of audio files is limited to the following pacenotes: 1-6 L or R and Flat, Square, Hairpin L or R (a total of 18 different noets).

## Changing input correlations
Should you change the audio and/or just want to change the input mapping, you can find that under the "soundToVal" function. It literally just takes your input and looks for the right if statement then returns the corresponing value. To change, just edit the strings of the if statements (see "How it works" to understand how it's mapped).

# How it works
The game works by using the exiting random.randrang function to generate a random number between 1 and 18 (there are 18 different pacenote audio files). Once that random number is generated it sends it to the "valToSound" function that matches the number to an audio file (e.g. 1 = /Audio/1L.mp3) and plays the audio. It also sends that random number to a list "aQueue" that will be used to compare our input to.

It then waits for the user to make an input. Once the user makes an input, it sends that input to iVList, which splits the input up, using a space as the delimiter. It checks for a "q", which would indicate that the user wishes to quit. If it doesn't find one, it converts the list of string inputs into their matching number using the "soundToVal" function ("1l" = 1 Left = 1; the code in "soundToVal" and "valToSound" have to have matching associations. I.e. if 1 in "valToSound" = the 1 Left audio, then "1l" in "soundToVal" has to translate to the value 1.

Once the user input is translated into numbers and put into the iValueList, the program then compares "aQueue" and "iValueList" using the "queComp" function. If they match it returns True, and runs the "correct" function, if they don't match, it runs the "wrong" function".
