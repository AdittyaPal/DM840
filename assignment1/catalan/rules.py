pushFilePrefix("rules/")
mark = ruleGML("markForConversion.gml")
removeR_unmarkA = ruleGML("removeSingleR.gml")
reattachExternal = ruleGML("reattachExternalEdge.gml")
removeAttached = ruleGML("removeAlreadyAttached.gml")
#rejectFourth = ruleGML("rejectFourthNode.gml")
removeInterR = ruleGML("removeInterREdge.gml")
#unmark = ruleGML("unmarkCollapsedNode.gml")
popFilePrefix()
