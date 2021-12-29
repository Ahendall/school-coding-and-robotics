

## This is my summative project for Coding & Robotics 7, Unit 2: Python.
For this project, We made a Digital Adventure Story.
I Chose to make mine an Choose Your Own Adventure (CYOA) Adaptation of ***Star Wars: Episode III - Revenge of the Sith***.
There are 2 versions of the project.\
To download the Simple Answer (SA) version of the project, [click here](https://github.com/Ahendall/School-robotics-and-coding/raw/main/Unit%202%20-%20Python/%5BIMPORTANT%5D%20Summative%20Assignment/Summative%20Assignment%20%28SA%29.zip).\
To download the Complicated Answer (CA) version of the project, [click here](https://github.com/Ahendall/School-robotics-and-coding/raw/main/Unit%202%20-%20Python/%5BIMPORTANT%5D%20Summative%20Assignment/Summative%20Assignment%20%28CA%29.zip).
***
A few things to note:
- The Audio in this project has not been volume-adjusted. So Some audio
files will be louder than others when you play it back
- When the program plays an audio file, it will take a second to load.
- You must type the option exactly as you see it (excluding letter cases)
- This requires [Python 3.9.4+](https://www.python.org/downloads/) to run properly. Please download it.
- This requires the *simpleaudio API* to run properly. To download it:
	1. Make sure you added Python 3.9.4 to PATH when installing.
	2. Run this command in your Command Prompt (Make sure *pip* is the correct command for your OS)
	![make sure pip command is the correct one for your platform](https://i.imgur.com/Yxpv6W3.png)

***
### Here are some of the issues I encountered while working on this.
***Audio file not found when Executing through VS Code***\
**Cause of issue:** VS Code's working directory isn't where the .py file is\
**Solution:** I was unable to fix this issue since I didn't know how properly to edit the launcher.json file.
At first, I used VS Code to edit the file, and IDLE to run it. Then, I just switched entirely
to Visual Studio 2019 Community Edition.


***Code only continues after audio finishes***\
**Cause of issue:** The *playsound* function from the *playsound* API makes the program wait
until the Audio finishes to continue it.\
**Solution:** used the *simpleaudio* API so that there were 2 functions. 1 for letting the code
continue while the audio was still playing, and the other waits until the audio is finished\
(  **play()** and **wait_done()** ).


***Any random answer works on lines 301 & 359 of the CAE***\
**Cause of issue:** for *SOME CONFUSING AF REASON*, when I use *or* to handle multiple option choices
(mainly to let the user type the answer without an apostrophe),  the while loop that makes sure
the user types a valid answer, just doesn't function properly.\
**Solution:** Honestly just removed the *or* and the second options without the apostrophe then created a simple answer version of the project.


***Audio kept overlapping and making messy noises***\
**Cause of issue:** *Simpleaudio* does not automatically stop the currently playing audio when another one starts playing.\
**Solution:** Manually stopped all playing audio using the function *sa.stop_all()*.
***

### Self Reflection

***What went well:*** \
I thought I did very well working on this project. Overall, coding the project was fairly simple with only a few issues. And when there was an issue, I managed to overcome it. I really like how the project turned out as well. I also thought that it was good that I made a CA and SA version of the project just so that there's an original experience, and a simplified one so that it's easier for the user.\
***Possible improvements:*** \
I could have tried to utilize list variables, but I just wasn't sure how I would use them in this specific story.\
 Also, I could have spent some time on making sure that the Audio files were properly leveled so that you wouldn't have to keep adjusting your volume throughout the story.
 ***
