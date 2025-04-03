#ifndef FCFS_SCHEDULER_H
#define FCFS_SCHEDULER_H

#include <queue>
#include <common/Scheduler.h>

template <typename T>
class FCFS_Scheduler final : public Scheduler<T> {
    // All contending tasks
    std::queue<T> list;

public:
    void reset() override {
        list = std::queue<T>();
    }

    void load(T task, const int burst) override {
        for (int i = 0; i < burst; ++i) {
            list.push(task);
        }
    }

    std::optional<T> schedule() override {
        if (list.empty()) {
            return std::nullopt;
        }

        T next_task = list.front();

        list.pop();

        return next_task;
    };

    ~FCFS_Scheduler() override = default;
};

#endif //FCFS_SCHEDULER_H
