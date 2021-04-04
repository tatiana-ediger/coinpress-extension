import numpy as np
import matplotlib.pyplot as plt

#Ratio (Figure 1)
counters = np.loadtxt("./results/synthetic_cov/n-1.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-1.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-1.txt")
ratio = [x/y for x,y in zip(t3, nonpr)]

fig, ax = plt.subplots()
ax.plot(counters, ratio, marker="x", color='#E377C2')
plt.ylim(bottom=1.0)
ax.set_xlabel('n')
ax.set_ylabel('Cost of Privacy')
ax.set_title("Multivariate Covariance Estimation")
plt.savefig('./plots/ratiocov.png')

#Headline comparison plotting (Figure 9)
counters = np.loadtxt("./results/synthetic_cov/n-1.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-1.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-1.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-1.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-1.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-1.txt")
t5 = np.loadtxt("./results/synthetic_cov/t5-1.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.plot(counters, t5, marker="x", label='t = 5', color='#bcbd22')
plt.ylim(0.0,2.0)
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Baseline Comparisons")
ax.legend()
plt.savefig('./plots/cov-1a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.plot(counters, t5, marker="x", label='t = 5', color='#bcbd22')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Baseline Comparisons")
ax.legend()
plt.savefig('./plots/cov-1b.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Baseline Comparisons")
ax.legend()
plt.savefig('./plots/cov-1c.png')

#Increasing K plotting (Figure 11)
counters = np.loadtxt("./results/synthetic_cov/u-2.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-2.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-2.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-2.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-2.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-2.txt")
t5 = np.loadtxt("./results/synthetic_cov/t5-2.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.plot(counters, t5, marker="x", label='t = 5', color='#bcbd22')
ax.set_xlabel('K')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Increasing K")
ax.legend()
ax.set_xscale('log')
plt.savefig('./plots/cov-2a.png')


fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.plot(counters, t5, marker="x", label='t = 5', color='#bcbd22')
ax.set_xlabel('K')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Increasing K")
plt.ylim(0,0.6)
ax.legend()
ax.set_xscale('log')
plt.savefig('./plots/cov-2b.png')

#Low dimension plotting (Figure 12)
counters = np.loadtxt("./results/synthetic_cov/n-3.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-3.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-3.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-3.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-3.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-3.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Low Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-3a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Low Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-3b.png')

#High dimension plotting (Figure 13)
counters = np.loadtxt("./results/synthetic_cov/n-4.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-4.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-4.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-4.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-4.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-4.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("High Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-4a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
plt.ylim(0,2.5)
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("High Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-4b.png')

#Privacy plotting (Figure 14)
counters = np.loadtxt("./results/synthetic_cov/r-5.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-5.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-5.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-5.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-5.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-5.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('rho')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Varying Privacy")
ax.legend()
plt.savefig('./plots/cov-5a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('rho')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Varying Privacy")
ax.legend()
plt.ylim(0.1,3.5)
ax.set_yscale('log')
plt.savefig('./plots/cov-5b.png')

#Headline comparison plotting (Figure 11)
counters = np.loadtxt("./results/synthetic_cov/n-6.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-6.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-6.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-6.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-6.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-6.txt")
t5 = np.loadtxt("./results/synthetic_cov/t5-6.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.plot(counters, t5, marker="x", label='t = 5', color='#bcbd22')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Baseline Comparisons")
ax.legend()
plt.savefig('./plots/cov-6a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Baseline Comparisons")
ax.legend()
plt.savefig('./plots/cov-6b.png')

#Increasing K plotting (Figure 11)
counters = np.loadtxt("./results/synthetic_cov/u-7.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-7.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-7.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-7.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-7.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-7.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('K')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Increasing K")
ax.legend()
ax.set_xscale('log')
plt.savefig('./plots/cov-7a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('K')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Increasing K")
ax.legend()
ax.set_xscale('log')
plt.savefig('./plots/cov-7b.png')

#Low dimension plotting (Figure 12)
counters = np.loadtxt("./results/synthetic_cov/n-8.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-8.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-8.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-8.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-8.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-8.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Low Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-8a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Low Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-8b.png')

#High dimension plotting (Figure 13)
counters = np.loadtxt("./results/synthetic_cov/n-9.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-9.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-9.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-9.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-9.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-9.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("High Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-9a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
plt.ylim(0,5)
ax.set_xlabel('n')
ax.set_ylabel('Mahalanobis error')
ax.set_title("High Dimensional Comparison")
ax.legend()
plt.savefig('./plots/cov-9b.png')

#Privacy plotting (Figure 14)
counters = np.loadtxt("./results/synthetic_cov/r-10.txt")
nonpr = np.loadtxt("./results/synthetic_cov/nonpr-10.txt")
t1 = np.loadtxt("./results/synthetic_cov/t1-10.txt")
t2 = np.loadtxt("./results/synthetic_cov/t2-10.txt")
t3 = np.loadtxt("./results/synthetic_cov/t3-10.txt")
t4 = np.loadtxt("./results/synthetic_cov/t4-10.txt")

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t1, marker="x", label='t = 1', color='#9467bd')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.plot(counters, t3, marker="x", label='t = 3', color='#e377c2')
ax.plot(counters, t4, marker="x", label='t = 4', color='#7f7f7f')
ax.set_xlabel('rho')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Varying Privacy")
ax.legend()
plt.savefig('./plots/cov-10a.png')

fig, ax = plt.subplots()
ax.plot(counters, nonpr, marker="x", label='Non-private', color='#1f77b4')
ax.plot(counters, t2, marker="x", label='t = 2', color='#d62728')
ax.set_xlabel('rho')
ax.set_ylabel('Mahalanobis error')
ax.set_title("Effect of Varying Privacy")
ax.legend()
ax.set_yscale('log')
plt.savefig('./plots/cov-10b.png')

#Europe plotting (Figure 15)
colors = np.loadtxt("./results/europe/colors.txt")
xs = np.loadtxt("./results/europe/xs.txt")
ys = np.loadtxt("./results/europe/ys.txt")
xst1 = np.loadtxt("./results/europe/xst1.txt")
yst1 = np.loadtxt("./results/europe/yst1.txt")
xst2 = np.loadtxt("./results/europe/xst2.txt")
yst2 = np.loadtxt("./results/europe/yst2.txt")
xst3 = np.loadtxt("./results/europe/xst3.txt")
yst3 = np.loadtxt("./results/europe/yst3.txt")
xst4 = np.loadtxt("./results/europe/xst4.txt")
yst4 = np.loadtxt("./results/europe/yst4.txt")
xst5 = np.loadtxt("./results/europe/xst5.txt")
yst5 = np.loadtxt("./results/europe/yst5.txt")

fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
for i in range(len(colors)):
    plt.scatter(xs[i],-ys[i], color = colors[i])
ax.set_title("Non-private projection")
plt.savefig('./plots/eu-np.png')

fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
for i in range(len(colors)):
    plt.scatter(-xst1[i],yst1[i], color = colors[i])
ax.set_title("Private projection, t = 1")
plt.savefig('./plots/eu-t1.png')
    
fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
for i in range(len(colors)):
    plt.scatter(-xst2[i],-yst2[i], color = colors[i])
ax.set_title("Private projection, t = 2")
plt.savefig('./plots/eu-t2.png')

fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
for i in range(len(colors)):
    plt.scatter(xst3[i],-yst3[i], color = colors[i])
ax.set_title("Private projection, t = 3")
plt.savefig('./plots/eu-t3.png')

fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
for i in range(len(colors)):
    plt.scatter(xst4[i],-yst4[i], color = colors[i])
ax.set_title("Private projection, t = 4")
plt.savefig('./plots/eu-t4.png')

fig, ax = plt.subplots()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
for i in range(len(colors)):
    plt.scatter(xst5[i],-yst5[i], color = colors[i])
ax.set_title("Private projection, t = 5")
plt.savefig('./plots/eu-t5.png')
