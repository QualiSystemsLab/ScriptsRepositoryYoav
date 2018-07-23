import xml.etree.ElementTree as ET
import os

class question():
    def __init__(self):
        self.question = ''
        self.options = []
        self.correct_answer = ''



path = 'C:\Users\yoav.e\Desktop\CTC Training materials\CloudShell'


def find_all_xml_files(path):
    all_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith('.xml') and not file.__contains__("lms") and file.__contains__("Quiz")):
                fullname = os.path.join(root, file)
                all_files.append(fullname)
    return all_files

def parse_quiz(filetext):
    all_questions = []
    # ETO = ET()
    tree = ET.fromstring(filetext)
    all_items = tree.findall(".//item")
    for item in all_items:
        pres = item.find(".//presentation")
        outcome = item.find(".//resprocessing")
        my_question = question()
        try:
            my_question.correct_answer = cheat_sheet(outcome)
        except:
            my_question.correct_answer = ''
        all_text =  pres.findall(".//mattext")
        for i, text in enumerate(all_text):
            my_text = text.text
            if i == 0:
                my_question.question = my_text
            else:
                my_question.options.append(my_text)
        all_questions.append(my_question)
    return all_questions

def cheat_sheet(rest_pro_item):
    correct_answer = ''
    all_options = rest_pro_item.findall(".//varequal")
    for option in all_options:
        if option.attrib.get('respident').__contains__('va') or option.attrib.get('respident').__contains__('vf'):
            correct_answer = option.text
    return correct_answer

def from_file_to_cut_text(filename):
    file_raw_data = open(filename)
    filedata = file_raw_data.read().split("<assessment")[1].split("</assessment>")[0]
    filetext = '<assessment{0}</assessment>'.format(filedata)
    return filetext

def save_questions_to_text(quest_instance):
    '''
    :param quest_instance:
    :type question:
    :return:
    '''
    string = ''
    string += '<the Question is> {0}\n'.format(quest_instance.question.encode("utf-8"))
    for opt in quest_instance.options:
        string += '<a Possible answer is> {0}\n'.format(opt.encode("utf-8"))
    string += '<the correct answer is> {0}\n'.format(quest_instance.correct_answer.encode("utf-8"))
    return string

def save_text_fo_file(text, filename):
    file_obj = open(filename, "w")
    file_obj.write(text)
    file_obj.close()


all_files = find_all_xml_files(path)
for file in all_files:
    question_list = parse_quiz(from_file_to_cut_text(file))
    for i, question_item in enumerate(question_list):
        question_text = save_questions_to_text(question_item)
        question_file_name = '{0}_question_{1}.txt'.format(file.split(".xml")[0], str(i))
        save_text_fo_file(question_text, question_file_name)
pass