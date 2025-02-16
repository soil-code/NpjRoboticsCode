import numpy as np

def get_weight(z, CM):
    return CM[:, z+3]

def shift(R_dist, action):
    if action > 0:
        R_dist = np.concatenate((np.zeros(abs(action)), R_dist), axis=0)
        R_dist = R_dist[:-action]
    else:
        R_dist = np.concatenate((R_dist, np.zeros(abs(action))), axis=0)
        R_dist = R_dist[-action:]

    return R_dist

# define variables
states_set = [-3, -2, -1, 0, 1, 2, 3]
M = 7
CM = np.array([[55,  0,  0,  0,  0,  0,  0],
               [ 1, 53,  1,  0,  0,  0,  0],
               [ 0,  1, 54,  0,  0,  0,  0],
               [ 0,  0,  1, 53,  1,  0,  0],
               [ 0,  0,  0,  1, 53,  1,  0],
               [ 0,  0,  0,  0,  1, 52,  0],
               [ 0,  0,  0,  0,  0,  1, 54]])

sum_row = np.dot(CM, np.ones((7, 1)))
CM_rc = CM / sum_row

R_dist = np.ones(7) / 7
action = 0
while True:
    R_dist_ = np.concatenate((np.zeros(7), R_dist, np.zeros(7)), axis=0)
    R_dist_ = shift(R_dist_, -action)

    # get measurement & probability
    v = int(input('Enter the measurement result: '))
    Omega = get_weight(v, CM_rc)

    R_dist = R_dist_[7:14]
    R_dist = np.dot(Omega.T, np.diag(R_dist))
    R_dist = R_dist / np.sum(R_dist)

    idx = np.argmax(R_dist)
    rlb = R_dist[idx]
    action = (idx - 3)
    print(f"RLB: {rlb}")
    print(f"Next Action: {action}")
    print(R_dist)