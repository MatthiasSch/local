'''
Created on Dec 7, 2011

@author: matthias
'''

from enthought.traits.api import HasTraits, Property, cached_property, Event, \
    Array, Instance, Int, Directory, Range, on_trait_change, Bool, Trait, Constant, \
    Tuple, Interface, implements, Enum, List, Float
    

from enthought.traits.ui.api import \
    View, Item, Group, ButtonEditor, RangeEditor, VGroup, HGroup, HSplit, Tabbed, \
    ModelView
    
from enthought.mayavi.core.ui.api import MayaviScene, SceneEditor, \
    MlabSceneModel
    
from enthought.mayavi.core.api import PipelineBase

class CreasePattern(HasTraits):
    
    pass

class CreasePatternView(ModelView):

    model = Instance(CreasePattern)
    def _model_default(self):
        return CreasePattern()
    
    # plotting stuff
    scene = Instance(MlabSceneModel, ())
    show_cnstr = Bool(True)
    fold_step = Int(0)

    plot = Property(Instance(PipelineBase))
    @cached_property
    def _get_plot(self):
        print 'creating plot'
        

    # when parameters are changed, plot is updated
    @on_trait_change('fold_step, show_cnstr')
    def update_plot(self):
        print self.plot
        print 'updating plot'
        
    # The layout of the dialog created
    view = View(
                HSplit(Group(
                             Group(Item('show_cnstr'),),
                             id = 'creasepatternview.animation',
                             dock = 'tab'
                             ),
                              
                      VGroup(
                             Item('scene', editor = SceneEditor(scene_class = MayaviScene),
                                  show_label = False),
                             Item('fold_step'),
                             id = 'creasepatternview.mayavi',
                             dock = 'tab'
                             ),
                      
                       
                        ),
                      
                dock = 'tab',
                resizable = True,
                id = 'creaspatternview',
                width = 1.0,
                height = 1.0
                )
    
if __name__ == '__main__':
    cp = CreasePattern()
    cpv = CreasePatternView(model = cp, show_cnstr = False)
    #cpv.configure_traits()
