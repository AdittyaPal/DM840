rule [
	ruleID "Remove Inter R-Node Edges"	
	left [
		edge[source 0 target 1 label "-"]
	]
	context [
		node[id 0 label "R"]
		node[id 1 label "R"]
	]
	right [
	]
]
