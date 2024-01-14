import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello()
#
# TO ADD:
  # Search box - https://anvil.works/learn/tutorials/data-grids/searching    ✓
  # Filter by columns
  # present records by Reference Number - descending order.    ✓
  # Consider management password instead of login user?
  # Seperate between Jet/piston
  # think about UX/UI

# Validation - Consult woth Stav Lobel for more tests:
  # Validate Results of power check!!!
  # new power tests
  # wrong engine numbers
  # wrong tail numbers
  # Add engine before removing
  # 

# To Consider:
  # The 'TestsHistory' page became useless after adding the search bar to the other search pages (consider deleting)

# Code refactor:
  # Comments.