rule [
	ruleID "Reattach External Edges"	
	left [
		edge[source 0 target 1 label "-"]
	]
	context [
		node[id 0 label "0"]
		node[id 1 label "R"]
		node[id 2 label "A"]
		edge[source 1 target 2 label "-"]
	]
	right [
		edge[source 0 target 2 label "-"]
	]
]
