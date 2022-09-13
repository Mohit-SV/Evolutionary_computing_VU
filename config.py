from dataclasses import dataclass

@dataclass
class config():
    #all parameters here
    experiment_name: str
    run: int = 10
    enemy_id: int = 2
    ngens: int = 15
    n_hidden_neurons: int = 10
    viz_game: bool = True 
    npop: int = 20
    cxpb: float = 0.6
    mutpb: float = 0.2
    ind_mutpb: float = 0.3
    mutation_step: float = 1



#final configs to run experiments
enemy8_wm = config(experiment_name='enemy8_mutpb0.2', enemy_id=8)
enemy8_nm = config(experiment_name='enemy8_mutpb0', enemy_id=8, mutpb=0)
enemy2_wm = config(experiment_name='enemy2_mutpb0.2', enemy_id = 2)
enemy2_nm = config(experiment_name='enemy2_mutpb0', enemy_id = 2, mutpb=0)
enemy5_wm = config(experiment_name='enemy5_mutpb0.2', enemy_id = 5)
enemy5_nm = config(experiment_name='enemy5_mutpb0', enemy_id = 5, mutpb=0 )


