#ifndef TASK_H
#define TASK_H
#include <optional>


template <typename T, typename M = void>
struct TaskEntry {
    T task;
    int burst_time;
    int arrival_time = 0;
    std::optional<M> option;
};



#endif //TASK_H
