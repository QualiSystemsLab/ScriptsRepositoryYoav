import os
import re
from elasticsearch import Elasticsearch
import jsonpickle
import requests

INDEX_NAME = 'perf_test'
INDEX_MAPPING = '''
{
    "mappings": {
        "run": {
            "_all":       { "enabled": true  },
            "properties": {
                "topology":  {
                    "type":   "string",
                    "index":  "not_analyzed"
                },
                "type":  {
                    "type":   "string",
                    "index":  "not_analyzed"
                },
                "cumulative_time":  {
                    "type":   "float"
                },
                "cumulative_time_factor":  {
                    "type":   "float"
                },
                "time_per_call":  {
                    "type":   "float"
                },
                "time_per_call_factor":  {
                    "type":   "float"
                }

            }
        }
    }
}
'''

class perfomance_data_point():
    def __init__(self, item, cumulative_time, time_per_call, number_of_calls, type, topology):
        self.item = item
        self.cumulative_time = cumulative_time
        self.time_per_call = time_per_call
        self.number_of_calls = number_of_calls
        self.type = type
        self.topology = topology

    def __init__(self, line, type, topology):
        elements = line.split()
        self.item = re.findall('\((\w+)\)', elements[5])[0]
        self.cumulative_time = elements[4]
        self.time_per_call = elements[3]
        self.number_of_calls = elements[0]
        self.type = type
        self.topology = topology
        self.agg_name = self.type + "_" + self.item + "_" + self.topology

def add_datapoints(type, log_name, filepath, res_id):
    file_to_open = filepath + "\\" + type + "_" + log_name + "_" + res_id
    with open(file_to_open, 'r') as myfile:
        data = myfile.read().split("\n")
    relevant_lines = filter(lambda line: line.__contains__(type.lower() + "_script") and not line.__contains__("lambda"), data)
    data_points = map(lambda line: perfomance_data_point(line, type, log_name), relevant_lines)
    return data_points

datapoints = []
filepath = r'\\qsnas1\shared\vcentershell_profiling'
files = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]
for one_file in files:
    ff = one_file.split("_")
    if ff[0].lower() == 'setup':
        datapoints.extend(add_datapoints(ff[0], ff[1], filepath, ff[2]))
    if ff[0].lower() == 'teardown':
        datapoints.extend(add_datapoints(ff[0], ff[1], filepath, ff[2]))
es = Elasticsearch("http://localhost:7890")
i = 0
es.indices.delete(index=INDEX_NAME)
requests.put('http://localhost:7890/'+INDEX_NAME, data=INDEX_MAPPING)
for datapoint in datapoints:
    raw_data = jsonpickle.encode(datapoint, unpicklable=False)
    raw_data = jsonpickle.decode(raw_data)
    raw_data['cumulative_time'] = float(raw_data['cumulative_time'])
    raw_data['cumulative_time_factor'] = float(raw_data['cumulative_time']) * 1000
    raw_data['number_of_calls'] = int(raw_data['number_of_calls'])
    raw_data['time_per_call'] = float(raw_data['time_per_call'])
    raw_data['time_per_call_factor'] = float(raw_data['time_per_call']) * 1000
    res = es.index(index=INDEX_NAME, doc_type='run', body=raw_data)
    i += 1
