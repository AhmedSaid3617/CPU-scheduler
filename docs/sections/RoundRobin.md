# RoundRobinScheduler

**Description**:  
This class implements a Round Robin scheduler, where tasks are executed in a cyclic manner with a fixed time quantum. If a task doesn't complete within the time quantum, it's preempted and moved back to the queue.

**Attributes**:  
- `queue`: A queue to store incoming tasks.  
- `time_quantum`: The fixed time slice allocated to each task.  
- `task_time`: Tracks the remaining time for the current task in its time slice.  
- `current_task`: The task currently being executed.  

**Methods**:  

### `__init__(self, timequantum)`  
Initializes the scheduler with a given time quantum.  

**Parameters**:  
- `timequantum`: The fixed time slice for each task.  

---  

### `reset(self, timequantum) -> None`  
Resets the scheduler by clearing the queue and setting a new time quantum.  

**Parameters**:  
- `timequantum`: The new time quantum for scheduling.  

---  

### `run(self, task) -> None`  
Adds a new task to the scheduler's queue.  

**Parameters**:  
- `task`: The task to be enqueued.  

---  

### `schedule(self) -> Task`  
Determines the next task to execute based on Round Robin scheduling.  

**Behavior**:  
- If no tasks are left, returns `None`.  
- If the current task completes or its time slice expires, it is preempted (if unfinished) and the next task is selected.  
- Decrements the burst time of the current task and its remaining time slice.  

**Returns**:  
- The currently executing task or `None` if no tasks remain.  
