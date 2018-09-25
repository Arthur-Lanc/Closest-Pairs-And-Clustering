import alg_project3_solution
import alg_cluster
import matplotlib.pyplot as plt
import time
import random
import math
import alg_project3_viz

def gen_random_clusters(num_clusters):
    cluster_list = []
    for i in range(num_clusters):
        x = random.choice([-1,1])*random.random()
        y = random.choice([-1,1])*random.random()
        temp_cluster = alg_cluster.Cluster(set(),float(x),float(y),int(0),float(0))
        cluster_list.append(temp_cluster)
    return cluster_list

def question1_plot():
    xvals = []
    slow_cp_yvals = []
    fast_cp_yvals = []
    for num_clusters in range(2,200+1):
        xvals.append(num_clusters)
        grc = gen_random_clusters(num_clusters)

        start = time.clock()
        alg_project3_solution.slow_closest_pair(grc)
        elapsed = (time.clock() - start)
        slow_cp_yvals.append(elapsed)

        start = time.clock()
        alg_project3_solution.fast_closest_pair(grc)
        elapsed = (time.clock() - start)
        fast_cp_yvals.append(elapsed)

    plt.plot(xvals, slow_cp_yvals, '-b', label='slow_closest_pair')
    plt.plot(xvals, fast_cp_yvals, '-r', label='fast_closest_pair')
    plt.legend(loc='upper right')
    plt.xlabel('number of initial clusters ')
    plt.ylabel('running time')
    plt.title('desktop Python')
    plt.grid(True)
    plt.show()


#question1
#question1_plot()
#question2
#alg_project3_viz.run_example()
# #question3
# alg_project3_viz.run_example()
#question4
# kmeans_clustering is much more faster than the hierarchical_clustering.
# the running time of hierarchical_clustering is O(n^2(logn)^2),but kmeans_clustering is O(n)

#question5
#alg_project3_viz.run_example()
#question6
# alg_project3_viz.run_example()
#question7
# Loaded 111 data points
# Displaying 9 hierarchical clusters
# distortion: 1.75163886916e+11
# hierarchical clusters distortion: 1.752×10**11

# Loaded 111 data points
# Displaying 9 k-means clusters
# distortion: 2.71254226924e+11
# k-means clusters distortion: 2.713×10**11

#question8
# The clusterings generated in Q5 is lower distortion than Q6.
# From image in q5, we can find that each point in the same cluster is closer 
# and the shape of the clusters is smaller area on the west coast of the USA.
# The reason cause image in q6 has a much higher distortion is that 
# k-means clustering generates its initial clustering correspond to the countie's populations.
# If there are two counties both have large population, 
# even tough they are closed, 
# k-means clustering would create two cluster in closed position when the iteration num is small.
#question9
# hierarchical clustering
#question10
alg_project3_viz.question10_plot(alg_project3_viz.DATA_111_URL)
alg_project3_viz.question10_plot(alg_project3_viz.DATA_290_URL)
alg_project3_viz.question10_plot(alg_project3_viz.DATA_896_URL)
#question11
# In 111 data set,hierarchical clustering can product lower distortion in the range 6 to 20
#Overall evaluation (optional, no credit)
# k-means clustering, because it is much more faster when data set become large.
# k-means clustering is much more efficiently than hierarchical clustering.
# hierarchical clustering requires less human supervision to generate reasonable clusterings, because k-means clustering can be affect by the initial clusters.
# hierarchical clustering generates clusterings with less error when the data is small, but when the data become large, kmeans_clustering distortion become closer to hierarchical clustering distortion.
##########################################
# print gen_random_clusters(1)
# print ''
# print gen_random_clusters(3)
# print ''
# print gen_random_clusters(5)

#alg_project3_viz.run_example()