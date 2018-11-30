from datetime import datetime
import os

def get_time_diff(time_start , time_end):
    format = '%H:%M:%S,%f'
    return datetime.strptime(time_end, format) - datetime.strptime(time_start, format)

class log_item():
    def __init__(self):
        self.time = ''
        self.date = ''
        self.category = ''
        self.message = ''
        self.start_time = ''
        self.end_time = ''
        self.start_end = None


class time_record():
    def __init__(self):
        self.item_name = ''
        self.start_time = ''
        self.time_taken = ''


item_list = []
common_path = r"C:\Users\yoav.e\Documents\skybox_performance\\"
files = os.listdir(common_path)
for f in files:
    if f.__contains__('.log'):
        file_name = f
        path_to_file = common_path + file_name

        all_lines = []
        timing_dict = {}
        clean_timing_dict = {}
        time_records = []
        item_list = []

        with open(path_to_file, 'r') as perf_file:
            all_lines = perf_file.readlines()
        for line in all_lines:
            items = line.split(' ')
            try:
                if items[2] == '[WARNING]:':
                    temp_item = log_item()
                    temp_item.date = items[0]
                    temp_item.time = items[1]
                    temp_item.category = items[6]
                    temp_message = ' '.join(items[7:])
                    if temp_message.__contains__('start'):
                        temp_item.start_end = 'start'
                        temp_item.message = temp_message.replace('start', '').strip()
                        temp_item.start_time =  temp_item.time
                    elif temp_message.__contains__('end'):
                        temp_item.start_end = 'end'
                        temp_item.message = temp_message.replace('end', '').strip()
                        temp_item.end_time = temp_item.time
                    else:
                        temp_item.message = ' '.join(items[7:]).strip()
                    item_list.append(temp_item)
            except:
                pass

        for item in item_list:
            temp_item_dict = timing_dict.get(item.message)
            if temp_item_dict:
                start_value = temp_item_dict.get('start')
                end_value = temp_item_dict.get('end')
                if start_value:
                    temp_item_dict = {item.message: {'start': start_value, 'end': item.end_time}}
                elif end_value:
                    temp_item_dict = {item.message: {'start': item.start_time, 'end': end_value}}
            else:
                temp_item_dict = {item.message: {'start': item.start_time, 'end': item.end_time}}
            timing_dict.update(temp_item_dict)



        for dict_item in timing_dict.iteritems():
            try:
                temp_timings = timing_dict.get(dict_item[0])
                current_time_diff = get_time_diff(temp_timings.get('start'), temp_timings.get('end'))
                # print '{0} : time taken : {1} started: {2}'.format(dict_item[0], current_time_diff, temp_timings.get('start'))
                temp_record = time_record()
                temp_record.item_name = dict_item[0]
                temp_record.start_time = temp_timings.get('start')
                temp_record.time_taken = current_time_diff
                time_records.append(temp_record)
            except:
                pass

        time_records.sort(key=lambda x: x.start_time, reverse=False)
        report = ''
        report += '{0:>45} :  {1}    : {2}'.format('Name of Process', 'Time Taken', 'Time Started\n')
        report +=  '----------------------------------------------------------------------------------------------------------------------------------\n'
        for t in time_records:
            report += '{0:>45} : {1} : {2}\n'.format(t.item_name, t.time_taken, t.start_time)

        global_start = all_lines[0].split(' ')[1]
        global_end = all_lines[-1].split(' ')[1]
        global_time_taken = get_time_diff(global_start, global_end)
        report +=  ('\n  Global start {0:>55}\n  Global End {1:>57}\n  Time Taken for the entire Setup: {2:>35} \n\n\n'.format(
            global_start, global_end, global_time_taken
        ))

        # print report
        perf_report_name = file_name.split('.')[0] + '_performance_log.txt'
        perf_report_filename = common_path + 'performace_logs\\' + perf_report_name
        with open(perf_report_filename, "w") as j:
            j.write(report)




