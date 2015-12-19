import mandrill
import pybars

def send(title=None, to=None, submissions=None, mandrill_config=None):
    try:
        mandrill_client = mandrill.Mandrill(mandrill_config['apikey'])
        with open('email.template') as f_template:
            template_source = f_template.read()
        compiler = pybars.Compiler()
        template = compiler.compile(template_source)
        template_content = {
                'title': title,
                'sources': submissions
                }

        mail = template(template_content)
        import pdb;pdb.set_trace()
        message = { 
                'to': [{'email' : to, 'type' : 'to'}], 
                'subject': title, 
                'from_name': 'Ribbo digester',
                'from_email': 'digester@ribbo.net',
                'html': mail,
                }
        message.update(mandrill_config['options'])
        mandrill_client.messages.send(message=message, async=False)

    except mandrill.Error:
        print('Mandrill error occured: {} - {}'.format(e.__class__, e))
        raise
    except:
        raise
    
