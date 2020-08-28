from find_rank import find_rank

if __name__ == "__main__":
    find_rank_class=find_rank('team.json','tasks.json')
    
    for task in find_rank_class.tasks():
        filtered_skill=find_rank_class.filter_skill(task['Skills'])
        print("Tasks:",task)
        print("\nRank by skill")
        find_rank_class.rank_by_skill(task)
        filtered_skill=find_rank_class.filtered_skill()
        count=0
        for member in filtered_skill:
            print("Rank",count,":",member)
            count+=1
        
        print("\nRank by cost\n")
