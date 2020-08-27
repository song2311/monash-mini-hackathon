from lowest_cost import lowest_cost

if __name__ == "__main__":
    cost=lowest_cost('team.json','tasks.json')
    for task in cost.tasks():
        print("Tasks:",task)
        qualified=cost.find_qualified(task['Skills'])
        for member in qualified:
            print(member)
        print("\n")
