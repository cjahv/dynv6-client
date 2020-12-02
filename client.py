import urllib.parse

import certifi  # noqa
import click
import netifaces
import requests
import time

@click.command()
@click.argument('hostname')
@click.option('--token', prompt=True, hide_input=True)
@click.option('--api', prompt=True, hide_input=True)
@click.option('--interface', default='eth0')
@click.option('--dely', default=10)
@click.option('--ipv4/--no-ipv4', default=True)
@click.option('--ipv6/--no-ipv6', default=True)
def main(hostname, token, api, interface, dely, ipv4, ipv6):

    print('!!dynv6-clinet!!')

    oldAddressIpv4 = ''
    oldAddressIpv6 = ''

    print('hostname: %s' % hostname)
    print('token: %s' % token)
    print('api: %s' % api)
    print('interface: %s' % interface)
    print('dely: %s' % dely)
    print('ipv4: %s' % ipv4)
    print('ipv6: %s' % ipv6)

    while 1:
        update = False
        parameters = {'hostname': hostname, 'token': token}

        if ipv4:
            ipv4addr = requests.get(api).json()['ip']
            if ipv4addr is not None:
                parameters['ipv4'] = ipv4addr
                if ipv4addr != oldAddressIpv4:
                    update = True

        if ipv6:
            addresses = netifaces.ifaddresses(interface)
            ipv6addr = addresses[netifaces.AF_INET6][0]['addr']
            if ipv6addr is not None:
                parameters['ipv6'] = ipv6addr
                if ipv6addr != oldAddressIpv6:
                    update = True

        if update:
            if ipv4:
                print('update ipv4: %s' % parameters['ipv4'])
            if ipv6:
                print('update ipv6: %s' % parameters['ipv6'])
            response = requests.get('https://dynv6.com/api/update?{}'.format(
                urllib.parse.urlencode(parameters)))
            if response.status_code == 200 and response.content:
                if ipv4:
                    oldAddressIpv4 = parameters['ipv4']
                if ipv6:
                    oldAddressIpv6 = parameters['ipv6']
                print('update success!')
                time.sleep(60 - dely)
            else:
                print('update fail!!!')
        time.sleep(dely)


if __name__ == '__main__':
    main()
