# SJF_Scheduler

This document describes two types of Shortest Job First (SJF) schedulers: Preemptive and Non-Preemptive.

---

## 1. SJF_prem_Scheduler (Preemptive SJF)

**Description**:  
This class implements a preemptive SJF scheduler, where tasks can be interrupted if a newly arrived task has a shorter burst time.

**Attributes**:  
- `min_heap`: A list that acts as a min-heap to store tasks based on their burst time.

**Methods**:  

### `__init__(self)`  
Initializes the scheduler with an empty heap.

---

### `reset(self) -> None`  
Clears the heap, effectively resetting the scheduler.

---

### `run(self, task: Task) -> None`  
Converts a `Task` into an `SJF_Task` and adds it to the heap.

**Parameters**:  
- `task`: The task to be added to the heap.

---

### `rearrange_min_heap(self) -> None`  
Re-applies the heap property in case burst times change during execution.

---

### `schedule(self) -> Task`  
Picks the task with the smallest remaining burst time.

**Behavior**:  
- Decrements the burst time of the selected task.  
- If a task finishes (burst time reaches 0), it is removed from the heap.  
- Returns the current running task or `None` if the heap is empty.

**Returns**:  
- The currently executing task or `None` if no tasks remain.

---

## 2. SJF_non_prem_Scheduler (Non-Preemptive SJF)

**Description**:  
This class implements a non-preemptive SJF scheduler, where once a task starts execution, it cannot be interrupted until completion.

**Attributes**:  
- `min_heap`: A heap to store incoming tasks.  
- `current_task`: Tracks the currently running task.

**Methods**:  

### `__init__(self)`  
Initializes the scheduler with an empty heap and no active task.

---

### `reset(self) -> None`  
Clears the heap and resets the current task.

---

### `run(self, task: Task) -> None`  
Converts a `Task` into an `SJF_Task` and adds it to the heap.

**Parameters**:  
- `task`: The task to be added to the heap.

---

### `rearrange_min_heap(self) -> Task`  
Re-applies the heap property and returns the top task (i.e., the task with the shortest burst time).

**Returns**:  
- The task with the shortest burst time.

---

### `schedule(self) -> Task`  
Schedules the next task to execute.

**Behavior**:  
- If there's no active task, fetches the shortest task from the heap.  
- Decrements the burst time of the active task.  
- Once the task is completed, removes it from the heap and fetches the next one.  

**Returns**:  
- The currently executing task or `None` if no tasks remain.