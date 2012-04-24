'''
Created on Jan 31, 2012

@author: matthias
'''
from etsproxy.mayavi.core.api import PipelineBase
from etsproxy.mayavi.core.ui.api import MayaviScene, SceneEditor, \
    MlabSceneModel
from etsproxy.mayavi.modules.axes import Axes

from etsproxy.traits.api import HasTraits, Range, Instance, on_trait_change, \
    Trait, Property, Constant, DelegatesTo, cached_property, Str, Delegate, \
    Button, Int, Bool, File, Array, List, Float

from etsproxy.traits.ui.api import \
    View, Item, Group, ButtonEditor, RangeEditor, VGroup, HGroup, HSplit, Tabbed, \
    ViewSubElement, VGrid, Include, TreeEditor, TreeNode, Handler, ListEditor
from etsproxy.mayavi import mlab
from etsproxy.mayavi.core.api import Engine

from etsproxy.tvtk.api import tvtk

from etsproxy.mayavi.sources.vtk_data_source import VTKDataSource
from etsproxy.mayavi.modules.surface import Surface

import tempfile
import os
import numpy as np
import string


class OwnObject(HasTraits):
    opacity_min = Int(0)
    opacity_max = Int(100)
    
    opacity = Int(20)
    
    @on_trait_change('opacity')
    def changed_opacity(self):
        print 'opacity changed to:', self.opacity
    
    view = View(Item('opacity', editor = RangeEditor(low_name = 'opacity_min',
                                                        high_name = 'opacity_max',
                                                        format = '(%s)',
                                                        auto_set = False,
                                                        enter_set = False,
                                                        )),
                
                   
                   dock = 'vertical')
