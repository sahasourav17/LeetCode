class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total_waiting_time = 0
        finishing_time = 0
        
        for arrival_time, required_time in customers:
            if arrival_time < finishing_time:
                finishing_time += required_time
            else:
                finishing_time = arrival_time + required_time
            total_waiting_time += (finishing_time - arrival_time)

        return total_waiting_time / n
