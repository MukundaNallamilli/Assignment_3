from matplotlib import pyplot as plt
import numpy as np
from matplotlib_venn import venn2,venn2_unweighted,venn2_circles

p_A = float(input('Enter the value of P(A) ='))
p_B = float(input('Enter the value of P(B) ='))
p_AandB = float(input('Enter the value of p(A and B) ='))
print(f'P(NOT A) = {round(1-p_A,4)}')
print(f'P(NOT B) = {round(1-p_B,4)}')
print(f'P(A OR B) = {round(p_A+p_B - p_AandB,4)}')

v1 = venn2(subsets=(0.26,0.32,0.16), set_labels = ('A', 'B'))
v1.get_patch_by_id('10').set_alpha(1.0)
v1.get_patch_by_id('10').set_color('white')
v1.get_patch_by_id('11').set_alpha(1.0)
v1.get_patch_by_id('11').set_color('white')
v1.get_patch_by_id('01').set_alpha(1.0)
v1.get_patch_by_id('01').set_color('skyblue')
c1 = venn2_circles(subsets=(0.26,0.32,0.16), linestyle='dashed')
c1[0].set_lw(1.5)
#size of dotted line
c1[0].set_ls('dotted')
plt.title("P (NOT A)")
plt.gca().set_facecolor('skyblue')
plt.gca().set_axis_on()
plt.text(-0.7,0.3, '0.26')
plt.show()



