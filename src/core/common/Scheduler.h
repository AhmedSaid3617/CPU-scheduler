#ifndef SCHEDULER_H
#define SCHEDULER_H

#include <optional>
#include <vector>

#include "TaskEntry.h"

template <typename T>
class Scheduler {

public:
    virtual ~Scheduler() = default;

    /**
     * Reset the state of the scheduler and removes all tasks
     */
    virtual void reset() = 0;

    virtual void load(T task, int burst) = 0;

    virtual void load(std::vector<std::pair<T, int>> tasks) {
        for (auto element: tasks) {
            load(element.first, element.second);
        }
    }

    virtual std::optional<T> schedule() = 0;

    Scheduler(const Scheduler&) = delete;
    Scheduler& operator=(const Scheduler&) = delete;
    Scheduler() = default;
};



#endif //SCHEDULER_H
