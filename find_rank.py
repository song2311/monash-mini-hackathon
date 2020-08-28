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

    #this function will filter skills unrelated to the tasks, a member without any skill required by a task why have an empty skill dictionary
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    def filter_skill(self,task):
        team= self.__team
        #list of dictionaries that only contains team members and their skill related to the task
        filtered_skill=[]

        for member in team:
            #the Skills dictionary will be empty if the member has 0 skill for the task
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

    #this function takes in an array that contains the members and the filtered skill and sorts the rank of each member according to the rank of skill
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    def rank_by_skill(self,task,filtered_skill):
        for member in filtered_skill:
            #count the total differnce of all skill level and skill level requirements, higher means higher rank
            total_score=0
            for skill in task['Skills']:
                try:
                    skill_req=task['Skills'][skill]
                    skill_level=member['Skills'][skill]
                    #find the balance to see how overqualified a member is in relation to the skill requirements
                    total_score+=(skill_level-skill_req)
                except KeyError:
                    #minus the skill requirements if the member does not have the skills
                    total_score-=skill_req
            member["Total score"]=total_score
        #sort by highest score
        filtered_skill.sort(key=lambda e: e['Total score'],reverse=True)
        return filtered_skill


    
                
   
                    
