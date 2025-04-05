from core.common.AreLoadedTasksSatisfied import AreLoadedTasksSatisfied
from core.common.Simulator import Simulator


def is_finished(sim: Simulator) -> bool:
    """
    Check if the simulation is finished.

    :param sim: Simulator instance
    :return: True if all tasks are finished, False otherwise
    """
    return sim.are_all_tasks_loaded() and sim.accept(AreLoadedTasksSatisfied())