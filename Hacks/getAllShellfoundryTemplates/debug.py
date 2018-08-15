import getTemplates
import read_user_input

my_token = '59066d6d1cf6158b6d8fdfeb6c6ff79e5e9d894e'
# to generate token https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/

input_handler = read_user_input.input_data()
input_handler.token = my_token
templateHandler = getTemplates.getallshellfoundrytemplates(input_handler.config_data)
templateHandler.execute()
pass
