import numpy as np
from scipy import stats
import itertools


def piecewise(xi,yi):
    z = zip(xi,yi)
    z.sort()

    x = np.array([xs for xs,ys in z])
    y = np.array([ys for xs,ys in z])
    models = []
   
    ## all combinations of models
    i = set(x)
    i = list(i)
    i.sort()

    for ia, ib in itertools.combinations(i,2):
        ya = y[x <= ia]
        yc = y[x >= ib]
        yb = y[(x >= ia) & (x<= ib)]
        xa = x[x <= ia]
        xc = x[x >= ib]
        xb = x[(x >=ia) & (x<= ib)]
        #print xa, xb, xc
        #print ya, yb, yc

        ## models
        a = np.mean(ya)
        slope, intercept, r_value, p_value, std_err = stats.linregress(xb,yb)
        c = np.mean(yc)

        ## error
        se_a = sum(a - ya)**2
        se_c = sum(c - yc)**2
        reg_b = r_value**2
        if slope > 1:
        ## totals
            total_error = (se_a, reg_b, se_c)
            models.append((total_error,(ia,ib,slope, a, c )))
    return models


def best_model(models_all):
    models = [m for m,i in models_all]
    m = np.amax(models, axis=0)
    norml = models/m
    total = np.sum(norml, axis = 1)
    order = np.argsort(total)
    total_error, other = models_all[order[0]]
    a_fit, r, c_fit = total_error
    b_start, b_end, slope, a_mean, c_mean = other
    return  a_mean, a_fit, c_mean, c_fit, b_start, b_end, slope, r

## we want model where 3 numbers are min & longest steady-state

#x = [1,2,3,4,5,6,7]
#y = [0,0,1,6,7,30,30]

x = [3.537162 , 3.537162 , 6.855326,  6.855326 , 0.000000,  0.000000,  0.000000 ,10.675745 , 8.567697 ,10.350374, 10.031677 , 3.118634 , 3.118634,  3.118634,
3.118634  ,3.380266,  3.380266  ,3.380266,  3.380266  ,4.887434,  4.887434  ,4.887434,  4.887434  ,5.689121,  5.689121  ,5.689121 , 5.689121  ,5.790119,
5.790119  ,5.366652 , 5.366652  ,5.366652 , 5.366652  ,5.312184 , 5.312184 , 5.092415 , 5.092415 , 5.965091 , 5.965091 , 5.994593  ,5.994593 , 7.569524,
 7.569524 , 6.585654  ,6.585654 , 6.130869  ,6.130869 , 6.130869  ,6.130869,  4.167229  ,4.167229,  4.167229  ,4.167229,  0.000000 , 0.000000,  0.000000,
 9.272086,  9.272086  ,9.272086,  9.272086  ,4.877234,  4.877234]

y = [0.00000 ,  0.00000,  85.98190  ,93.11778,   0.00000   ,0.00000 ,  0.00000,  82.66497 , 92.43803,  80.52647  ,90.71847,   0.00000   ,0.00000,   0.00000,
0.00000,   0.00000,   0.00000   ,0.00000,   0.00000   ,0.00000,   0.00000,   0.00000   ,0.00000,  24.70786  ,52.45350,  60.31722   ,0.00000,  49.66025,
60.62913 ,  0.00000 ,  0.00000  ,54.50563,  92.61401  , 0.00000 ,  0.00000 , 25.24188  , 0.00000 ,  0.00000 , 54.46697 ,  0.00000  ,90.70662 , 84.62010,
85.97513  , 0.00000  ,72.91498 ,  0.00000, 100.00000 ,  0.00000  ,89.06269  , 0.00000 ,  0.00000  , 0.00000,   0.00000  , 0.00000 ,  0.00000  , 0.00000,
100.00000 ,100.00000 ,100.00000,  99.52622 , 94.73365,   0.00000]

#def gene_expression_matrix(dataset):
#    # open file
#    d =
#    v = d[vnd7]
#    for gene in colnames():
#        ## run davis test
#        y = d[gene]
#        p = piecewise(v,y)
#        a_mean, a_fit, c_mean, c_fit, b_start, b_end, slope, r = best_model(p)
#        ##A_mean, A_fit, B_mean, B_fit, C_start, C_end, Slope, r2, davids_test
#        line = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\n".format(0,1,2,3,4,5,6,7,8)

d = piecewise(x,y)
best_model(d)


#print d
