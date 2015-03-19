#!/usr/bin/env python2

from FeedSynchronizer import FeedSynchronizer
from cgi import parse_qs, escape
import ConfigParser

sync = FeedSynchronizer()

html = """
<html>
<header>
	<title>RSS Synchronizer</title>
	<style>
	.text_input { width: 100%% }
	.row2 { width: 75%% }
	.row1 { width: 150px }
	div { margin-left:auto; margin-right:auto; width:600px; text-align:center }
	legend { text-align:left }
	</style>
</header>

<div>
<h1>Configuration</h1>
<form method="post" action="web.py">
%s
	<br />
	<input type="submit" value="Submit" />
</form>
</div>
</html>
"""

def app(environ, start_response):
	
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
		
	request_body = environ['wsgi.input'].read(request_body_size)
	d = parse_qs(request_body)
	
	if request_body_size > 0:
		saveConfig(d)
	
	form_content = ''
	conf = ConfigParser.RawConfigParser()
	conf.read('config.cfg')
	for section in conf.sections():
		form_content += '\t<fieldset>\n\t\t<legend> %s </legend>\n\t\t<table>\n' % (section)
		for item in conf.items(section):
			input_form = ''
			
			if item[1] == 'True' or item[1] == 'False':
				if item[1] == 'True':
					chk_true = 'checked'
					chk_fals = ''
				else:
					chk_true = ''
					chk_fals = 'checked'
					
				input_form = '<input type="radio" name="%s;%s" value="True" %s/>True' % (section, item[0], chk_true)
				input_form += '<input type="radio" name="%s;%s" value="False" %s/>False' % (section, item[0], chk_fals)
			else:
				input_form = '<input type="text" class="text_input" name="%s;%s" value="%s"/>' % (section, item[0], item[1])
				
			form_content += ('\t\t\t<tr>'
							 '\n\t\t\t\t<td class="row1">%s : </td>\n\t\t\t\t'
							 '<td class="row2">' + input_form + '</td>'
							 '\n\t\t\t</tr>\n') % (item[0])
		form_content += '\t\t</table>\n\t</fieldset>\n\n'
		
	response_body = html % (form_content)
	
	response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
	start_response('200 OK', response_headers)
	
	return [response_body]
	
def saveConfig(d):
	conf = ConfigParser.RawConfigParser()
	conf.read('config.cfg')
	for entry in d:
		conf.set(entry.split(';')[0], entry.split(';')[1], d[entry][0])

	with open('config.cfg', 'wb') as configfile:
				conf.write(configfile)

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(app).run()
