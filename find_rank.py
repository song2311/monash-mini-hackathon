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
    #Worst time complexity is O(n*m*p*q) where n is number of json objects in tasks.json, m is number of json objects in team.json, p is number of key value pairs in the dictionary skill of a task and q
    #is number of key value pairs in the dictionary skill of team member
    def find_qualified(self,task):
        team= self.__team
        qualified=[]
        for member in team:
            for skill in task:
                qualify=False
                #check in every skill of a team member to see whether they match a skill requirement
                for mem_skill in member['Skills']:
                    if mem_skill==skill:
                        skill_level=member['Skills'][skill]
                        skill_req=task[skill]
                        #if member meets skill requirements set qualify to true and break loop
                        if skill_level>=skill_req:
                            qualify=True
                            break
                #exit loop early if member did not meet one of the skill requirements
                if qualify==False:
                    break
            #only add member to qualified list if member meets all requirements
            if qualify==True:
                member_dict={'Name':member['Name'],
                             'Skills':{}}
                for skill in task:
                    member_dict['Skills'][skill]=member['Skills'][skill]
                qualified.append(member_dict)
        return qualified

    #this function takes in an array that contains those that are qualified for a task and sorts the rank of each member according to the lowest cost
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
                    
