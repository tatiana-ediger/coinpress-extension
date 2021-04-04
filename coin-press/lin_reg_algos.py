import torch
import algos
import numpy as np


def coinpress_linreg(x, y, beta, c, r, total_budget):
    """
    input:
    output:
    beta_hat = mean_est @ np.inv(cov_est)
    """
    n = len(x)
    d = len(x[0])

    z = []
    for i in range(n):
        z.append(x[i] * y[i])
    z = np.array(z)

    # TODO: private beta_norm_sqr !!
    beta_norm_sqr = np.linalg.norm(beta) ** 2

    mean_est = coinpress_linreg_mean(z, c, r, d, beta_norm_sqr, total_budget)
    cov_est = coinpress_linalg_covariance(x, d, 2, total_budget)
    beta_hat = mean_est @ np.linalg.inv(cov_est)
    return beta_hat


def coinpress_linalg_covariance(x, d, t=2, total_budget=0.5):
    '''need X and args={d, u, rho, t}'''
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


def coinpress_linreg_mean(z, c, r, d, beta_norm_sqr, total_budget=0.5):
    z = z / np.sqrt(2 * beta_norm_sqr + 1)
    rho = [(1.0 / 4.0) * total_budget, (3.0 / 4.0) * total_budget]
    return algos.multivariate_mean_iterative(z, c, r, 2, rho) * np.sqrt(2 * beta_norm_sqr + 1)
