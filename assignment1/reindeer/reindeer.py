s = "SAAAEBBBT"
t = "TAAAEBBBS"
g = graphDFS("".join("[%s]" % a for a in s))
g.print()
goal = graphDFS("".join("[%s]" % a for a in t))
goal.print()

Jump = ruleGMLString("""rule [
	ruleID "Jump"
	left [
		edge[source 1 target 2 label "-"]
		edge[source 5 target 4 label "-"]
	]
	context [
		node[id 1 label "*"]
		node[id 2 label "E"]
		node[id 3 label "*"]
		node[id 4 label "*"]
		node[id 5 label "*"]
		edge[source 2 target 3 label "-"]
		edge[source 4 target 3 label "-"]
	]
	right [
		edge[source 1 target 4 label "-"]
		edge[source 5 target 2 label "-"]
	]
]""")

Move = ruleGMLString("""rule [
	ruleID "Move"
	left [
		edge[source 1 target 2 label "-"]
		edge[source 4 target 3 label "-"]
	]
	context [
		node[id 1 label "*"]
		node[id 2 label "E"]
		node[id 3 label "*"]
		node[id 4 label "*"]
		edge[source 2 target 3 label "-"]
	]
	right [
		edge[source 1 target 3 label "-"]
		edge[source 4 target 2 label "-"]
	]
]""")

for a in inputRules: a.print()

dg = DG(
	labelSettings=LabelSettings(
		LabelType.Term, 
		LabelRelation.Specialisation), 
	graphDatabase=inputGraphs)
dg.build().execute(addSubset(g) >> repeat(inputRules))

p = DGPrinter()
p.graphvizPrefix=' layout = "dot"; '

def setPrinter(p):
	p.withRuleName = True
	p.pushVertexColour(lambda a: "blue" if a.graph == g else "")
	p.pushVertexColour(lambda a: "red" if a.graph == goal else "")
setPrinter(p)
dg.print(p)

# The following is a rather brutal sledgehammer-approach.
#
# You could also use, e.g., networkx to find a shortest path
# in the derivation graph, as the derivation graph is very
# likely a directed graph (i.e., not a hyper.graph)

flow = Flow(dg)
flow.addSource(g)
flow.addSink(goal)
flow.addConstraint(inFlow(g) == 1)
flow.setSolverEnumerateBy(absGap=0)
flow.calc()
fp = FlowPrinter()
setPrinter(fp.dgPrinter)
for s in flow.solutions:
	s.print(fp)

