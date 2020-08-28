from find_rank import find_rank

if __name__ == "__main__":
    find_rank_class=find_rank('team.json','tasks.json')
    for task in find_rank_class.tasks():
        print("Tasks:",task)
        filter_skill=find_rank_class.find_qualified(task['Skills'])
        filter_skill=find_rank_class.rank_by_skill(task,filter_skill)
        count=0
        for member in filter_skill:
            print("Rank:",count,member)
            count+=1
            
        print("\n")
