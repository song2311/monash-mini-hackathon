from find_rank import find_rank
import time

# driver file that runs the class find_rank
if __name__ == "__main__":
    find_rank_class=find_rank('team.json','tasks.json')
    find_rank_class.run()
    find_rank_class.log_performance()

