from collections import defaultdict

from core.common.Simulator import Simulator


class AreLoadedTasksSatisfied:
    def __init__(self):
        pass

    @staticmethod
    def visit(simulator: Simulator):
        history = simulator.history

        # Obtain burst times in history
        burst = defaultdict(int)
        for step in range(len(history)):
            task = history[step]
            if task is not None:
                burst[task] += 1

        # Make sure all simulator tasks are present in the history
        for task in simulator.tasks:
            if task not in burst:
                return False

        # Make sure tasks in history are satisfied
        for task in burst.keys():
            if task.burst_time != burst[task]:
                return False

        return True



