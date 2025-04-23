# Scheduler

**Description**:  
This abstract base class defines the structure for all schedulers implemented in the project. It provides a common interface and enforces the implementation of essential scheduling methods in derived classes.

**Attributes**:  
This class does not define any attributes directly but serves as a blueprint for derived scheduler classes.

**Methods**:  

### `reset(self) -> None`  
An abstract method that resets the state of the scheduler by removing all tasks.  

**Behavior**:  
- Clears all tasks and resets the scheduler to its initial state.  

---

### `run(self, task: Task) -> None`  
An abstract method that loads a single task into the scheduler.  

**Parameters**:  
- `task`: The task to be added to the scheduler.  

---

### `load_bulk(self, tasks: List[Task]) -> None`  
Loads multiple tasks into the scheduler.  

**Parameters**:  
- `tasks`: A list of tasks to be added to the scheduler.  

**Behavior**:  
- Iterates through the list of tasks and adds each one to the scheduler using the `run` method.  

---

### `schedule(self) -> Task`  
An abstract method that determines the next task to execute based on the scheduling algorithm.  

**Behavior**:  
- Returns the task that should currently be executed based on the scheduling policy.  

**Returns**:  
- The next task to execute or `None` if no tasks are available.  

---

**Notes**:  
- This class is abstract and cannot be instantiated directly.  
- Derived classes must implement the `reset`, `run`, and `schedule` methods to define specific scheduling behavior.