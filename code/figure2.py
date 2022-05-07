from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2,venn2_unweighted,venn2_circles

v2 = venn2(subsets=(0.26,0.32,0.16), set_labels = ('A', 'B'))
v2.get_patch_by_id('10').set_alpha(1.0)
v2.get_patch_by_id('10').set_color('skyblue')
v2.get_patch_by_id('11').set_alpha(1.0)
v2.get_patch_by_id('11').set_color('white')
v2.get_patch_by_id('01').set_alpha(1.0)
v2.get_patch_by_id('01').set_color('white')
c2= venn2_circles(subsets=(0.26,0.32,0.16), linestyle='dashed')
c2[1].set_lw(1.5)
#size of dotted line
c2[1].set_ls('dotted')
plt.title("P (NOT B)")
plt.gca().set_facecolor('skyblue')
plt.gca().set_axis_on()
plt.text(-0.7,0.3, '0.26')
plt.show()