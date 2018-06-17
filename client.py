import urllib.parse

import certifi  # noqa
import click
import netifaces
import requests
import time

@click.command()
@click.argument('hostname')
@click.option('--token', prompt=True, hide_input=True)
@click.option('--interface', default='eth0')
@click.option('--ipv4/--no-ipv4', default=True)
@click.option('--ipv6/--no-ipv6', default=True)
def main(hostname, token, interface, ipv4, ipv6):
    while 1:
        addresses = netifaces.ifaddresses(interface)
        parameters = {'hostname': hostname, 'token': token }

        if ipv4:
            ipv4addr = requests.get('https://api.ipify.org?format=json').json()['ip']
            parameters['ipv4'] = ipv4addr

        if ipv6:
            ipv6addr = addresses[netifaces.AF_INET6][0]['addr']
            parameters['ipv6'] = ipv6addr

        response = requests.get('https://dynv6.com/api/update?{}'.format(
            urllib.parse.urlencode(parameters)))
        assert response.status_code == 200, response.content
        time.sleep(5 * 60)

if __name__ == '__main__':
    main()
