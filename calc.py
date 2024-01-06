import numpy as np

arr = [3.770,
3.448,
3.571,
3.647,
3.914,
3.886,
3.804,
3.555,
3.829]
arr = np.array(arr)

print(np.mean(arr), np.std(arr))

# CFR -- IHDP - ERM

# ATE-In  : 3.8102222222222224 +/- 0.06841178874657623
# ATE-Out : 3.8657777777777773 +/- 0.0638901449151898

# PEHE-In : 1.741888888888889 +/- 0.0334246896252337
# PEHE-Out: 1.805555555555555 +/- 0.024395405355704457

# _________________________________________________________

# IHDP - FISH -- META-LR : 0.4

# ATE-In  : 3.9008888888888884 +/- 0.08643358972123495
# ATE-Out : 3.942555555555556  +/- 0.10038715180197895

# PEHE-In : 1.712222222222222  +/- 0.0324303622406801
# PEHE-Out: 1.7742222222222221 +/- 0.04286873447002756

# _________________________________________________________

# IHDP - FISH -- META-LR : 0.5

# ATE-In : 3.914888888888888 +/- 0.09864126299592935
# ATE-Out: 3.957777777777777 +/- 0.11143785291241208

# PEHE-In : 1.7062222222222223 +/- 0.030043589731432205
# PEHE-Out: 1.7662222222222224 +/- 0.04202850296796681

# _________________________________________________________

# IHDP - FISH -- META-LR : 0.6

# ATE-In: 3.9268888888888887 +/- 0.10768931077094411
# ATE-Out: 3.968777777777778 +/- 0.11933685076545848

# PEHE-In: 1.7001111111111111 +/- 0.027794661535563682
# PEHE-Out: 1.7591111111111113 +/- 0.040983585994732764