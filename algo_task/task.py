class RedBlackBalancedBinaryTree:
	def __init__(self, make_root = False, root_value = None):
		if make_root:
			self.root = Node(root_value, color = 'black')
		else:
			self.root = None


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
		work_node = Node()
		countine = True
		while countine:
			nodes = self.all_nodes()
			countine = False
			if self.root and self.root.color == 'red':
				self.root.color = 'black'
			i = 0
			not_out = True
			while not_out  and i < len(nodes):
				balanced_node = work_node.node_balancing(self.root)
				self.root = balanced_node[0]
				countine = balanced_node[1]
				not_out = not countine

				if nodes[i].left_child:
					left_child = nodes[i].left_child
					balanced_node = work_node.node_balancing(left_child)
					nodes[i].left_child = balanced_node[0]
					countine = balanced_node[1]
					not_out = not countine
				if nodes[i].right_child and not_out:
					right_child = nodes[i].right_child
					balanced_node = work_node.node_balancing(right_child)
					nodes[i].right_child = balanced_node[0]
					countine = balanced_node[1]
					not_out = not countine
				i += 1


			


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
	def __init__(self, value = None, left_child = None, right_child = None, color = 'red'):
		self.left_child = left_child
		self.right_child = right_child
		self.value = value
		self.color = color

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
		return self

	def node_balancing(self, node):
		condition_fst_part_fst = node.right_child and node.right_child.color == 'red'
		condition_fst_part_snd = node.left_child and node.left_child.color == 'black'
		condition_fst = condition_fst_part_fst and condition_fst_part_snd

		condition_snd_part_fst = node.left_child and node.left_child.color == 'red'
		condition_snd = condition_snd_part_fst and node.left_child.left_child and node.left_child.left_child.color == 'red'

		condition_thd_part_fst = node.right_child and node.right_child.color == 'red'
		condition_thd_part_snd = node.left_child and node.left_child.color == 'red'
		condition_thd = condition_thd_part_fst and condition_thd_part_snd
				
		if condition_fst:
			return [node.little_right_turn(), True, 'fst']	
		elif condition_snd:	
			return [node.little_left_turn(), True, 'snd']
		elif condition_thd:
			return [node.change_color(), True, 'thd']	
		return [node, False, 'fth']


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



tree_fst = RedBlackBalancedBinaryTree(True, 2)

tree_fst.add_element(1)
tree_fst.balancing()

tree_fst.add_element(3)
tree_fst.balancing()

tree_fst.add_element(7)
tree_fst.balancing()

tree_fst.add_element(9)
tree_fst.balancing()







