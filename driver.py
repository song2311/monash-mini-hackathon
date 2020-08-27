from find_rank import find_rank

if __name__ == "__main__":
    find_rank_class=find_rank('team.json','tasks.json')
    for task in find_rank_class.tasks():
        print("Tasks:",task)
        qualified=find_rank_class.find_qualified(task['Skills'])
        qualified=find_rank_class.min_cost(task,qualified)
        count=0
        
        for member in qualified:
            print("Rank:",count,member)
            count+=1
            
        print("\n")
