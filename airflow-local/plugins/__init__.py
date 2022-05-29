from __future__ import division, absolute_import, print_function
from airflow.plugins_manager import AirflowPlugin

#import modules which was originally your folder containing operators (or other plugins)
#The __init__.py lying within that folder makes your folder a module for Python
import operators

#Define the plugin class
class MyPlugins(AirflowPlugin):
    #Name your AirflowPlugin
    name = "time_diff_plugin"
    #List all plugins you want to use in dag operation
    operators = [operators.TimeDiff]