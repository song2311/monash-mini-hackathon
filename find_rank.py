import json

class find_rank:

    def __init__(self, team, tasks):
        self.__team = self.read_json(team)
        self.__tasks = self.read_json(tasks)
        
    #this method reads a json file and stores it in an variable, it will return a json string
    def read_json(self,json_file):
        with open(json_file) as f:
            json_string = json.load(f)
        f.close()
        return json_string

    #this function will find members in the team that are qualified for the task
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    def find_qualified(self,task):
        team= self.__team
        qualified_members=[]

        for member in team:
            qualify=False
            for skill in task:
                print(skill)
                try:
                    #check if a member has the required skill
                    if member['Skills'][skill]:
                        skill_level=member['Skills'][skill]
                        skill_req=task[skill]
                        #if member meets skill requirements set qualify to true and break loop
                        if skill_level>=skill_req:
                            qualify=True
                        #quit if member does not meet skill requirements
                        else:
                            qualify=False
                            break
                except KeyError:
                    #if skill cannot be found the member is also not qualified for the task
                    qualify=False
                    break
            if qualify:
                member_dict={'Name':member['Name'],'Skills':{}}
                #only insert the required skill in the returned list
                for skill in task:
                    member_dict['Skills'][skill]=member['Skills'][skill]
                qualified_members.append(member_dict)
        return qualified_members

    #this function takes in an array that contains those that are qualified for a task and sorts the rank of each member according to the lowest cost
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    def min_cost(self,task,qualified):
        for member in qualified:
            #count the total differnce of all skill level and skill level requirements, lower means higher rank
            total_score=0
            for skill in task['Skills']:
                skill_level=member['Skills'].get(skill)
                skill_req=task['Skills'].get(skill)
                #find the balance so we can compare and see which member has the lowest skill level
                total_score+=(skill_level-skill_req)
            member["Total score"]=total_score
        #sort based on total difference
        qualified.sort(key=lambda e: e['Total score'])
        return qualified
                
    def tasks(self):
        return self.__tasks
                    
