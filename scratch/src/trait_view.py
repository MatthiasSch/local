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

from OwnObject import OwnObject

class MainClass(HasTraits):
    list_object = Property(List(OwnObject))
    def _get_list_object(self):
        print 'build list'
        own1 = OwnObject()
        own2 = OwnObject()
        own3 = OwnObject()
        mylist = [own1, own2, own3]
        print mylist
        return mylist


    view = View(Group(Item('list_object',
                           editor = ListEditor(style = 'custom',
                                               rows = 5))                      
                      ))


    
if __name__ == '__main__':
    mc = MainClass()
    mc.configure_traits()
