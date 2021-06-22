import numpy as np
import scipy as sp


class kicksys():

    """
    This class allows the user to take the matrix of time series spectra
    which have been already masked out appropriately for regions of strong
    telluric absorption and detector artefact (like gaps for example) and apply the
    SysRem algorithm from Mazeh et al. 2007 and obtain the correction factor for systematics
    occuring linearly in the time series spectra due to instrument, tellurics, stellar absorption, etc.
    and ideally preserve the planet signals after an optimum number of iteration.


    Parameters
    ----------
    specmat : 2D matrix of spectra with the shape as time x wavelength, necessary
    specmat_err : 2D matrix of spectra error (e.g. those derived from optimal extraction, will
    be used as a denominator in the expression sysrem minimizes.), necessary

    """

    def __init__(self, specmat = None, specmat_err = None):

        self.specmat = specmat
        self.specmat_err = specmat_err










