'''
Created on Jan 31, 2012

@author: matthias
'''
from enthought.mayavi.core.api import PipelineBase
from enthought.mayavi.core.ui.api import MayaviScene, SceneEditor, \
    MlabSceneModel
from enthought.mayavi.modules.axes import Axes

from enthought.traits.api import HasTraits, Range, Instance, on_trait_change, \
    Trait, Property, Constant, DelegatesTo, cached_property, Str, Delegate, \
    Button, Int, Bool, File, Array, List, Float

from enthought.traits.ui.api import \
    View, Item, Group, ButtonEditor, RangeEditor, VGroup, HGroup, HSplit, Tabbed, \
    ViewSubElement, VGrid, Include, TreeEditor, TreeNode, Handler, ListEditor
from enthought.mayavi import mlab
from enthought.mayavi.core.api import Engine

from enthought.tvtk.api import tvtk

from enthought.mayavi.sources.vtk_data_source import VTKDataSource
from enthought.mayavi.modules.surface import Surface

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
