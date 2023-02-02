import socket
import pickle
# from product import Product

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(( socket.gethostname(), 4571 ))
	python_dict = {'a': 1, 'b': 2}
	pickled_dict = pickle.dumps(python_dict)
	s.listen(5)
	print('server is up and running \n')
	client, address = s.accept()
	print('connection to ', address, ' establsihed\n')
	print('client object:', client, '\n')
	client.send(pickled_dict)

        
