from datetime import datetime, timedelta
import time


data_trips = [
    {'truck_id': 1,
     'first_batch': datetime(2013, 4, 8, 11, 32, 00),
     'second_batch': datetime(2013, 4, 8, 11, 34, 00),
     'arrive_time': datetime(2013, 4, 8, 11, 30, 00),
     'start_time': datetime(2013, 4, 8, 11, 30, 00),
     'finish_time': datetime(2013, 4, 8, 11, 30, 00),
     },
    {'truck_id': 2,
     'first_batch': datetime(2013, 4, 8, 11, 32, 00),
     'second_batch': datetime(2013, 4, 8, 11, 34, 00),
     'arrive_time': datetime(2013, 4, 8, 11, 30, 00),
     'start_time': datetime(2013, 4, 8, 11, 30, 00),
     'finish_time': datetime(2013, 4, 8, 11, 30, 00),
     },
    {'truck_id': 1,
     'first_batch': datetime(2013, 4, 8, 11, 32, 00),
     'second_batch': datetime(2013, 4, 8, 11, 34, 00),
     'arrive_time': datetime(2013, 4, 8, 11, 30, 00),
     'start_time': datetime(2013, 4, 8, 11, 30, 00),
     'finish_time': datetime(2013, 4, 8, 11, 30, 00),
     },
    
]


class Trip():
    def __init__(self, truck_id, first_batch, second_batch, arrive, start, finish):
        self.id = truck_id
        self.first_batch = first_batch
        self.second_batch = second_batch
        self.arrive = arrive
        self.start = start
        self.finish = finish


class Simulation():
    def __init__(self, start_datetime, end_datetime):
        self.start = start_datetime
        self.end = end_datetime
        
    def start_simulation(self):
        time_range = self.end - self.start
        time_range = int(time_range.total_seconds() / 60)
        actual_time = self.start
        for dt in range(0, time_range + 1):
            # increase actual_time by 1 minute
            print(actual_time)
            actual_time += timedelta(minutes=1)
            time.sleep(0.5)
            
            
        


def main():
    simulation = Simulation(datetime(2013, 4, 8, 11, 30, 00), datetime(2013, 4, 9, 4, 0, 0))
    simulation.start_simulation()

if __name__ == '__main__':
    main()