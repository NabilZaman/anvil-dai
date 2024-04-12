from ._anvil_designer import HomeTemplate
import anvil

from ..NavigationHub import NavigationHub

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self._hub_form = None

    # Any code you write here will run before the form opens.

  @property
  def navigation_form(self):
    if self._hub_form is None:https://github.com/NabilZaman/anvil-dai.git
      self._hub_form = NavigationHub(home_page=self)
    return self._hub_form
  
  def to_navigation_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form(self.navigation_form)
