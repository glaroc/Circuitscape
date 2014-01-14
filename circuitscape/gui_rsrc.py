GUI_RSRC = {'application':{'type':'Application',
          'name':'Minimal',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':u'Circuitscape',
          'size':(1005, 670),
          'backgroundColor':(230, 230, 230),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileLoadLast',
                   'label':u'Load settings from last run\tCtrl+L',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileLoadPrev',
                   'label':u'Load settings from file\tCtrl+O',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileSave',
                   'label':'Save settings\tCtrl+S',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileVerifyCode',
                   'label':'Verify code',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileRunBatch',
                   'label':'Run in batch mode',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuOptions',
             'label':'&Options',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuOptionsMoreOptions',
                   'label':'&More settings && inputs...',
                  },
              ]
             },
             {'type':'Menu',
             'name':'menuHelp',
             'label':'&Help',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuHelpManual',
                   'label':'Circuitscape User Guide',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpFeedback',
                   'label':'Discuss / Provide Feedbacks',
                  },
                  {'type':'MenuItem',
                   'name':'menuHelpAbout',
                   'label':'About Circuitscape...',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'CheckBox', 
    'name':'printTimingsBox', 
    'position':(384, 381), 
    'size':(169, 20), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'label':'Log completion times', 
    },

{'type':'Choice', 
    'name':'dataTypeChoice', 
    'position':(27, 54), 
    'size':(250, -1), 
    'font':{'faceName': 'Lucida Grande', 'family': 'default', 'size': 12}, 
    'items':[u'(Choose your data type)', u'Raster', u'Network (graph)'], 
    'stringSelection':'(Choose your data type)', 
    },

{'type':'Choice', 
    'name':'scenarioChoice', 
    'position':(26, 107), 
    'size':(467, -1), 
    'font':{'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 12}, 
    'items':[u'(Choose a modeling mode)', u'Pairwise: iterate across all pairs in focal node file', u'Advanced: activate independent sources and grounds', u'One-to-all (seldom used; see user guide)', u'All-to-one (seldom used; see user guide)'], 
    'stringSelection':'(Choose a modeling mode)', 
    },

{'type':'Choice', 
    'name':'scenarioChoiceNetwork', 
    'position':(27, 107), 
    'size':(458, -1), 
    'font':{'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 12}, 
    'items':[u'(Choose a modeling mode)', u'Pairwise: iterate across all pairs in focal node file', u'Advanced: activate independent sources and grounds'], 
    'stringSelection':'(Choose a modeling mode)', 
    },

{'type':'TextField', 
    'name':'habitatFile', 
    'position':(27, 195), 
    'size':(346, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a resistance map or network/graph file)', 
    },

{'type':'Button', 
    'name':'habitatBrowse', 
    'position':(379, 194), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'CheckBox', 
    'name':'useConductancesBox', 
    'position':(27, 223), 
    'size':(437, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Data represent conductances instead of resistances', 
    },

{'type':'TextField', 
    'name':'srcTargetFile', 
    'position':(27, 314), 
    'size':(363, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a file with focal points [fastest] or regions)', 
    },

{'type':'Button', 
    'name':'srcTargetBrowse', 
    'position':(395, 315), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'StaticText', 
    'name':'parallelizeText', 
    'position':(29, 345), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Number of parallel processors to use: ', 
    },

{'type':'Spinner', 
    'name':'parallelSpin', 
    'position':(305, 343), 
    'size':(48, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'max':100, 
    'min':1, 
    'value':1, 
    },

{'type':'TextField', 
    'name':'currentSrcFile', 
    'position':(535, 88), 
    'size':(363, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a current source file)', 
    },

{'type':'Button', 
    'name':'currentSrcBrowse', 
    'position':(905, 87), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'TextField', 
    'name':'gndFile', 
    'position':(535, 142), 
    'size':(363, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'text':'(Browse for a ground point file)', 
    },

{'type':'Button', 
    'name':'gndBrowse', 
    'position':(905, 141), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'CheckBox', 
    'name':'useGroundConductancesBox', 
    'position':(539, 170), 
    'size':(437, 21), 
    'font':{'faceName': u'Arial', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'label':'Data represent conductances instead of resistances to ground', 
    },

{'type':'TextField', 
    'name':'outFile', 
    'position':(536, 258), 
    'size':(346, 21), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'text':'(Choose a base name for output files)', 
    },

{'type':'Button', 
    'name':'outBrowse', 
    'position':(888, 257), 
    'size':(-1, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Browse', 
    },

{'type':'CheckBox', 
    'name':'curMapBox', 
    'position':(546, 316), 
    'size':(128, 20), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'label':'Current maps', 
    },

{'type':'CheckBox', 
    'name':'voltMapBox', 
    'position':(546, 340), 
    'size':(116, 20), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'label':'Voltage maps', 
    },

{'type':'Button', 
    'name':'calcButton', 
    'position':(857, 321), 
    'size':(100, 23), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'label':'RUN', 
    },

{'type':'Choice', 
    'name':'logLevelChoice', 
    'position':(226, 381), 
    'size':(80, -1), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 9}, 
    'items':[u'DEBUG', u'INFO', u'WARN', u'ERROR'], 
    'stringSelection':'INFO', 
    },

{'type':'CheckBox', 
    'name':'logRusageBox', 
    'position':(574, 382), 
    'size':(220, 20), 
    'font':{'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'label':'Log resource usage info', 
    },

{'type':'Button', 
    'name':'clearLogsButton', 
    'position':(848, 379), 
    'size':(75, 23), 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    'label':'Clear log', 
    },

{'type':'StaticText', 
    'name':'DataModelingTypeTitle', 
    'position':(12, 6), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Data type and modeling mode', 
    },

{'type':'TextArea', 
    'name':'logMessages', 
    'position':(13, 413), 
    'size':(965, 184), 
    'editable':False, 
    'font':{'faceName': u'Lucida Grande', 'family': 'default', 'size': 11}, 
    },

{'type':'StaticText', 
    'name':'modelingModeTitle', 
    'position':(27, 86), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Step 2: Choose a modeling mode', 
    },

{'type':'StaticLine', 
    'name':'StaticLine112', 
    'position':(12, 142), 
    'size':(475, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine1', 
    'position':(30, 371), 
    'size':(926, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'logWindowLabel', 
    'position':(43, 384), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Log window', 
    },

{'type':'StaticText', 
    'name':'logLevelText', 
    'position':(180, 384), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Level', 
    },

{'type':'StaticText', 
    'name':'outFileText1', 
    'position':(536, 291), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Output maps to create:', 
    },

{'type':'StaticText', 
    'name':'outputOptions', 
    'position':(523, 215), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Output options', 
    },

{'type':'StaticText', 
    'name':'outFileText', 
    'position':(536, 236), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Base output file name', 
    },

{'type':'StaticText', 
    'name':'gndFileText', 
    'position':(535, 121), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Ground point file ', 
    },

{'type':'StaticText', 
    'name':'srcFileText', 
    'position':(535, 68), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Current source file', 
    },

{'type':'StaticText', 
    'name':'dataTypeTitle', 
    'position':(27, 34), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Step 1: Choose your input data type', 
    },

{'type':'Image', 
    'name':'Image1', 
    'position':(891, -5), 
    'backgroundColor':(230, 230, 230, 255), 
    'file':'', 
    },

{'type':'StaticLine', 
    'name':'StaticLine2', 
    'position':(507, 35), 
    'size':(-1, 328), 
    'layout':'vertical', 
    },

{'type':'StaticText', 
    'name':'srcTargetFileText', 
    'position':(27, 293), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Focal node location file', 
    },

{'type':'StaticText', 
    'name':'CIRCUITSCAPE', 
    'position':(535, 2), 
    'font':{'style': 'bold', 'faceName': u'Arial', 'family': 'sansSerif', 'size': 22}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'CIRCUITSCAPE 4.0', 
    },

{'type':'StaticText', 
    'name':'inputResistanceData', 
    'position':(12, 154), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Input resistance data', 
    },

{'type':'StaticText', 
    'name':'rasterResistanceMapOrNetworkgraph', 
    'position':(27, 174), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Raster resistance map or network/graph', 
    },

{'type':'StaticText', 
    'name':'pairwiseOptionsTitle', 
    'position':(12, 268), 
    'font':{'style': 'bold', 'faceName': u'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Pairwise mode options', 
    },

{'type':'StaticLine', 
    'name':'StaticLine111', 
    'position':(526, 196), 
    'size':(445, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticLine', 
    'name':'StaticLine11', 
    'position':(9, 253), 
    'size':(476, -1), 
    'layout':'horizontal', 
    },

{'type':'StaticText', 
    'name':'BETA', 
    'position':(805, 2), 
    'font':{'style': 'bold', 'faceName': u'Arial', 'family': 'sansSerif', 'size': 22}, 
    'foregroundColor':(128, 128, 192, 255), 
    'text':'BETA', 
    },

{'type':'StaticText', 
    'name':'advancedOptionsTitle', 
    'position':(523, 47), 
    'font':{'style': 'bold', 'faceName': 'Lucida Grande', 'family': 'sansSerif', 'size': 13}, 
    'foregroundColor':(0, 0, 160, 255), 
    'text':'Advanced mode options', 
    },

] # end components
} # end background
] # end backgrounds
} }
