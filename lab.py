from madt_lib.network import Network


def main():
    net = Network('15.0.0.0/8')
    node_count = 5
    thunders = []
    # create network nodes that will represent client and server
    for i in range(node_count):
        num = str(i+1)
        thunder = net.create_node('thunder'+num, image='thunder')
        thunders.append(thunder)
    # create a local network that will connect all those nodes
    net.create_subnet('net', (thunders))
    # distribute IP addresses
    net.configure(verbose=True)

    net.render('../../labs/my', verbose=True)


if __name__ == "__main__":
    main()
