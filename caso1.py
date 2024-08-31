#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')

    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')

    r_main = net.addHost('r_main', cls=Node, ip='192.168.100.6/29')
    r_main.cmd('sysctl -w net.ipv4.ip_forward=1')
    r1 = net.addHost('r1', cls=Node, ip='192.168.100.1/29')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
    r2 = net.addHost('r2', cls=Node, ip='192.168.100.9/29')
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')
    r3 = net.addHost('r3', cls=Node, ip='192.168.100.17/29')
    r3.cmd('sysctl -w net.ipv4.ip_forward=1')
    r4 = net.addHost('r4', cls=Node, ip='192.168.100.25/29')
    r4.cmd('sysctl -w net.ipv4.ip_forward=1')
    r5 = net.addHost('r5', cls=Node, ip='192.168.100.33/29')
    r5.cmd('sysctl -w net.ipv4.ip_forward=1')
    r6 = net.addHost('r6', cls=Node, ip='192.168.100.41/29')
    r6.cmd('sysctl -w net.ipv4.ip_forward=1')

    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch, failMode='standalone')
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch, failMode='standalone')
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.254/24', defaultRoute='via 10.0.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.254/24', defaultRoute='via 10.0.2.1')
    h3 = net.addHost('h3', cls=Host, ip='10.0.3.254/24', defaultRoute='via 10.0.3.1')
    h4 = net.addHost('h4', cls=Host, ip='10.0.4.254/24', defaultRoute='via 10.0.4.1')
    h5 = net.addHost('h5', cls=Host, ip='10.0.5.254/24', defaultRoute='via 10.0.5.1')
    h6 = net.addHost('h6', cls=Host, ip='10.0.6.254/24', defaultRoute='via 10.0.6.1')

    info( '*** Add links\n')
    net.addLink(s1, r_main, intfName1='s1-eth1', intfName2='rmain-eth1', params2={'ip': '192.168.100.6/29'})
    net.addLink(s2, r_main, intfName1='s2-eth1', intfName2='rmain-eth2', params2={'ip': '192.168.100.14/29'})
    net.addLink(s3, r_main, intfName1='s3-eth1', intfName2='rmain-eth3', params2={'ip': '192.168.100.22/29'})
    net.addLink(s4, r_main, intfName1='s4-eth1', intfName2='rmain-eth4', params2={'ip': '192.168.100.30/29'})
    net.addLink(s5, r_main, intfName1='s5-eth1', intfName2='rmain-eth5', params2={'ip': '192.168.100.38/29'})
    net.addLink(s6, r_main, intfName1='s6-eth1', intfName2='rmain-eth6', params2={'ip': '192.168.100.46/29'})

    net.addLink(s1, r1, intfName1='s1-eth2', intfName2='r1-eth1', params2={'ip': '192.168.100.1/29'})
    net.addLink(s2, r2, intfName1='s2-eth2', intfName2='r2-eth1', params2={'ip': '192.168.100.9/29'})
    net.addLink(s3, r3, intfName1='s3-eth2', intfName2='r3-eth1', params2={'ip': '192.168.100.17/29'})
    net.addLink(s4, r4, intfName1='s4-eth2', intfName2='r4-eth1', params2={'ip': '192.168.100.25/29'})
    net.addLink(s5, r5, intfName1='s5-eth2', intfName2='r5-eth1', params2={'ip': '192.168.100.33/29'})
    net.addLink(s6, r6, intfName1='s6-eth2', intfName2='r6-eth1', params2={'ip': '192.168.100.41/29'})

    net.addLink(s7, r1, intfName1='s7-eth1', intfName2='r1-eth2', params2={'ip': '10.0.1.1/24'})
    net.addLink(s8, r2, intfName1='s8-eth1', intfName2='r2-eth2', params2={'ip': '10.0.2.1/24'})
    net.addLink(s9, r3, intfName1='s9-eth1', intfName2='r3-eth2', params2={'ip': '10.0.3.1/24'})
    net.addLink(s10, r4, intfName1='s10-eth1', intfName2='r4-eth2', params2={'ip': '10.0.4.1/24'})
    net.addLink(s11, r5, intfName1='s11-eth1', intfName2='r5-eth2', params2={'ip': '10.0.5.1/24'})
    net.addLink(s12, r6, intfName1='s12-eth1', intfName2='r6-eth2', params2={'ip': '10.0.6.1/24'})

    net.addLink(s7, h1)
    net.addLink(s8, h2)
    net.addLink(s9, h3)
    net.addLink(s10, h4)
    net.addLink(s11, h5)
    net.addLink(s12, h6)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    switch_names = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12']
    for switch_name in switch_names:
        net.get(switch_name).start([])

    info( '*** Post configure switches and hosts\n')
    net.start()

    r_main_cmd = 'ip route add 10.0.1.0/24 via 192.168.100.1 && \
                  ip route add 10.0.2.0/24 via 192.168.100.9 && \
                  ip route add 10.0.3.0/24 via 192.168.100.17 && \
                  ip route add 10.0.4.0/24 via 192.168.100.25 && \
                  ip route add 10.0.5.0/24 via 192.168.100.33 && \
                  ip route add 10.0.6.0/24 via 192.168.100.41'
    r_main.cmd(r_main_cmd)

    r1_cmd = 'ip route add 10.0.0.0/21 via 192.168.100.6 && \
              ip route add 192.168.100.0/26 via 192.168.100.6'
    r1.cmd(r1_cmd)

    r2_cmd = 'ip route add 10.0.0.0/21 via 192.168.100.14 && \
              ip route add 192.168.100.0/26 via 192.168.100.14'
    r2.cmd(r2_cmd)

    r3_cmd = 'ip route add 10.0.0.0/21 via 192.168.100.22 && \
              ip route add 192.168.100.0/26 via 192.168.100.22'
    r3.cmd(r3_cmd)

    r4_cmd = 'ip route add 10.0.0.0/21 via 192.168.100.30 && \
              ip route add 192.168.100.0/26 via 192.168.100.30'
    r4.cmd(r4_cmd)

    r5_cmd = 'ip route add 10.0.0.0/21 via 192.168.100.38 && \
              ip route add 192.168.100.0/26 via 192.168.100.38'
    r5.cmd(r5_cmd)

    r6_cmd = 'ip route add 10.0.0.0/21 via 192.168.100.46 && \
              ip route add 192.168.100.0/26 via 192.168.100.46'
    r6.cmd(r6_cmd)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
