# FCFS_Scheduler

**Description**:  
This class implements a First-Come, First-Served (FCFS) scheduler, where tasks are executed in the order they arrive. Tasks are processed without preemption, ensuring that the first task in the queue is completed before moving to the next.

**Attributes**:  
- `queue`: A FIFO queue to store tasks in the order they are received.  

**Methods**:  

### `__init__(self)`  
Initializes the scheduler with an empty queue.  

---

### `reset(self) -> None`  
Resets the scheduler by clearing the queue.  

**Behavior**:  
- Empties the queue to prepare the scheduler for a new set of tasks.  

---

### `run(self, task: Task) -> None`  
Adds a task to the scheduler's queue multiple times based on its burst time.  

**Parameters**:  
- `task`: The task to be enqueued.  

**Behavior**:  
- For each unit of burst time, the task is added to the queue.  
- Example: A task with a burst time of 8 seconds will be enqueued 8 times.  

---

### `schedule(self) -> Task`  
Determines the next task to execute based on FCFS scheduling.  

**Behavior**:  
- If the queue is empty, returns `None`.  
- Otherwise, retrieves and removes the next task from the queue.  

**Returns**:  
- The next task to execute or `None` if no tasks remain.