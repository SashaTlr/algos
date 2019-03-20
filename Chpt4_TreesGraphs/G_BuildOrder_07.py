#have an array with each graph node

#track inboudn and outbound edges

#if node only has inbound edges, build that node and delete edges

class Node:
	def __init__(self, value, state = buildStatus.BLANK):
		self.value = value
		self.edges = []
		self.dependencies_left = 0
		self.state = state

	def add_edge(self, node):
		self.edges.append(node)
		node.dependencies_left += 1
		return self

def build_project_order(projects, dependencies):
	projectList = []

	for project in projects:
		projectList.append(Node(project))

	for (node, dependency) in dependencies:
		projectList[node].add_edge(dependency)

	queue = []
	build_order = []

	for node in projectList:
		if not node.dependencies_left:
			queue.append(node)

	while len(queue) > 0:
		node = queue.pop(0)
		build_order.append(node)

		for edgeNode in node.edges:
			edgeNode.dependencies_left -= 1
			if not edgeNode.dependencies_left:
				queue.append(edgeNode)


	if len(build_order) < len(projectList):
		raise Exception('Cycle in project dependencies')

	return build_order

import enum
class buildStatus(enum.enum):
	BLANK = 1,
	PARTIAL = 2,
	COMPLETE = 3

def BuildGraph(projects, dependencies):
	projectList = []

	for project in projects:
		projectList.append(Node(project))

	for (node, dependency) in dependencies:
		projectList[node].add_edge(dependency)

	return projectList


#basically, always iterate through project nodes in an array
#the build order is needed to get 'stray' projects since they wont all link together 
#as you iterate through each node, if the node is blank, it's children have to be processed
#as each node completes, it rolls up one and completes

def build_project_order_dfs(projects, dependencies):

	graph = BuildGraph(projects, dependencies)

	return buildOrder(graph)

def buildOrder(projects):

	buildOrder = []

	stack = []

	for project in projects:
		if project.state == buildStatus.BLANK:
			if not DoDFS(project, stack):
				return null

	return stack

def DoDFS(node, stack):
	if node.state == buildStatus.PARTIAL:
		return false
	#project has a cycle

	if node.state == buildStatus.BLANK:
		node.state = buildStatus.PARTIAL

	#change state before moving to child node
	#if child has cycle, returns back to parent node

	for child in node.dependencies:
		if not DoDFS(child, stack):
			return false

	node.state = buildStatus.COMPLETE
	stack.append(node)

	return true










