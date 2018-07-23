from login_sbox_api_activityFeed import AF_handler
import datetime
import html_table_builder
import numpy

class bp_data():
    def __init__(self, bp_id, bp_name):
        self.bp_id = bp_id
        self.bp_name = bp_name['name']
        self.times = []
        self.avg_setup_time = datetime.timedelta()
        self.tot_setup_time = datetime.timedelta()
        self.all_setup_times = []
        self.all_teardown_times = []
        self.setup_SD = 0
        self.teardown_SD = 0
        self.avg_teardown_time = datetime.timedelta()
        self.count_iters = 0

class time_calculator():
    def __init__(self):
        pass

    def calculate(self):
        myc = AF_handler()
        all_sboxes = myc.get_all_sandboxes_from_blueprint()
        sbox_ids_for_bp = []
        all_bps = []
        all_bps_objs = []
        for sbox in all_sboxes:
            if sbox['blueprint']:
                all_bps.append(sbox['blueprint']['id'])
        all_bps = list(set(all_bps))
        for bp in all_bps:
            bp_name = myc.get_blueprint_name_from_id(bp)
            if bp_name:
                all_bps_objs.append(bp_data(bp, bp_name))
        for sbox in all_sboxes:
            if sbox['blueprint'] and sbox['state'] == 'Ended':
                for x in all_bps_objs:
                    if x.bp_id == sbox['blueprint']['id']:
                            v = myc.get_af_times(sbox['id'])
                            x.times.append(v)
        for obj in all_bps_objs:
            setup_time = datetime.timedelta()
            teardown_time = datetime.timedelta()
            obj.count_iters = obj.times.__len__()
            for timer in obj.times:
                setup_time_list = [x['Time_Taken'] for x in timer if x['Name'] == 'Setup']
                if setup_time_list:
                    obj.all_setup_times.append(setup_time_list[0].total_seconds())
                    setup_time += setup_time_list[0]
                teardown_time_list = [x['Time_Taken'] for x in timer if x['Name'] == 'Teardown']
                if teardown_time_list:
                    obj.all_teardown_times.append(teardown_time_list[0].total_seconds())
                    teardown_time += teardown_time_list[0]
            if obj.count_iters != 0:
                obj.avg_setup_time = str(setup_time / obj.count_iters).split('.')[0]
                obj.setup_SD = round(numpy.std(obj.all_setup_times), 0)
                obj.avg_teardown_time = str(teardown_time / obj.count_iters).split('.')[0]
                obj.setup_SD = round(numpy.std(obj.all_teardown_times), 0)
        return self.prepare_for_html(all_bps_objs)

    def prepare_for_html(self, all_bps_objs):
        headlines = [
            'Blueprint Name',
            'Blueprint ID',
            'times run',
            'Average Setup Time',
            'Setup SD',
            'Average Teardown Time',
            'Teardown SD'
        ]
        html_table_data = []
        for obj in all_bps_objs:
            html_table_data.append(
                [
                    obj.bp_name,
                    obj.bp_id,
                    obj.count_iters,
                    obj.avg_setup_time,
                    obj.setup_SD,
                    obj.avg_teardown_time,
                    obj.teardown_SD
                ])
        my_html = html_table_builder.createHTMLtablehtml_Table(headlines, html_table_data, title='Average Setup and teardown times')
        return my_html