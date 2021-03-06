import pickle

__author__ = 'pegah'

"""this class is for calling each person_id from scholarship.json dDB, call its related snippets from USM and finally extract
 the entities and their confidence values."""

import os

from CODE.entity_extraction import extract_entities_confidence_score
from collections import deque
import json

class queries:
    def __init__(self, person_id, query_id):

        self.person_id = person_id
        self.query_id = query_id

        with open('../DATA/scholarships.json') as data_file:
            data = json.load(data_file)

        self.person_info = data["_default"][self.person_id]

    def generate_query(self):

        name = '_'.join(self.person_info['name'].split(' '))
        query_results = '../USM/train_db/' + self.person_id + '/test_for_' + self.person_id +'_with_query_' + name + '_' + \
                        self.query_id +'.json'

        with open(query_results) as data_file:
            data_query = json.load(data_file)

        queue = {}

        for i in range(len(data_query)): #range(50)
            text = data_query[str(i)]['text']
            entities = extract_entities_confidence_score(text)
            queue[str(i)] = entities

        return queue

    def write_query_to_json(self, queue):

            output = {}

            original_entities = {'RN': self.person_info['name'], 'U':self.person_info['institution'],'Y': self.person_info['year_start']}

            output['original_entities'] = original_entities
            output['queue'] = queue
            json_data = output

            newpath = r'../DATA/entities_db/'+ str(self.person_id)

            if not os.path.exists(newpath):
                os.makedirs(newpath)

            with open(newpath + '/queue_'+ str(self.query_id) +'.json', 'w') as outfile:
                json.dump(json_data, outfile)

    def generate_write_query_to_file(self):
        queue = self.generate_query()
        self.write_query_to_json(queue)




 #test for opening the pickle list
with open('../DATA/person_id/train_list.pkl', 'rb') as f:
    persons_trains = pickle.load(f)

#Example
def genrate_all_queries(person_id):

    queiries_list = ["", "PHD", "doctorate", "institute", "master", "undergraduate", "university"]
    #person_id = "1390"

    for que in queiries_list:
        q = queries(str(person_id), que)
        q.generate_write_query_to_file()


def generate_queiries_for_train(_trains):
    for i in _trains:
        genrate_all_queries(i)

#genrate_all_queries(1390)

#generate all queries for all traning set
#generate_queiries_for_train(persons_trains)


person_id = "1390"
que = "institute"
q = queries(person_id, que)
q.generate_write_query_to_file()
