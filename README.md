# Evoman-Specialist_player_agent

<b>Subject:</b> Assignment 2 of Evolutionary Computing Course - Vrije Universiteit Amsterdam, 2021

<b>Task:</b> Evoman (https://www.youtube.com/watch?v=ZqaMjd1E4ZI) is a video game framework inspired on Megaman. The task is to win a particular enemy in the game with the developed model.

To reproduce our results follow the following steps:
1) run pip install -r requirements.txt
2) run python run_experiments.py to run the experiments again
3) run python LinePlotter.py to plot the lines plots 
4) run python Boxplotter.py to plot the box plot

To run a custom experiment :
see config.py and define a new config 
run  python train_specialist.py --cfg_name <name of the config defined in config.py>
