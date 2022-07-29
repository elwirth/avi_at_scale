
from global_ import tos_
from src.experiment_analysis.experiment_analysis import table_results
import numpy as np


print(np.logspace(-0.5, -5.0, num=10))

#
# hp_cg_ihb_rev = {'algorithm': 'oavi', 'oracle_type': 'CG', 'term_ordering_strategy': "rev pearson",
#                  'inverse_hessian_boost': 'full'}
#
# hp_cg_ihb = {'algorithm': 'oavi', 'oracle_type': 'CG', 'term_ordering_strategy': tos_,
#              'inverse_hessian_boost': 'full'}
# hp_agd_ihb = {'algorithm': 'oavi', 'oracle_type': 'AGD', 'term_ordering_strategy': tos_,
#               'inverse_hessian_boost': 'full'}
# hp_bpcg_wihb = {'algorithm': 'oavi', 'oracle_type': 'BPCG', 'term_ordering_strategy': tos_,
#                 'inverse_hessian_boost': 'weak'}
# hp_abm = {'algorithm': 'oavi', 'oracle_type': 'ABM', 'term_ordering_strategy': tos_,
#           'inverse_hessian_boost': 'false'}
# hp_vca = {'algorithm': 'vca'}
# hp_svm = {'algorithm': 'svm'}
# hps_no_svm = [hp_cg_ihb, hp_agd_ihb, hp_bpcg_wihb, hp_abm, hp_vca]
# hps = hps_no_svm + [hp_svm]
# data_sets = ['bank', 'credit', 'htru', 'seeds', 'skin', 'spam']
# table_results(data_sets, [hp_cg_ihb, hp_cg_ihb_rev, hp_agd_ihb,], "error_test", ordering=True)
