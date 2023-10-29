rule [
	ruleID "Remove R Nodes"	
	left [
		node[id 0 label "A"]
		node[id 1 label "R"]
		node[id 2 label "R"]
		node[id 3 label "R"]
		edge[source 0 target 1 label "-"]
		edge[source 0 target 2 label "-"]
		edge[source 0 target 3 label "-"]
	]
	context [
	]
	right [
		node[id 0 label "0"]
	]
]
