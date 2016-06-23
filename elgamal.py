def keygen(g, q, x_index):
    private_key = range(1, q)[x_index]
    h = g ** range(1, q)[x_index]

