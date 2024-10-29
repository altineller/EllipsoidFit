#!/usr/bin/python

import numpy as np
from ellipsoid_fit import ellipsoid_fit as ellipsoid_fit, data_regularize


if __name__=='__main__':

    filename = 'magf.txt'
    data = np.loadtxt(filename)
    data2 = data_regularize(data)

    center, radii, evecs, v = ellipsoid_fit(data2)

    a,b,c = radii
    r = (a*b*c)**(1./3.)
    D = np.array([[r/a,0.,0.],[0.,r/b,0.],[0.,0.,r/c]])
    TR = evecs.dot(D).dot(evecs.T)

    print('center:\n', center)
    print('transformation:\n', TR)

    np.savetxt('cal_' + filename, np.vstack((center.T, TR)))
