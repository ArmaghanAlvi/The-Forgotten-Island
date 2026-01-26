<!-- TITLE AND SHORT DESCRIPTION -->
<div align="center">
  <h1 align="center">The-Forgotten-Island</h1>
</div>
<p align="center">A text based adventure game based in Python that runs in the terminal</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#project-overview">Project Overview</a></li>
    <li><a href="#features-and-classes">Features and Classes</a></li>
    <li><a href="#lessons">Lessons</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


## Project Overview
I made this project in 2022 for my highschool Video Game Design midterm. The requirements were to make a simple text-based adventure game that showed mastery of python syntax, 
understanding of conditionals, loops, functions, etc. Being a highschool freshman with too much time, I decided to go further than that, and created this far more developed game. 
This text-based adventure game runs in the terminal once the code is run. The premise of the game's story is that the player wakes up stranded on an island with amnesia, and has to
figure out how to escape. However, they are not simply stuck there, but they are also in a time loop, where the day restarts if they reach the end, or die at some point during it.

I considered most text-based RPG options where it is simply a tree of choices which takes trial and error to find the correct path to the end to be boring. Due to this, 
I created a game where there are two positive endings and one negative ending, meaning there are multiple end points to the game, and not only a single path to sucess. 
Further, there are parts of the game that allow the player to linger in an area for a while, and other parts that are not consistently the same each time around. 

The restarting of the game once the player dies is also not traditional to a basic text based RPG, as it doesn't actually restart the game immediately. Instead, deaths are counted as day-restarts as well. If the player suffers from too many day-restarts, they reach the negative Insanity Ending. If they manage to reach the end of the game successfully, they will 
either accomplish the Escape Ending or the New Beginnings Ending.

### Built with
**Language used:** Python  

**Python libraries and modules:**
* random
* time
* Timer from threading module
* os

## Features and Classes
Title text: title is printed as large, styled words using ASCII text art

Text display: Manual and auto text display options are provided

`Control` class: provides various control functions like clearing the terminal, in-game time keeping, and story line-printing.

`General` class: provides functions for checking player status, inventory status, and an action function for when the player is prompted

`Mechanics` class: provides functions for a quick-time hunting mechanic, the resource management and crafting mechanic, the combat mechanic, and the day-restart/time-loop mechanic

`Story` class: includes all functions related to the actual story text and when to use the functions from the other classes

`Endings` class: includes story text abd ASCII art text for all three possible endings


## Lessons
This project is essentially the first real project I made. It taught me how to plan out and execute an idea I had in mind.
It also helped me properly grasp Python as a language, and understand code logic in general, to an extent.


## Acknowledgements
This project was made in replit.com. 


