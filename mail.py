import mandrill
import pybars

GLOBAL_TITLE = 'Your monthly digest'

def send(user, content, settings):
    """
    Send email message to user with given content

    Content is a list of dicts like this:
    [
        {
            'title': 'Reddit /r/programming month top',
            'links': [
                {
                    'title': 'Another programming language! Yay!',
                    'url': 'http://bit.ly/garbledlink'
                },
                {
                    'title': 'Is it too late to start programming at 5?',
                    'url': 'http://quora.com/i-am-idiot'
                }
            ]
        }
    ]

    Content will be wrapped in dict with top level "title" and passed to
    handlebars compiler to produce final HTML email.
    """

    if settings['provider'] != 'mandrill':
        raise NotImplementedError("Only Mandrill mail provider is currently implemented")
    
    config = settings['config']
    try:
        mandrill_client = mandrill.Mandrill(config['apikey'])
        with open('email.html') as f_template:
            template_source = f_template.read()
        compiler = pybars.Compiler()
        template = compiler.compile(template_source)
        
        template_content = {
                'title': GLOBAL_TITLE,
                'sites': content
                }

        html = template(template_content)
        message = { 
                'to': [{
                    'email' : user['email'], 
                    'name': user['name'],
                    'type' : 'to'
                    }], 
                'subject': GLOBAL_TITLE, 
                'from_name': 'Ribbo digester',
                'from_email': 'digester@ribbo.net',
                'html': html,
                }
        message.update(config['options'])
        mandrill_client.messages.send(message=message, async=False)

    except mandrill.Error:
        print('Mandrill error occured: {} - {}'.format(e.__class__, e))
        raise
    except:
        raise
    
