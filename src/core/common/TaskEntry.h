#ifndef TASK_H
#define TASK_H


template <typename T>
struct TaskEntry {
public:
    T task;
    int burst_time;
    int arrival_time = 0;
};



#endif //TASK_H
