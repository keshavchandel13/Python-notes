# Data to be written
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_tuple = (10, 20, 30)

# Writing to .dat file
with open('data.dat', 'w') as dat_file:
    dat_file.write(str(my_list) + '\n')
    dat_file.write(str(my_dict) + '\n')
    dat_file.write(str(my_tuple) + '\n')

# Writing to .txt file
with open('data.txt', 'w') as txt_file:
    txt_file.write(str(my_list) + '\n')
    txt_file.write(str(my_dict) + '\n')
    txt_file.write(str(my_tuple) + '\n')

# Reading from .dat file
with open('data.dat', 'r') as dat_file:
    print("Contents of data.dat:")
    print(dat_file.read())

# Reading from .txt file
with open('data.txt', 'r') as txt_file:
    print("Contents of data.txt:")
    print(txt_file.read())


'''
import pickle

# Data to be written
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_tuple = (10, 20, 30)

# Writing to .dat file using pickle
with open('data_pickle.dat', 'wb') as pickle_file:
    pickle.dump(my_list, pickle_file)
    pickle.dump(my_dict, pickle_file)
    pickle.dump(my_tuple, pickle_file)

# Reading from .dat file using pickle
with open('data_pickle.dat', 'rb') as pickle_file:
    loaded_list = pickle.load(pickle_file)
    loaded_dict = pickle.load(pickle_file)
    loaded_tuple = pickle.load(pickle_file)

print("Contents of data_pickle.dat using pickle:")
print("List:", loaded_list)
print("Dictionary:", loaded_dict)
print("Tuple:", loaded_tuple)
'''
