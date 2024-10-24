# Titanic Tussle
##  Overview
The game is a 3v3 Monsters battle using ros topic to communicate between players and server.  
![image](https://github.com/user-attachments/assets/c7d3cb27-1017-49d4-85dc-2ca29252ef87)  
● Each monster has two types of attacks:  
a. Attack all : deals 10 percent of the attacking monster’s max hitpoints to each of
the opponent’s monsters that are alive.  
b. Attack one : deals 20 percent of damage to the selected Monster (20 percent of
max hitpoints)  
● In each round, the attack order goes like this:  
❖ First, all of Player A’s monsters will get to attack in the order (fire, water earth)
for which A will communicate with the main server and ask for the hitpoints of
all the monsters via ros topic and depending on the hitpoints of the opponent,
strategize his attack (manually) and send his move to the main server via
another ros topic.  
❖ Then, all of Player B’s monsters will get to attack in the order (Rock, Thunder,
Wind) for which B will communicate with the main server and ask for the
hitpoints of all the monsters via ros topic and depending on the hitpoints of the
opponent, strategize his attack (manually) and send his move to the main
server via another ros topic.  
❖ The main server will receive the attacks from Players and will also send the
updated monster hit points before each round begins. It will also end the
game once one of the Players wins.  

## Dependencies
rospy, std_msgs

## Workflow
The 2 states of the System can be visualized from their RQT graphs:
### Listening to Client A
![listening to A](https://github.com/user-attachments/assets/291634ea-1807-46cf-bd26-ffe6187a3ebd)
### Listening to Client B
![listening to B](https://github.com/user-attachments/assets/620a0597-717d-426d-8c90-4a4e228e0d62)


