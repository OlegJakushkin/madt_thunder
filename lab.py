from madt_lib.network import Network


def main():
    net = Network('15.0.0.0/8')
    node_count = 6
    thunders = []
    # path = 'my:/home/svetlov/Downloads/madt/tutorials/madt_thunder/build/tendermint:Z'
    # create network nodes that will represent client and server
    for x in range(1,6):
	    thunders.append(net.create_node('node'+str(x), 
                        privileged=True,
                        image="tendermint/validator",
                        ports={'26656/tcp': 26659+2*(x-1), '26657/tcp': 26660+2*(x-1)},
                        environment={'ID':str(x-1),'LOG':'${LOG:-tendermint.log}'},
                        ))
    # create sleep node to simulated adding new nodes
    for x in range(6,7):
        thunders.append(net.create_node('node'+str(x), 
                        privileged=True,
                        image="tendermint/validator",
                        ports={'26656/tcp': 26659+2*(x-1), '26657/tcp': 26660+2*(x-1)},
                        environment={'ID':str(x-1),'LOG':'${LOG:-tendermint.log}'},
                        # entrypoint="sleep "+str(int(x>4)*x*10)
                        entrypoint="sleep 100000",
                        ))
    x=7
    thunders.append(net.create_node('node'+str(x), 
                        privileged=True,
                        image="tendermint/nonvalidator",
                        ports={'26656/tcp': 26659+2*(7-1), '26657/tcp': 26660+2*(x-1)},
                        environment={'ID':str(x-1),'LOG':'${LOG:-tendermint.log}'},
                        # entrypoint="sleep "+str(int(x>4)*x*10)
                        #entrypoint="sleep 100000",
                        ))
    # thunder1 = net.create_node('node1', 
    #                     privileged=True,
    #                     image="tendermint/validator",
    #                     ports={'26656/tcp': 26656, '26657/tcp': 26657},
    #                     environment={'ID':'0','LOG':'${LOG:-tendermint.log}'})
    # thunder2 = net.create_node('node2', 
    #                     privileged=True,
    #                     image="tendermint/validator",
    #                     ports={'26656/tcp': 26659, '26657/tcp': 26660},
    #                     environment={'LOG':'${LOG:-tendermint.log}', 'ID':'1'})
    # thunder3 = net.create_node('node3', 
    #                     privileged=True,
    #                     image="tendermint/validator",
    #                     environment={'LOG':'${LOG:-tendermint.log}', 'ID':'2'},
    #                     ports={'26656/tcp': 26661, '26657/tcp': 26662},
    #                     )
    # thunder4 = net.create_node('node4', 
    #                     privileged=True,
    #                     image="tendermint/validator",
    #                     environment={'LOG':'${LOG:-tendermint.log}', 'ID':'3'},
    #                     ports={'26656/tcp': 26663, '26657/tcp': 26664},
    #                     )
   

    # thunder5 = net.create_node('node5', 
    #                     privileged=True,
    #                     image="tendermint/nonvalidator",
    #                     environment={'LOG':'${LOG:-tendermint.log}', 'ID':'4'},
    #                     ports={'26656/tcp': 26665, '26657/tcp': 26666},
    #                     entrypoint="sleep 10000000",
    #                     #volumes=path
    #                     )
    
    # create a local network that will connect all those nodes
    net.create_subnet('net', thunders)
    # net.create_subnet('net', (thunder1,thunder2,thunder3,thunder4))
    # distribute IP addresses
    net.configure(verbose=True)

    net.render('../../labs/my', verbose=True)


if __name__ == "__main__":
    main()
