import template_matching
from template_matching import Image
#imports
import matplotlib.patches as patches
from sklearn.cluster import KMeans
from PIL import Image as pilimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys, os
import imutils
import copy
import glob
import time
import cv2
#end of imports



path = ".\yolo_cones\data\Combo_img\in5_0002"
image = Image(path)
image.imageMask()
start_time = time.time()
image.imageShowRectHSV()
end_time = time.time()
print("time : {}".format(end_time - start_time))
print('Done')

