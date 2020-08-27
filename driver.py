from lowest_cost import lowest_cost

if __name__ == "__main__":
    cost=lowest_cost('team.json','tasks.json')
    qualified=cost.find_qualified()
    for member in qualified:
        print(member)
