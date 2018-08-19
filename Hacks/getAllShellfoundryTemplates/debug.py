import getTemplates
import read_user_input


input_handler = read_user_input.input_data()
templateHandler = getTemplates.getallshellfoundrytemplates(input_handler.config_data)
templateHandler.execute()
pass
