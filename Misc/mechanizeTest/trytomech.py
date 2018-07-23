import mechanize
import cookielib

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.add_password('http://10.87.42.117/Account/Login', 'admin', 'admin')
br.open("http://10.87.42.117/")

# br.select_form(nr=0)
# br["Username"] = 'admin'
# br["Password"] = 'admin'
# br.method = "POST"

pass