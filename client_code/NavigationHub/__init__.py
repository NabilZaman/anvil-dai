from ._anvil_designer import NavigationHubTemplate
import anvil

from .. import navigation

class NavigationHub(NavigationHubTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.PrimaryTabs.tab_titles = list(navigation.tabs.keys())
    self.home_page = properties.get('home_page')
    self.active_tab = None

  def PrimaryTabs_tab_click(self, tab_index, tab_title, **event_args):
    """This method is called when a tab is clicked"""
    # If this tab is already active, deactivate it
    if self.active_tab is not None and self.active_tab == tab_index:
      self.SecondaryTabs.visible = False
      return
    # else, enable the appropriate secondary tabs
    self.active_tab = tab_index
    self.SecondaryTabs.active_tab_index = 0
    self.SecondaryTabs.visible = True
    self.SecondaryTabs.tab_titles = list(navigation.tabs[tab_title])

  def SecondaryTabs_tab_click(self, tab_index, tab_title, **event_args):
    """This method is called when a tab is clicked"""
    primary_tab_name = self.PrimaryTabs.tab_titles[self.active_tab]
    self.Content.visible = True
    self.main_text.font_size = 16
    self.main_text.text = f'This is the {primary_tab_name}/{tab_title} page!'

  def home_nav_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form(self.home_page)


