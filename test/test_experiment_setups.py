import unittest
from src.auxiliary_functions.auxiliary_functions import HiddenPrints
from src.experiment_setups.experiment_setups import ExperimentSetups
import cupy as cp
import numpy as np


class TestExperimentSetups(unittest.TestCase):

    def test_evaluate(self):
        """Tests whether ExperimentSetups() behaves as intended."""

        Cs = [1, 1.5]
        hyperparameters_vca = {"algorithm": "vca", "psi": [0.5], "C": Cs}
        hyperparameters_avi = {"algorithm": "avi", "psi": [0.5], "tau": [0], "C": Cs}
        hyperparameters_pcgavi = {"algorithm": "oavi", "oracle_type": "PCG", "term_ordering_strategy": "pearson",
                                  'inverse_hessian_boost': "false", "psi": [0.1], "C": Cs}
        hyperparameters_cgavi = {"algorithm": "oavi", "oracle_type": "CG", "term_ordering_strategy": "pearson",
                                  'inverse_hessian_boost': "full", "psi": [0.1], "C": Cs}
        hyperparameters_agdavi = {"algorithm": "oavi", "oracle_type": "AGD", "term_ordering_strategy": "pearson",
                                  'inverse_hessian_boost': "full", "psi": [0.1], "C": Cs}

        hyperparameters_svm = {"algorithm": "svm", "C": Cs, "degree": [5]}
        cp.random.seed(19)
        np.random.seed(19)
        for name in ['bank']:
            for hyperparameters in [hyperparameters_pcgavi, hyperparameters_cgavi, hyperparameters_agdavi,
                                    hyperparameters_avi, hyperparameters_vca, hyperparameters_svm]:
                for i in range(0, 1):
                    pc = ExperimentSetups(name, hyperparameters)
                    with HiddenPrints():
                        res = pc.cross_validation(saving=False)
