import json
from performance import decorator
import time

class find_rank():
    total_times = []

    def __init__(self, team, tasks):
        total_times = []
        self.__call_count = 0
        self.__team = team
        self.__tasks = tasks
        self.__meet_req=[]
        self.__fail_req=[]
        self.__run_time = 0
    
    def is_empty(self):
        return len(self.__team[0]) == 0 or len(self.__tasks[0]) == 0

    @decorator(total_times) 
    def tasks(self):
        if self.is_empty():
            return []
        self.__call_count += 1
        return self.__tasks

    @decorator(total_times)
    def meet_req(self):
        self.__call_count += 1
        return self.__meet_req

    @decorator(total_times)
    def fail_req(self):
        self.__call_count += 1
        return self.__fail_req
    
    #this method reads a json file and stores it in an variable, it will return a json string
    @decorator(total_times)
    def read_json(self,json_file):
        self.__call_count += 1
        with open(json_file) as f:
            json_string = json.load(f)
        f.close()
        return json_string

    #this function will filter skills unrelated to the tasks, a member without any skill required by a task will have an empty skill dictionary
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    @decorator(total_times)
    def filter_skill(self,task):
        if self.is_empty():
            return
        self.__call_count += 1
        #empty list before filtering skill because it is different for each task
        self.__meet_req=[]
        self.__fail_req=[]
        for member in self.__team:
            qualify=True
            #the Skills dictionary will be empty if the member has 0 skill for the task
            member_dict={'Name':member['Name'],'Skills':{}}
            for skill in task:
                try:
                    #check if a member has the required skill
                    if member['Skills'][skill]:
                        member_dict['Skills'][skill]=member['Skills'][skill]
                    if member['Skills'][skill]<task[skill]:
                        qualify=False
                except KeyError:
                    qualify=False
                    #if skill cannot be found just continue
                    continue
            #only insert those that at least have all the required skills into the met_req list because those members will be higher rank than the others
            if len(member_dict['Skills'])==len(task) and qualify:
                self.__meet_req.append(member_dict)
            else:
                self.__fail_req.append(member_dict)

    #this function takes in an array that contains the members and the filtered skill and sorts the rank of each member by the skill level 
    #Worst time complexity is O(n*m), where n is the number of json elements in team json and m is the number of elements in tasks json
    @decorator(total_times)
    def rank_by_skill(self,task):
        if self.is_empty():
            return
        self.__call_count += 1
        
        for member in self.__filtered_skill:
            #count the total differnce of all skill level and skill level requirements, higher means higher rank
            total_score=0
            for skill in task['Skills']:
                try:
                    skill_req=task['Skills'][skill]
                    skill_level=member['Skills'][skill]
                    #find the balance to see how overqualified a member is in relation to the skill requirements
                    if skill_level>=skill_req:
                        total_score+=(skill_level-skill_req)
                    else:
                        total_score-=(skill_req-skill_level)
                except KeyError:
                    #minus the skill requirements if the member does not have the skills
                    total_score-=skill_req
            member["Total score"]=total_score
        #sort by highest score
        self.__filtered_skill.sort(key=lambda e: e['Total score'],reverse=True)
        self.__call_count += 1
        return

    @decorator(total_times)
    def rank_by_cost(self, task):
        if self.is_empty():
            return
    
        for member in self.__meet_req:
            #count the total differnce of all skill level and skill level requirements, lower means higher rank
            total_score=0
            for skill in task['Skills']:
                skill_req=task['Skills'][skill]
                skill_level=member['Skills'][skill]
                #find the balance to see how overqualified a member is in relation to the skill requirements
                total_score+=(skill_level-skill_req)
                member["Over skill level"]=total_score
        
        for member in self.__fail_req:
            #count the total differnce of all skill level and skill level requirements, lower means higher rank
            total_score=0
            for skill in task['Skills']:
                try:
                    skill_req=task['Skills'][skill]
                    skill_level=member['Skills'][skill]
                    #find the balance to see how overqualified a member is in relation to the skill requirements
                    if skill_level>=skill_req:
                        total_score+=(skill_level-skill_req)
                    #check how much skill the member requires to meet the skill requirements
                    else:
                        total_score+=(skill_req-skill_level)
                except KeyError:
                    #minus the skill requirements if the member does not have the skills
                    total_score+=skill_req
            member["Total score"]=total_score
        try:   
            self.__meet_req.sort(key=lambda e: e["Over skill level"])
            self.__fail_req.sort(key=lambda e: e['Total score'])
        except KeyError:
            pass
        
        self.__call_count += 1
        return self.__meet_req+self.__fail_req

    
    def get_call_count(self):
        return self.__call_count

    def get_total_times(self):
        return find_rank.total_times

    def run(self):
        open("log.txt", "w").close()
        start = time.time()
        self.__tasks = self.read_json(self.__tasks)
        self.__team = self.read_json(self.__team)
        for task in self.tasks():
            filtered_skill=self.filter_skill(task['Skills'])
            print("Tasks:",task)
            print("\nRank by skill")
           
            print("\nRank by cost\n")
            ranked_list=self.rank_by_cost(task)
            count=0
            for member in ranked_list:
                print("Rank",count,":",member)
                count+=1
            
            print("")
        end = time.time()
        self.__run_time = (end-start) * 1000

    def log_performance(self):
        file = open("log.txt", "a+")
        file.write("-------Final Performance Log-------\n")
        file.write("Total function calls made : %d\n" %(self.__call_count))
        file.write("Total elapsed time in milliseconds : %f\n" %(self.__run_time))
        if len(find_rank.total_times) == 0:
            file.write("Mean call elapsed time in milliseconds : 0\n")
            file.write("Maximum call elapsed time in milliseconds : 0\n")
            file.write("Minimum call elapsed time in milliseconds : 0")
        else:
            file.write("Mean call elapsed time in milliseconds : %f\n" %(sum(find_rank.total_times) / len(find_rank.total_times)))
            file.write("Maximum call elapsed time in milliseconds : %f\n" %max(find_rank.total_times))
            file.write("Minimum call elapsed time in milliseconds : %f" %min(find_rank.total_times))
        file.write("\n")
        file.close()






    
                
   
                    
