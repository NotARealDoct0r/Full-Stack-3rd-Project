import time

class Timer:
    # a Timer class
    def __init__(self, time_left=60):
        """
        Initializes the Timer with a specified time duration.
        
        :param time_left: The total time (in seconds) for the timer. Default is 60 seconds.
        """
        self.time_left = time_left
        self._start_time = None

    def start(self):
        """Starts the timer by recording the start time."""
        self._start_time = time.time()

    def get_time_left(self):
        """Calculates the time left based on the elapsed time."""
        if self._start_time is None:
            return self.time_left  # Timer hasn't started yet
        elapsed_time = time.time() - self._start_time
        return max(0, int(self.time_left - elapsed_time))

    def has_time_left(self):
        """Checks if there is still time left."""
        return self.get_time_left() > 0