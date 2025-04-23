# Priority_prem_Scheduler (Preemptive Priority)

**Description**:  
This scheduler implements preemptive priority scheduling, where a running task can be interrupted if a new task with a higher priority (lower number) arrives.

**Attributes**:  
- `min_heap`: A min-heap (priority queue) that stores all active tasks.

**Methods**:  

### `__init__(self)`  
Initializes the scheduler with an empty min-heap.  

---  

### `reset(self)`  
Clears the min-heap to reset the scheduler.  

---  

### `run(self, task: Task)`  
Wraps the incoming task as a `Priority_Task` and inserts it into the min-heap.  

**Parameters**:  
- `task`: The task to be added to the scheduler.  

---  

### `rearrange_min_heap(self)`  
Re-applies the heap property to account for any priority or burst changes.  

---  

### `schedule(self) -> Task`  
Picks the task with the highest priority (lowest value).  

**Behavior**:  
- Decrements the burst time of the selected task.  
- If the task is completed, removes it from the heap.  
- Returns the current running task or `None` if no tasks are available.  

**Note**:  
Although the preemptive nature is assumed in the logic (heap reordering at each tick), there’s no explicit interruption of the current task upon arrival of a new one; instead, the task with the highest priority is always chosen dynamically each cycle.  

---

# Priority_non_prem_Scheduler (Non-Preemptive Priority)

**Description**:  
This scheduler implements non-preemptive priority scheduling, where once a task starts execution, it cannot be interrupted, even if a higher-priority task arrives.

**Attributes**:  
- `min_heap`: Stores all queued tasks based on priority.  
- `current_task`: Stores the task currently being executed.  

**Methods**:  

### `__init__(self)`  
Initializes the scheduler with an empty heap and no active task.  

---  

### `reset(self)`  
Resets the scheduler by clearing all state.  

---  

### `run(self, task: Task)`  
Inserts a new task into the min-heap.  

**Parameters**:  
- `task`: The task to be added to the scheduler.  

---  

### `rearrange_min_heap(self) -> Task`  
Sorts the heap to ensure the task with the highest priority is accessible, then returns it.  

---  

### `schedule(self) -> Task`  
If no task is running, selects the task with the highest priority.  

**Behavior**:  
- Continues running the `current_task` until completion.  
- Once finished, removes the task and starts the next one if available.  
- Returns the active task for that clock tick or `None` if idle.  