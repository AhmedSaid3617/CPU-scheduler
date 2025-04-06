from collections import defaultdict

from core.common.Simulator import Simulator


class SchedulerStats:
    def __init__(self):
        pass

    @staticmethod
    def visit(simulator: Simulator):
        history = simulator.history

        # Obtain completion times, burst times, and first run times
        completion = defaultdict(int)
        burst = defaultdict(int)
        first_run = defaultdict(int)
        for step in range(len(history)):
            task = history[step]
            if task is not None:
                completion[task] = step + 1 # +1 because still running, will stop in next step
                burst[task] += 1
                if task not in first_run:
                    # Record the first run time
                    first_run[task] = step

        # Make sure all tasks are satisfied
        for task in burst.keys():
            if task.burst_time != burst[task]:
                raise ValueError(f"Task {task.name} was not completed in the expected time.")

        # Calculate turnaround time
        turnaround = defaultdict(int)
        for task, step in completion.items():
            turnaround[task] = step - task.arr_time

        # Calculate waiting time
        waiting = defaultdict(int)
        for task, t in turnaround.items():
            waiting[task] = t - task.burst_time

        # Calculate response time
        response = defaultdict(int)
        for task, step in first_run.items():
            response[task] = step - task.arr_time

        """
        Turnaround, Waiting and Response for each task
        Aggregated average
        """
        return {
            "turnaround": turnaround,
            "waiting": waiting,
            "response": response,
            "avg_turnaround": sum(turnaround.values()) / len(simulator.tasks),
            "avg_waiting": sum(waiting.values()) / len(simulator.tasks),
            "avg_response": sum(response.values()) / len(simulator.tasks),
        }

