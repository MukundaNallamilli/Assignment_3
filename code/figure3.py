from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2,venn2_unweighted,venn2_circles

v3 = venn2(subsets=(0.26,0.32,0.16), set_labels = ('A', 'B'))
v3.get_patch_by_id('10').set_alpha(1.0)
v3.get_patch_by_id('10').set_color('skyblue')
v3.get_patch_by_id('11').set_alpha(1.0)
v3.get_patch_by_id('11').set_color('skyblue')
v3.get_patch_by_id('01').set_alpha(1.0)
v3.get_patch_by_id('01').set_color('skyblue')
c3= venn2_circles(subsets=(0.26,0.32,0.16), linestyle='dashed')
c3[0].set_lw(1.5)
#size of dotted line
c3[0].set_ls('dotted')
c3[1].set_lw(1.5)
#size of dotted line
c3[1].set_ls('dotted')
plt.title("P (A OR B)")
plt.gca().set_facecolor('white')
plt.gca().set_axis_on()
plt.text(-0.7,0.3, '0.26')
plt.show()