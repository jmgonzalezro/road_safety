import pandas as pd
import os
import hydra
from hydra import utils


DF_ACCIDENT=os.environ['ACCIDENT_ROUTE']
DF_ROUTE=os.environ['CASUALITY_ROUTE']
DF_VEHICLE=os.environ['VEHICLE_ROUTE']


