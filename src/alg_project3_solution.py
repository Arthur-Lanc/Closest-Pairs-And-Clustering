"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))

def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    result_tuple = (float('inf'),-1,-1)
    for idx_i in range(len(cluster_list)):
        for idx_j in range(len(cluster_list)):
            if idx_i != idx_j:
                temp_tuple = pair_distance(cluster_list,idx_i,idx_j)
                #cluster_dist = cluster_list[idx_i].distance(cluster_list[idx_j])
                if temp_tuple[0] < result_tuple[0]:
                    result_tuple = temp_tuple
    return result_tuple

def closest_pair_strip(cluster_list, mid, width):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    s_list = []
    for idx in range(len(cluster_list)):
        if abs(cluster_list[idx].horiz_center()-mid) < width:
            s_list.append(idx)
    s_list.sort(key = lambda idx: cluster_list[idx].vert_center())
    #cluster_list.sort(key = lambda cluster: cluster.vert_center())
    len_k = len(s_list)
    result_tuple = (float('inf'),-1,-1)
    for idx_u in range(0,len_k-2+1):
        for idx_v in range(idx_u+1,min(idx_u+3,len_k-1)+1):
            idx_i = s_list[idx_u]
            idx_j = s_list[idx_v]
            temp_tuple = pair_distance(cluster_list,idx_i,idx_j)
            #cluster_dist = cluster_list[idx_i].distance(cluster_list[idx_j])
            if temp_tuple[0] < result_tuple[0]:
                result_tuple = temp_tuple
    return result_tuple


def fast_closest_pair(cluster_list):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's_list vertical center line
    half_width is the half the width of the strip (idx_i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    len_n = len(cluster_list)
    if len_n <= 3:
        result_tuple = slow_closest_pair(cluster_list)
    else:
        idx_m = int(math.floor(len_n/2.0))
        cluster_list_l = cluster_list[:idx_m]
        cluster_list_r = cluster_list[idx_m:]
        distance_tuple_l = fast_closest_pair(cluster_list_l)
        distance_tuple_r = fast_closest_pair(cluster_list_r)
        if distance_tuple_l[0] < distance_tuple_r[0]:
            result_tuple = distance_tuple_l
        else:
            result_tuple = (distance_tuple_r[0],distance_tuple_r[1]+idx_m,distance_tuple_r[2]+idx_m)
        mid = (cluster_list[idx_m-1].horiz_center()+cluster_list[idx_m].horiz_center())/2.0
        cps_tuple = closest_pair_strip(cluster_list,mid,result_tuple[0])
        if cps_tuple[0] < result_tuple[0]:
            result_tuple = cps_tuple
    return result_tuple


def hierarchical_clustering(cluster_list, cluster_num_k):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > cluster_num_k:
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        cp_tuple = fast_closest_pair(cluster_list)
        #cp_tuple = slow_closest_pair(cluster_list)
        idx_i = cp_tuple[1]
        idx_j = cp_tuple[2]
        new_cluster = cluster_list[idx_i].merge_clusters(cluster_list[idx_j])
        cluster_list.pop(idx_i)
        cluster_list.pop(idx_j-1)
        cluster_list.append(new_cluster)
    return cluster_list


def kmeans_clustering(cluster_list, len_k, iter_times_q):
    """
    Compute the len_k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
            
    cluster_list_copy = list(cluster_list)
    cluster_list_copy.sort(key = lambda cluster: cluster.total_population(),reverse=True)
    miu = []
    for idx_f in range(len_k):
        miu.append((cluster_list_copy[idx_f].horiz_center(),cluster_list_copy[idx_f].vert_center()))

    for dummy_i in range(iter_times_q):
        k_cluster_list = []
        nk_cluster_list = []
        for idx_x in range(len_k):
            temp_cluster = alg_cluster.Cluster(set(),float(miu[idx_x][0]),float(miu[idx_x][1]),int(0),float(0))
            k_cluster_list.append(temp_cluster)
            temp_cluster = alg_cluster.Cluster(set(),float(0),float(0),int(0),float(0))
            nk_cluster_list.append(temp_cluster)

        for idx_j in range(len(cluster_list)):
            min_distance = float('inf')
            idx_l = -1
            for idx_f in range(len_k):
                temp_distance = cluster_list[idx_j].distance(k_cluster_list[idx_f])
                if temp_distance <= min_distance:
                    min_distance = temp_distance
                    idx_l = idx_f
            nk_cluster_list[idx_l].merge_clusters(cluster_list[idx_j])

        miu = []
        for idx_f in range(len_k):
            miu.append((nk_cluster_list[idx_f].horiz_center(),nk_cluster_list[idx_f].vert_center()))
    
    return nk_cluster_list

