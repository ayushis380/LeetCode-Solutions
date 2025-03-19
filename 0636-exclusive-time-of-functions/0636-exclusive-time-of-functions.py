class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []  # Stack to store (function_id, start_time)
        result = [0] * n  # Store exclusive time for each function
        prev_time = 0  # Track the previous timestamp
        
        for log in logs:
            func_id, event, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)

            if event == "start":
                if stack:
                    # Update time for the function at the top of the stack
                    result[stack[-1][0]] += timestamp - prev_time

                stack.append((func_id, timestamp))
                prev_time = timestamp  # Move prev_time to current start - as the next execution will start from here now

            else:  # event == "end"
                func_id, start_time = stack.pop()
                result[func_id] += (timestamp - prev_time + 1)  # Include end time
                prev_time = timestamp + 1  # Move prev_time to the next time step

        return result