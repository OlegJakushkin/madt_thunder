from madt_lib.network import Network


def main():
    net = Network('15.0.0.0/8')
    node_count = 4
    thunders = []
    path = 'my:/home/svetlov/Downloads/madt/tutorials/madt_thunder/build/tendermint:Z'
    # create network nodes that will represent client and server
    thunder1 = net.create_node('node1', 
                        privileged=True,
                        image="tendermint/localnode",
                        ports={'26656/tcp': 26656, '26657/tcp': 26657},
                        environment={'ID':'0','LOG':'${LOG:-tendermint.log}'})
    thunder2 = net.create_node('node2', 
                        privileged=True,
                        image="tendermint/localnode",
                        ports={'26656/tcp': 26659, '26657/tcp': 26660},
                        environment={'LOG':'${LOG:-tendermint.log}', 'ID':'1'})
    thunder3 = net.create_node('node3', 
                        privileged=True,
                        image="tendermint/localnode",
                        environment={'LOG':'${LOG:-tendermint.log}', 'ID':'2'},
                        ports={'26656/tcp': 26661, '26657/tcp': 26662},
                        )
    thunder4 = net.create_node('node4', 
                        privileged=True,
                        image="tendermint/localnode",
                        environment={'LOG':'${LOG:-tendermint.log}', 'ID':'3'},
                        ports={'26656/tcp': 26663, '26657/tcp': 26664},
                        )
    thunder5 = net.create_node('node5', 
                        privileged=True,
                        image="tendermint/localnode",
                        environment={'LOG':'${LOG:-tendermint.log}', 'ID':'4'},
                        ports={'26656/tcp': 26665, '26657/tcp': 26666},
                        entrypoint="sleep infinity",
                        #volumes=path
                        )
    
    # create a local network that will connect all those nodes
    net.create_subnet('net', (thunder1,thunder2,thunder3,thunder4))
    # distribute IP addresses
    net.configure(verbose=True)

    net.render('../../labs/my', verbose=True)


if __name__ == "__main__":
    main()
