import sys
sys.path.insert(0, 'evoman')
from environment import Environment
from controller import player_controller

import os
import numpy as np
import matplotlib.pyplot as plt
import config as C

os.environ["SDL_VIDEODRIVER"] = "dummy"

def get_run_number(filename):
    return int(filename.split('.')[0].split('_')[-1][-1])


def generateBoxPlot(my_dict):
    plt.title("Box Plot: Individual Gains of the EAs")
    plt.ylabel("Individual Gain")
    plt.xlabel("Evolutionary Algorithm")
    plt.boxplot(my_dict.values())
    plt.xticks([x for x in range(1,len(my_dict)+1)], my_dict.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.4)
    plt.savefig(f'box_plot_({",".join(my_dict.keys())}).png')
    
def get_box_plot_values(cfg_object):
    
    if not os.path.exists(cfg_object.experiment_name):
        os.makedirs(cfg_object.experiment_name)

    # initializes simulation in individual evolution mode, for single static enemy.
    env = Environment(experiment_name=cfg_object.experiment_name,
                enemies=[cfg_object.enemy_id],
                playermode="ai",
                player_controller=player_controller(cfg_object.n_hidden_neurons),
                enemymode="static",
                level=2,
                speed="fastest",
                randomini='yes')

    directory = cfg_object.experiment_name+'/'+'best/'
    best_run_gain_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            bsol = np.loadtxt(filepath)
            print( f'\n RUNNING SAVED BEST SOLUTION 5 TIMES FOR {filepath}\n')
            gain = []
            for test in range(1,6):
                #Test this specific individiual 5 times
                f,p,e,_ = env.play(np.array(bsol))
                gain.append(p-e)
        
        #Add RUN number to mean fitness dict
        run_no = get_run_number(filename)
        # best_run_fitness_dict[run_no] = round(float(sum(fit) / len(fit)), 2)
        best_run_gain_dict[run_no] = round(float(sum(gain) / len(gain)), 2)
        
    return best_run_gain_dict

    
if __name__ == "__main__":
    cfg_gains_dict = {}
    cfg_names = ['enemy2_nm', 
               'enemy2_wm',
                'enemy5_nm', 
                'enemy5_wm',
                'enemy8_nm',
                'enemy8_wm']
    
    for cfg in cfg_names:
        cfg_object = getattr(C, cfg)
        
        best_run_gain_dict = get_box_plot_values(cfg_object)
        cfg_gains_dict[cfg_object.experiment_name] = list(best_run_gain_dict.values())
    
    print(cfg_gains_dict)
    generateBoxPlot(cfg_gains_dict)


