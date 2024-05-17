import numpy as np
import itertools

class Schaeffler_PFD:
    def __init__(self):
        self.problem_name = 'Schaeffler_PFD'
        self.problem_description = 'Problem for milestone meeting with Schaeffler_PFD'
        # self.plotter = np.array([[2,0],[1,3]])
        self.plotter = np.asarray(list(itertools.combinations(np.arange(6), 2)))

    def _compute_commons(self, dv_samples):
        self.var = dv_samples
        pass

    def w_j(self):
        m_gear_est = self.var['N_m'] / 50
        m_motor_est = self.var['tau_m_max'] / 2.5
        self.var['w_j'] =  m_gear_est + m_motor_est

    def l_j(self):
        l_gear_est = self.var['N_m'] / 1000
        l_motor_est = self.var['tau_m_max'] / 100
        self.var['l_j'] =  l_gear_est + l_motor_est

    def tau_j_cont(self):
        tau_j_cont_val = self.var['N_m'] * self.var['tau_m_cont']
        self.var['tau_j_cont'] = tau_j_cont_val


    def tau_j_max(self):
        tau_j_max_val = self.var['N_m'] * self.var['tau_m_max']
        tau_j_max_real = np.min(
            np.column_stack((self.var['N_m']*self.var['K_m'] * self.var['i_max'], tau_j_max_val, self.var['N_peak'])), axis=1
        )
        self.var['tau_j_max'] = tau_j_max_real

    def power_loss(self):
        self.var['power_loss'] = self.var['K_m']*500 + self.var['N_peak']/30

