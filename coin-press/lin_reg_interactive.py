import torch
import lin_reg_algos
import numpy as np


def losses(n_values, d, iters, total_privacy_budget, beta_mean=0, beta_var=1.0):
    """
    returns excess loss of the private, coinpress linear regression solution
    and excess loss for the closed form solution of linear regression.

    where excess loss = E[(<x,beta_hat> - y)**2 - (<x,beta> - y)**2]
    """
    c = [0] * d
    r = 100 * np.sqrt(d)

    nonpriv_excess_losses = []
    priv_excess_losses = []

    for n in n_values:
        nonpriv_losses_for_n = []
        priv_losses_for_n = []

        for i in range(iters):
            underlying_dist = generate_normal_underlying_dist(d, beta_mean, beta_var)
            x, y, z = generate_data(n, d, underlying_dist)

            priv_beta_hat = lin_reg_algos.coinpress_linreg(x, y, underlying_dist, c, r, total_privacy_budget)
            priv_losses_for_n.append(loss(priv_beta_hat, underlying_dist[0], d))

            nonpriv_beta_hat = linreg_closed_form_solution(x, y)
            nonpriv_losses_for_n.append(loss(nonpriv_beta_hat, underlying_dist[0], d))

        priv_losses_for_n = np.array(priv_losses_for_n)
        priv_excess_losses.append(np.mean(priv_losses_for_n))
        nonpriv_losses_for_n = np.array(nonpriv_losses_for_n)
        nonpriv_excess_losses.append(np.mean(nonpriv_losses_for_n))

    return priv_excess_losses, nonpriv_excess_losses


def generate_normal_underlying_dist(d, beta_mean, beta_var):
    """ generates beta, <X,beta> = y"""
    underlying_dist = np.random.normal(beta_mean, beta_var, (1, d))
    return np.array(underlying_dist)


def generate_data(n, d, underlying_dist):
    """Creates an nxd matrix X, a 1xd underlying_dist vector, nx1 y vector, and nxd z vector (where zi=xi*yi)"""

    # generate an n x d data matrix with N(0,1) entries- feature matrix
    X = np.random.normal(0, 1.0, (n, d))
    X = np.array(X)

    # Generates a label vector from underlying distribution plus some noise
    y = []
    for i in range(n):
        y.append(np.dot(underlying_dist, X[i])[0] + np.random.normal(0, 1))
    y = np.array(y)

    # Generate z = xy
    z = []
    for i in range(n):
        z.append(X[i] * y[i])
    z = np.array(z)

    return X, y, z


def linreg_closed_form_solution(x, y):
    return np.linalg.inv(x.T @ x) @ x.T @ y


def excess_loss(beta_hat, beta, d):
    """
    Generate 1000 d-dimensional x values and y values to test excess loss
    of our predicted beta_hat vs. underlying distribution beta
    """

def loss(beta_hat, beta, d):
    
    # make trimmed mean? throw out 5 most extreme values?
    
    n = 1000
    
    '''generate new x values'''
    x = np.random.normal(0, 1.0, (n, d))
    x = np.array(x)
    y = []

    '''generate new y values based on underlying distribution, beta'''
    for i in range(n):
        y.append(np.dot(beta, x[i]) + np.random.normal(0, 1.0))
    y = np.array(y)
    
    '''find squared accuracy of prediction for each entry of x'''
    def dist(xi,yi):
        return (xi @ beta_hat - yi) ** 2 #np.clip((xi @ beta_hat - yi) ** 2, -5, 5) #
    
    '''return MSE'''
    losses = list(map(dist, x, y))
    return np.mean(np.array(losses))
