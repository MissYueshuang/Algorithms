Write a function get_indices (Including type annotations) which takes a list of tuples and returns a 2D list of indices. Each sub-list corresponds to the indices of all rows pointing to the same person. Rows point to the same person if any of their column entries are the same. 

Note: Your function should work for any number of columns/ people and be tested for other unseen edge cases.

>>> data = [(‘id1’, addr1, ‘pw1’), (‘idx’, ‘addr1’, ‘pwx’), (‘idz’, ‘addrz’, ‘pwz’),
(‘idy’, ‘addry’, ‘pwx’)]

>>> get_indices(data) >>> [[0, 1, 3], [2]]