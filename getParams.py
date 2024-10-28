# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:01:53 2024

@author: k2258346
"""

def runParams():
    
    #get parameters from user
    import getParamsGUI
    paramsResponse=getParamsGUI.getParams()
    
    params = paramsResponse.makeDict()

    
    #find correct slash
    import utils
    directoryPath=utils.selectDir()
    slash = utils.getSlash(directoryPath)
    
    fname='BayesParams'
    utils.saveJson(params,fname,slash,directoryPath)
    
    
    
    
