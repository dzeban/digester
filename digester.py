import sys
import yaml

import site_handler
import mail

def usage():
    print('{} <config>'.format(sys.argv[0]))

def main(config):
    content = []
    for site in config['sites']:
        content.append(site_handler.get_content(site))

    for user in config['users']:
        mail.send(user, content, config['mail'])

if __name__ == '__main__':
    # argparse
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    # load config
    config_path = sys.argv[1]
    with open(config_path) as f:
        config = yaml.load(f)

    # invoke main
    main(config)
