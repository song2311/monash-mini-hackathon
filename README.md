# monash-mini-hackathon
A skill sorting algorithm that sorts a list of candidates according to their highest skill points and most cost efficient skill. 

# Flow diagram
![Screenshot 2020-10-09 at 6 43 22 PM](https://user-images.githubusercontent.com/25546711/95574605-d1070080-0a5f-11eb-8b24-3c849b61bf9a.png)


# Output
For instance, the following request for a position:
```
[
  {
    "Name": "Workflow_Manager",
    "Skills": {
      "Kafka": 3,
      "Flutter": 4,
      "SQL": 1,
      "Hazelcast": 3,
      "TypeScript": 2,
      "Apache Flink": 4,
      "C": 5,
      "BashScripting": 2,
      "Apache Storm": 1,
      "Java": 4
    }
  }
]
```
And the following request for the list of candidates with their skill points will output the following:
```
Rank by skill

Rank 0 : Britta Skills: {'Kafka': 2, 'Flutter': 1, 'Hazelcast': 5, 'TypeScript': 5, 'Apache Flink': 5, 'C': 2, 'BashScripting': 2, 'Apache Storm': 4, 'Java': 5}
Rank 1 : Amelie Skills: {'Kafka': 1, 'Flutter': 2, 'Hazelcast': 4, 'TypeScript': 2, 'Apache Flink': 3, 'C': 3, 'BashScripting': 4, 'Apache Storm': 5}
Rank 2 : Arjun Skills: {'Flutter': 3, 'SQL': 5, 'Hazelcast': 2, 'TypeScript': 1, 'Apache Flink': 2, 'C': 5, 'Java': 5}
Rank 3 : Chang Skills: {'Kafka': 5, 'SQL': 4, 'TypeScript': 4, 'C': 5, 'BashScripting': 1, 'Java': 3}
Rank 4 : Natasha Skills: {'Flutter': 2, 'TypeScript': 4, 'Apache Flink': 5, 'C': 3, 'BashScripting': 2, 'Apache Storm': 2}
Rank 5 : Abed Skills: {'Kafka': 1, 'Flutter': 5, 'Hazelcast': 1, 'TypeScript': 5}
Rank 6 : Annie Skills: {'Kafka': 5, 'SQL': 1, 'Hazelcast': 5}
Rank 7 : Sam Skills: {'Flutter': 3, 'C': 5, 'Java': 2}
Rank 8 : Brandon Skills: {'SQL': 3, 'TypeScript': 5}
Rank 9 : Lee Skills: {'Apache Storm': 3}

Rank by cost

Rank 0 : Britta Skills: {'Kafka': 2, 'Flutter': 1, 'Hazelcast': 5, 'TypeScript': 5, 'Apache Flink': 5, 'C': 2, 'BashScripting': 2, 'Apache Storm': 4, 'Java': 5}
Rank 1 : Amelie Skills: {'Kafka': 1, 'Flutter': 2, 'Hazelcast': 4, 'TypeScript': 2, 'Apache Flink': 3, 'C': 3, 'BashScripting': 4, 'Apache Storm': 5}
Rank 2 : Arjun Skills: {'Flutter': 3, 'SQL': 5, 'Hazelcast': 2, 'TypeScript': 1, 'Apache Flink': 2, 'C': 5, 'Java': 5}
Rank 3 : Natasha Skills: {'Flutter': 2, 'TypeScript': 4, 'Apache Flink': 5, 'C': 3, 'BashScripting': 2, 'Apache Storm': 2}
Rank 4 : Chang Skills: {'Kafka': 5, 'SQL': 4, 'TypeScript': 4, 'C': 5, 'BashScripting': 1, 'Java': 3}
Rank 5 : Sam Skills: {'Flutter': 3, 'C': 5, 'Java': 2}
Rank 6 : Abed Skills: {'Kafka': 1, 'Flutter': 5, 'Hazelcast': 1, 'TypeScript': 5}
Rank 7 : Annie Skills: {'Kafka': 5, 'SQL': 1, 'Hazelcast': 5}
Rank 8 : Brandon Skills: {'SQL': 3, 'TypeScript': 5}
Rank 9 : Lee Skills: {'Apache Storm': 3}
```
