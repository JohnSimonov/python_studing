class RedBlackBalancedBinaryTree:
	def __init__(self, make_root = False, root_value = None):
		if make_root:
			self.root = Node(root_value)
		else:
			self.root = None


	def ident(self, depth):
		max_depth = self.depth()
		space_numbers =   2 ** (max_depth - depth ) - 1
		return " " * space_numbers 

	def space_between(self, depth):
		max_depth = self.depth()
		elements_on_level = 2 ** (depth - 1)
		total_space_numbers = 2 ** max_depth - 1
		indent_space_numbers =   2 ** (max_depth - depth ) - 1
		space_between_numbers = (total_space_numbers - 2 * indent_space_numbers - elements_on_level) / (elements_on_level - 1)
		return " " * int(space_between_numbers)


	def depth(self):
		result = 0
		if self.root:
			result = 1
			children = [self.root.left_child, self.root.right_child]
			List_Processor().remove_all(children, None)
			while len(children) > 0:
				result += 1 
				children = [ [child.left_child, child.right_child] for child in children ]
				children = List_Processor().join_lists_inside(children)
				children = List_Processor().remove_all(children, None)


		return result




	def tree_output(self):
		max_depth = self.depth()
		if max_depth > 0:
			cur_depth = 1
			nodes = [self.root]
			except_list = [' ', None]
			while cur_depth <= max_depth:
				children = []
				for i in range(len(nodes)):
					val_for_insert = nodes[i].value if (nodes[i] != ' ') else ' '
					if i == 0:
						print(self.ident(cur_depth) + f'{val_for_insert}', end = '')
					else:
						print(self.space_between(cur_depth) + f'{val_for_insert}', end = '') 
					
					children.append( nodes[i].left_child if ((nodes[i] not in except_list) and nodes[i].left_child) else ' ')
					children.append( nodes[i].right_child if ((nodes[i] not in except_list) and nodes[i].right_child) else ' ')	
				print()
				
				cur_depth += 1	 
				nodes = children
		print()	

        	
	def includes(self, value):
		cur_node = self.root 
		while cur_node:
			if cur_node.value == value:
				return True 
			elif cur_node.value > value:
				cur_node = cur_node.left_child
			else:
				cur_node = cur_node.right_child
		return False

	def add_element(self, value):
		if not self.includes(value):
			if self.root: 
				cur_node = self.root 
				while cur_node.value != value:
					if cur_node.value > value:
						if cur_node.left_child:
							cur_node = cur_node.left_child
						else:
							cur_node.left_child = Node(value)
							cur_node = cur_node.left_child
					elif cur_node.right_child:
						cur_node = cur_node.right_child
					else: 
						cur_node.right_child = Node(value)
						cur_node = cur_node.right_child	
			else:
				self.root = Node(value)


	def balancing(self):
		all_nodes = self.all_nodes
		countine = True
		while countine:
			countine = False
			if self.root.color == 'red':
				self.root.color = 'black'
			for node in all_nodes:
				condition_fst_part_fst = node.right_child and node.right_child == 'red'
				condition_fst_part_snd = node.left_child and node.left_child == 'black'
				condition_fst = condition_fst_part_fst and condition_fst_part_snd

				if condition_fst:
					n			
			


	def all_nodes(self):
		max_depth = self.depth()
		cur_depth = 1
		nodes = [self.root]
		all_nodes = []
		if self.root: 
			all_nodes.append(self.root)
		while cur_depth <= max_depth:
			children = []
			for i in range(len(nodes)):	
				if  nodes[i].left_child:
					children.append( nodes[i].left_child )
				if  nodes[i].right_child:
					children.append( nodes[i].right_child )	
			
				
			cur_depth += 1	 
			nodes = children
			all_nodes += children
		return all_nodes



class Node:
	def __init__(self, value = None, left_child = None, right_child = None):
		self.left_child = left_child
		self.right_child = right_child
		self.value = value
		self.color = 'red'

	def little_left_turn(self):
		temp = self.left_child.right_child
		root_node = self.left_child
		root_node.right_child = self
		root_node.right_child.left_child = temp

		root_node.color = 'black'
		root_node.right_child = 'red'

		return root_node

	def little_right_turn(self):

		temp = self.right_child.left_child

		root_node = self.right_child
		root_node.left_child = self
		root_node.left_child.right_child = temp

		root_node.color = 'black'
		root_node.left_child = 'red'

		return root_node

	def change_color(self):
		self.color = 'red'
		self.left_child.color = 'black'
		self.right_child.color = 'black'


class List_Processor:
	def remove_all(self, input_list, value):
		i = 0
		while i < len(input_list):
			if input_list[i] == value:
				del input_list[i]
			else:
				i += 1
		return input_list

	def join_lists_inside(self, input_list):
		sum_array = []
		for element in input_list:
			sum_array += element

		return sum_array



# tree_fst = RedBlackBalancedBinaryTree(True, 6)
# tree_fst.root.left_child = Node(3)
# tree_fst.root.right_child = Node(8)
# tree_fst.tree_output()
# print([el.value for el in tree_fst.all_nodes()])

# tree_fst.tree_output()
# tree_fst.add_element(7)
# tree_fst.add_element(9)
# tree_fst.tree_output()
tree_fst = RedBlackBalancedBinaryTree()
print(tree_fst.all_nodes())
# print(tree_fst.includes(2))


