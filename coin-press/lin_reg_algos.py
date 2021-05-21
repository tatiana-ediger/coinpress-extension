import torch
import algos
import numpy as np

    
def coinpress_linreg(x, y, beta, c, r, total_budget):
    '''
    input:
    output:
    beta_hat = mean_est
    '''
    n = len(x)
    d = len(x[0])

    z = []
    for i in range(n):
        z.append(x[i] * y[i])
    z = np.array(z)

    beta_norm_sqr =  beta_l2_norm(y, total_budget * 0.2) #np.linalg.norm(beta) ** 2 
    mean_est = coinpress_linreg_mean(z, c, r, d, beta_norm_sqr, total_budget * 0.8)
    
    return mean_est


def coinpress_linreg_mean(z, c, r, d, beta_norm_sqr, total_budget=0.5):
    z = z / np.sqrt(max(2 * beta_norm_sqr + 1, 0.1))
    rho = [(1.0 / 4.0) * total_budget, (3.0 / 4.0) * total_budget]
    return algos.multivariate_mean_iterative(z, c, r, 2, rho) * np.sqrt(max(0, 2 * beta_norm_sqr + 1))



def coinpress_linreg_covariance(x, d, t=2, total_budget=0.5):
    # need X and args={d, u, rho, t}
    x = torch.FloatTensor(x)

    class Args:
        def __init__(self, n, d, u, rho, t):
            self.n = n
            self.d = d
            self.u = u
            self.rho = rho
            self.t = t

    n = len(x)
    rho = [(1.0 / 4.0) * total_budget, (3.0 / 4.0) * total_budget]
    u = 10 * np.sqrt(d)
    args = Args(n, d, u, rho, t)
    return algos.cov_est(x, args)



def beta_l2_norm(y, total_budget):
    '''need y and args={d, u, rho, t}'''
    d = 1
    n = len(y)
    t = 2 # number of times to run cov estimation one-step

    torch_y = torch.FloatTensor(y.reshape(n,1))

    class Args:
        def __init__(self, n, d, u, rho, t):
            self.n = n
            self.d = d
            self.u = u
            self.rho = rho
            self.t = t


    rho = [(1.0 / 4.0) * total_budget, (3.0 / 4.0) * total_budget]
    u = 100 * d
    args = Args(n, d, u, [(1.0 / 4.0) * total_budget, (3.0 / 4.0) * total_budget], t)
    cov_est = algos.cov_est(torch_y, args).numpy()
    return cov_est[0][0] - 1