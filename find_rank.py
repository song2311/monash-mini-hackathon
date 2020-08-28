import json

class find_rank:

    def __init__(self, team, tasks):
        self.__team = self.read_json(team)
        self.__tasks = self.read_json(tasks)

    def tasks(self):
        return self.__tasks
    
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
        #list of dictionaries that only contains team members with the skill required by the task
        filtered_skill=[]

        for member in team:
            member_dict={'Name':member['Name'],'Skills':{}}
            for skill in task:
                try:
                    #check if a member has the required skill
                    if member['Skills'][skill]:
                        member_dict['Skills'][skill]=member['Skills'][skill]
                except KeyError:
                    #if skill cannot be found just continue
                    continue
            filtered_skill.append(member_dict)
        return filtered_skill

    #this function takes in an array that contains those that are qualified for a task and sorts the rank of each member according to the rank of skill
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    def rank_by_skill(self,task,filtered_skill):
        for member in filtered_skill:
            #count the total differnce of all skill level and skill level requirements, lower means higher rank
            total_score=0
            for skill in task['Skills']:
                try:
                    skill_req=task['Skills'][skill]
                    skill_level=member['Skills'][skill]
                    #find the balance so we can compare and see which member has the lowest skill level
                    total_score+=(skill_level-skill_req)
                except KeyError:
                    #minus if skill is not found in member
                    total_score-=skill_req
            member["Total score"]=total_score
        #sort based on total difference
        filtered_skill.sort(key=lambda e: e['Total score'],reverse=True)
        return filtered_skill
                
   
                    
