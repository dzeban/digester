import sys
import yaml

import reddit
import mail

def usage():
    print('{} <config>'.format(sys.argv[0]))

def main(config):
    for site, site_config in config['digest'].items():
        if site == 'reddit':
            submissions = reddit.monthly(site_config)
            for user in config['users']:
                mail.send(title = 'Reddit montly', to = user['email'],
                        submissions = submissions, mandrill_config=config['mandrill'])

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
